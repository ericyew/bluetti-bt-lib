import asyncio
import logging
import async_timeout
from typing import Any, Callable, cast
from bleak import BleakClient
from bleak.exc import BleakError

from ..registers import ReadableRegisters
from ..const import NOTIFY_UUID, WRITE_UUID
from ..base_devices import BluettiDevice

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)  # TODO Remove before release


class DeviceReaderConfig:
    def __init__(self):
        self.timeout = 60


class DeviceReader:
    def __init__(
        self,
        bleak_client: BleakClient,
        bluetti_device: BluettiDevice,
        future_builder_method: Callable[[], asyncio.Future[Any]],
        config: DeviceReaderConfig | None = None,
    ):
        self.client = bleak_client
        self.bluetti_device = bluetti_device
        self.create_future = future_builder_method

        if config is not None:
            self.config = config
        else:
            self.config = DeviceReaderConfig()

        self.has_notifier = False
        self.current_registers = None
        self.notify_response = bytearray()
        self.notify_future: asyncio.Future[Any] | None = None

        self.polling_lock = asyncio.Lock()

    async def read(self) -> dict | None:
        registers = self.bluetti_device.get_polling_registers()

        parsed_data: dict = {}

        _LOGGER.debug("Reading device registers")

        async with self.polling_lock:
            try:
                async with async_timeout.timeout(self.config.timeout):
                    if not self.client.is_connected:
                        _LOGGER.debug("Connecting to device")
                        await self.client.connect()

                    _LOGGER.debug("Connected to device")

                    if not self.has_notifier:
                        await self.client.start_notify(
                            NOTIFY_UUID, self._notification_handler
                        )
                        self.has_notifier = True

                    _LOGGER.debug("Notification handler setup complete")

                    for register in registers:
                        body = register.parse_response(
                            await self._async_send_command(register)
                        )

                        _LOGGER.debug("Raw data: %s", body)

                        parsed = self.bluetti_device.parse(
                            register.starting_address, body
                        )

                        _LOGGER.debug("Parsed data: %s", parsed)

                        parsed_data.update(parsed)

            except TimeoutError:
                _LOGGER.warning("Timeout")
                return None
            except BleakError as err:
                _LOGGER.warning("Bleak error: %s", err)
                return None
            except BaseException as err:
                _LOGGER.warning("Unknown error: %s", err)
                return None
            finally:
                if self.has_notifier:
                    try:
                        await self.client.stop_notify(NOTIFY_UUID)
                        _LOGGER.debug("Stopped notifier")
                    except:
                        # Ignore errors here
                        pass
                    self.has_notifier = False
                await self.client.disconnect()
                _LOGGER.debug("Disconnected from device")

            # Check if dict is empty
            if not parsed_data:
                return None

            return parsed_data

    async def _async_send_command(self, registers: ReadableRegisters) -> bytes:
        """Send command and return response"""
        self.current_registers = registers
        self.notify_response = bytearray()
        self.notify_future = self.create_future()

        try:
            # Make request
            await self.client.write_gatt_char(WRITE_UUID, bytes(registers))

            _LOGGER.debug("Request sent (%s)", registers)

            # Wait for response
            res = await asyncio.wait_for(self.notify_future, timeout=5)

            _LOGGER.debug("Got response")

            return cast(bytes, res)
        except:
            _LOGGER.warning("Error while reading data")

        return bytes()

    def _notification_handler(self, _: int, data: bytearray):
        """Handle bt data."""
        _LOGGER.debug("Got new data")

        # Save data
        self.notify_response.extend(data)
        self.notify_future.set_result(self.notify_response)

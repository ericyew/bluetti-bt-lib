import struct
from decimal import Decimal

from . import DeviceField


class VersionField(DeviceField):
    def __init__(self, name: str, address: int):
        super().__init__(name, address, 2)

    def parse(self, data: bytes) -> int:
        values = struct.unpack("!2H", data)
        return Decimal(values[0] + (values[1] << 16)) / 100

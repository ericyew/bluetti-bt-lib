from typing import List

from . import BluettiDevice
from ..fields import DeviceField
from ..fields import FieldName, SwapStringField, UIntField


class BaseDeviceV2(BluettiDevice):
    def __init__(self, mac: str, additional_fields: List[DeviceField] = []):
        super().__init__(
            mac,
            [
                SwapStringField(FieldName.DEVICE_TYPE, 110, 6),
                UIntField(FieldName.BATTERY_SOC, 102),
            ]
            + additional_fields,
        )

from typing import List

from . import BluettiDevice
from ..fields import DeviceField
from ..fields import FieldName, StringField, UIntField


class BaseDeviceV1(BluettiDevice):
    def __init__(self, mac: str, additional_fields: List[DeviceField] = []):
        super().__init__(
            mac,
            [
                StringField(FieldName.DEVICE_TYPE, 10, 6),
                UIntField(FieldName.BATTERY_SOC, 43),
                UIntField(FieldName.DC_INPUT_POWER, 36),
                UIntField(FieldName.AC_INPUT_POWER, 37),
                UIntField(FieldName.DC_OUTPUT_POWER, 38),
                UIntField(FieldName.AC_OUTPUT_POWER, 39),
            ]
            + additional_fields,
        )

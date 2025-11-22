import struct
from decimal import Decimal

from . import DeviceField


class DecimalArrayField(DeviceField):
    def __init__(self, name: str, address: int, size: int, scale: int):
        super().__init__(name, address, size)
        self.scale = scale

    def parse(self, data: bytes) -> Decimal:
        values = list(struct.unpack(f"!{self.size}H", data))
        return [Decimal(v) / 10 ** self.scale for v in values]

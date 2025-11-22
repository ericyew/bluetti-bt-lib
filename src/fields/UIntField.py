import struct

from . import DeviceField


class UIntField(DeviceField):
    def __init__(self, name: str, address: int):
        super().__init__(name, address, 1)

    def parse(self, data: bytes) -> int:
        val = struct.unpack("!H", data)[0]
        return val

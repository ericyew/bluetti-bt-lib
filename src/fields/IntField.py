import struct

from . import DeviceField


class IntField(DeviceField):
    def __init__(self, name: str, address: int):
        super().__init__(name, address, 1)

    def parse(self, data: bytes) -> int:
        return struct.unpack(">h", data)[0]

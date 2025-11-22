from . import DeviceField


class StringField(DeviceField):
    def __init__(self, name: str, address: int, size: int):
        super().__init__(name, address, size)

    def parse(self, data: bytes) -> str:
        return data.rstrip(b"\0").decode("ascii")

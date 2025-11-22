from typing import Any

from ..fields import FieldName


class DeviceField:
    def __init__(self, name: FieldName, address: int, size: int):
        self.name = name.value
        self.address = address
        self.size = size

    def parse(self, data: bytes) -> Any:
        raise NotImplementedError

from ..base_devices import BaseDeviceV1


class EB3A(BaseDeviceV1):
    def __init__(self, mac: str):
        super().__init__(mac)

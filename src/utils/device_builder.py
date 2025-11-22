"""Device builder helper."""

from ..const import DEVICE_NAME_RE
from ..base_devices import BluettiDevice

# Add new classes below
from ..devices.ac180 import AC180
from ..devices.eb3a import EB3A


def build_device(mac: str, name: str) -> BluettiDevice | None:
    devMatch = DEVICE_NAME_RE.match(name)

    if devMatch is None:
        return None

    devType = devMatch[1]

    if devType is None:
        return None

    Station = None

    # Add new classes as case below
    match devType:
        case "AC180":
            Station = AC180
        case "EB3A":
            Station = EB3A

    if Station is None:
        return None

    return Station(mac)

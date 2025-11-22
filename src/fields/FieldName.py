from enum import Enum, unique


@unique
class FieldName(Enum):
    DEVICE_TYPE = "device_type"
    DC_INPUT_POWER = "dc_input_power"
    DC_OUTPUT_POWER = "dc_output_power"
    AC_INPUT_POWER = "ac_input_power"
    AC_OUTPUT_POWER = "ac_output_power"
    BATTERY_SOC = "total_battery_percent"

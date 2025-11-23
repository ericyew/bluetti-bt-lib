# bluetti-bt-lib
Inofficial Library for basic communication to bluetti powerstations.

## Disclaimer
This library is provided without any warranty or support by Bluetti. I do not take responsibility for any problems it may cause in all cases. Use it at your own risk.

## Installation

```bash
pip install bluetti-bt-lib
```

## Commands for testing

### Scan for supported devices

```bash
usage: bluetti-scan [-h]

Detect bluetti devices by bluetooth name

options:
  -h, --help  show this help message and exit
```

### Detect device type by mac address

```bash
usage: bluetti-detect [-h] mac

Detect bluetti devices

positional arguments:
  mac         Mac-address of the powerstation

options:
  -h, --help  show this help message and exit
```

### Read device data for supported devices

```bash
usage: bluetti-read [-h] [-m MAC] [-t TYPE] [-e ENCRYPTION]

Detect bluetti devices

options:
  -h, --help            show this help message and exit
  -m MAC, --mac MAC     Mac-address of the powerstation
  -t TYPE, --type TYPE  Type of the powerstation (AC70 f.ex.)
  -e ENCRYPTION, --encryption ENCRYPTION
                        Add this if encryption is needed
```

## Supported Powerstations and data

Validated

|Device Name|total_battery_percent|dc_input_power|ac_input_power|dc_output_power|ac_output_power|
|-----------|---------------------|--------------|--------------|---------------|---------------|
|AC70       |✅                   |✅            |✅            |✅             |✅             |
|AC180      |✅                   |✅            |✅            |✅             |✅             |
|EB3A       |✅                   |✅            |✅            |✅             |✅             |
|Handsfree 1|✅                   |✅            |✅            |✅             |✅             |

Added and mostly validated by contributors (some are moved here from the HA Integration https://github.com/Patrick762/hassio-bluetti-bt):

|Device Name|Contributor     |total_battery_percent|dc_input_power|ac_input_power|dc_output_power|ac_output_power|
|-----------|----------------|---------------------|--------------|--------------|---------------|---------------|
|AC2A       |@ruanmed        |✅                   |✅            |✅            |✅             |✅             |
|AC60       |@mzpwr          |✅                   |✅            |✅            |✅             |✅             |
|AC60P      |@mzpwr          |✅                   |✅            |✅            |✅             |✅             |
|AC70P      |@matthewpucc    |✅                   |❌            |❌            |❌             |❌             |
|AC180P     |@Patrick762     |✅                   |✅            |✅            |✅             |✅             |

## Controls

Controls will be migrated to this library soon

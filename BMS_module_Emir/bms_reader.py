from smbus2 import SMBus
import yaml
# for register definitions refer to link below:
# https://www.ti.com/lit/ug/sluubc1d/sluubc1d.pdf?ts=1714639201228&ref_url=https%253A%252F%252Fduckduckgo.com%252F
bus = SMBus(1)  # 1 indicates /dev/i2c-1
BQ20Z45_DEVICE_ADDRESS = 0x0b  # replace with your device address
conf_path = '/home/ibex/Documents/BMS/BMS_module/registers.yml'
with open(conf_path, 'r') as file:
    registers = yaml.safe_load(file)

for name, register in registers.items():
    if isinstance(register,dict) or isinstance(register,str):
        continue
    try:
        value = bus.read_word_data(BQ20Z45_DEVICE_ADDRESS, register)
        print(f"{name}: {value}")
    except IOError:
        print(f"Error reading {name}")
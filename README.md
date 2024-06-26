# setup SMBUS
install smbus2:
pip3 install smbus2

On the Jetson Nano, the I2C interface available on pins 3 (SDA) and 5 (SCL) corresponds to I2C bus 1. Here’s a detailed mapping of the I2C pins on the Jetson Nano:

Jetson Nano I2C Pin Mapping
I2C Bus 1:
SDA (Data Line): Pin 3 (GPIO2 SDA)
SCL (Clock Line): Pin 5 (GPIO3 SCL)
Summary
So, for the Jetson Nano:

Pin 3 (SDA) corresponds to I2C bus 1 SDA.
Pin 5 (SCL) corresponds to I2C bus 1 SCL.

# setup tint2 for battery indicator
1- install tint2
create config file as ~/.config/tint2/tint2rc
a sample tint file is present at the repo

2- Create a systemd service file for tint2 (as root or using sudo):
sudo vim /etc/systemd/system/tint2.service with content below:

[Unit]
Description=tint2 Panel

[Service]
ExecStart=/usr/bin/tint2

[Install]
WantedBy=default.target

3- Enable and start the service:

sudo systemctl enable --now tint2.service

4- make the comand run on startup:
vim ~/.config/openbox/autostart
add the following to the file
tint2 &

5- run:
openbox --reconfigure

6- create a file in anywhere you want named battery_icon_script.sh and write the below in it.

#!/bin/bash

# Get the current battery percentage
battery_level=$(cat /sys/class/power_supply/BAT0/capacity)

# Determine which icon to show based on battery level
if [ "$battery_level" -ge 75 ]; then
    echo '/path/to/full_battery_icon.png'
elif [ "$battery_level" -ge 50 ]; then
    echo '/path/to/half_battery_icon.png'
elif [ "$battery_level" -ge 25 ]; then
    echo '/path/to/low_battery_icon.png'
else
    echo '/path/to/very_low_battery_icon.png'
fi



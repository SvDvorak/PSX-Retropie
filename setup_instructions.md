

# Configuring PSX Retropie #
# IF NOT SPECIFIED, ASSUME THAT WORKING DIRECTORY IS HOME

## User ##
# default user is pi with password raspberry
passwd  # change pi password to something safer
sudo adduser daniel
sudo visudo
# add the line under root:
# daniel  ALL=NOPASSWD: ALL
update-alternatives --set editor /usr/bin/vim.tiny  # change to vim (for my sanity)
echo "alias vim=\"vim.tiny\"" >> .bashrc  # shortcut!


## Wifi ##
# Source: https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
sudo raspi-config
# setup Wifi in config
# IMPORTANT! Reboot afterwards
sudo ifconfig   # should show that you are connected
sudo apt-get update && sudo apt-get upgrade


## Installing RetroPie ##
# Source:
#  - https://retropie.org.uk/forum/topic/23859/pi4b-lagging-n64-mario-kart/4
#  - https://github.com/RetroPie/RetroPie-Setup/wiki/Manual-Installation
sudo raspi-config
# Change Advanced - Memory Split to something larger like 256MB
# Enable OpenGL driver, set to GL (Fake KMS)
# Change autostart to Start Emulation Station at boot
# Change locale to include sv_SE.UTF-8 AND en_US.UTF-8 with US as default (needed for RetroPie)
sudo update-locale LANG="en_US.UTF-8"
sudo update-locale LANGUAGE="en_US:en"
sudo update-locale LC_ALL="en_US.UTF-8"
locale  # SHOULD show all fields as "en_US.UTF-8" except LANGUAGE=en_US:en and LANG & LC_ALL =en_US.UTF-8
# IMPORTANT! Reboot afterwards
sudo apt-get install git lsb-release
git clone --depth=1 https://github.com/RetroPie/RetroPie-Setup.git
cd RetroPie-Setup
chmod +x retropie_setup.sh
sudo ./retropie_setup.sh


## Samba share ##
# Source: https://www.htpcguides.com/create-samba-share-raspberry-pi/

sudo apt-get install samba samba-common-bin -y
# allow WINS during installation
sudo chown -R daniel:daniel /home/daniel/RetroPie  # got to own the share
sudo cp /etc/samba/smb.conf /etc/samba/smb.bak  # backup
sudo vi /etc/samba/smb.conf
# edit the following:
# [PSX]
# comment = PSX ROMS
# path = /home/daniel/RetroPie/roms/psx
# create mask = 0775
# directory mask = 0775
# read only = no
# browseable = yes
# public = yes
# force user = daniel
# only guest = no
sudo service smbd restart   # restart samba to apply config
sudo service nmbd restart


## Copy files ##
# copy over control_retropie_system.py, psx_buttons.py, psx_buttons.service, cooling_fan.py, cooling_fan.service, psx_boot.mkv to home


## Power LED ##
# Source:
#   - https://raspberrypi.stackexchange.com/questions/77905/raspberry-pi-3-model-b-dtoverlay-gpio-shutdown
#   - https://howchoo.com/g/ytzjyzy4m2e/build-a-simple-raspberry-pi-led-power-status-indicator
# Connect LED to GPIO14/TxD (pin 8) and Ground (pin 14)
sudo vim.tiny /boot/config.txt
# add the following lines:
enable_uart=1


## Power button, Reset button & cooling fan ##
# Source:
#   - https://retropie.org.uk/forum/topic/12424/retroflag-nespi-case-soft-power-reset-hack/2
#   - https://www.raspberrypi.org/forums/viewtopic.php?p=921354#p921354
#   - https://www.raspberrypi.org/documentation/linux/usage/systemd.md
#   - https://www.raspberrypi.org/forums/viewtopic.php?p=1220502
# Connect Power to GPIO3 (pin 5) and Ground (pin 6)
# Connect Reset to GPIO4 (pin 7) and Ground (pin 9)
sudo apt install python3-gpiozero
sudo mv psx_buttons.service /etc/systemd/system/
sudo mv cooling_fan.service /etc/systemd/system/
sudo chmod u+rw /etc/systemd/system/psx_buttons.service
sudo chmod u+rw /etc/systemd/system/cooling_fan.service
sudo systemctl enable psx_buttons.service
sudo systemctl enable cooling_fan.service
sudo vim.tiny /opt/retropie/configs/all/retroarch.cfg
# uncomment and set 'network_cmd_enable' to true



# VERY IMPORTANT THAT YOU CONNECT FAN CIRCUIT PROPERLY! CONNECTING 5V TO PIN ACCIDENTALLY COULD SMOKE YOUR RASBERRY PI
# Connect 5V (pin 2) circuit positive
# Connect circuit positive to fan positive
# Connect fan negative to transistor collector
# Connect GPIO24 (pin 18) to transistor base
# Connect circuit negative to Ground (pin 20)


## PSX install ##
# Source: https://github.com/RetroPie/RetroPie-Setup/wiki/Playstation-1
# acquire PSX BIOS and copy over to PSX ROMS, then:
mv ~/RetroPie/roms/psx/BIOS_NAME.BIN ~/RetroPie/BIOS/
# copy over any other roms, MUST have both .bin AND .cue to be registered
# Dont forget to run scraper to get cover art!
# If you have a whole bunch of bin files and missing a cue file, go here and generate one http://nielsbuus.dk/pg/psx_cue_maker/


## Swap A/B in menus
sudo vim.tiny /opt/retropie/configs/all/autoconf.cfg
# change es_swap_a_b to 1
# make sure to reconfigure controller if it doesn't work at first!


## Splash screen ##
mv psx_boot.mkv RetroPie/splashscreens/psx_boot.mkv
# Go to Retropie settings tab in emulationstation
splash screens -> Choose splashscreen ...

    # NO LONGER NEEDED SINCE OFFICIAL RPI4 RELEASE IS OUT, SAVED FOR LEGACY.
    sudo mv psx_boot.service /etc/systemd/system/
    sudo chmod u+rw /etc/systemd/system/psx_boot.service
    sudo systemctl enable psx_boot.service


## Settings ##
# scrape game covers
# UI Settings -> Theme Set -> Carbon
#                Gamelist View Style -> Detailed
#                Start On System -> PSX
# Other Settings -> Use OMX Player -> On
# Other Settings -> Save Metadata On Exit -> On
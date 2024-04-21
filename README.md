
# PSX Retropie

For my brother's birthday I wanted to make something special. As the original Playstation is near to his heart I converted an old one to hold a Raspberry Pi, with completely functional controller ports, power & reset buttons, power LED and USB ports in the memory slots.

This repository contains the scripts and Raspberry Pi configuration steps I used.

DISCLAIMER: It was more than 5 years ago I wrote these scripts and the setup config. I leave no guarantees that they'll work for you.

For the physical parts:
[https://www.thingiverse.com/thing:4371570](Print files (Thingiverse))
[https://anwilc.com/2019/12/06/PSX_Retropie.html](Build log)

The model of the PSX is an SCPH-5552 (european). 

NOTE: Many of these models are based on both parts I already had on hand and others I've bought (some of which I've listed below). This print requires you to modify the PSX case itself quite a bit to make them fit (USB ports, cooling fan and more). This is not a straight & easy build but it might make a good start.

These were some of the parts I've bought for this project from a swedish electronics store, some I already had on hand.

- [https://www.electrokit.com/en/product/usb-a-female-pcb-straight/](USB-A female pcb straight (two for the front USB))
- [https://www.electrokit.com/en/product/usb-c-monterad-pa-kort/](USB-C breakout board (for power connector in the back))
- [https://www.electrokit.com/en/product/usb-cable-a-male-c-male-0-5m/](USB cable A-male – C-male 0.5m (RPi power to USB-C on PCB above))
- [https://www.electrokit.com/en/product/micro-switch-d2f-on-on-no-lever/](Micro switch D2F on-(on) no lever (for the reset button))
- [https://www.electrokit.com/en/product/micro-switch-d2f-on-on-with-lever/](Micro switch D2F on-(on) with lever (for the power button))
- [https://japanspelshop.se/index.php?route=product/product&path=185_72_161&product_id=6769](PS1 / PS2 adapter for USB)
- Found a short HDMI micro male to HDMI female in a local shop
- Used an old PSU fan for cooling (12V but running at 5V, slowly)
- LED's are I believe 5mm ones, unsure of strength
- Assorted USB & network cables for cabling

The Raspberry Pi mount I created is a remix of this one:
https://www.thingiverse.com/thing:2012518That model does not allow for derivatives to be distributed. So for a RPi mount I point you to their solution.

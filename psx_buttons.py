#! /usr/bin/env python3

from gpiozero import Button
from signal import pause
import sys
from control_retropie_system import do_quit, do_shutdown 

quitPin = int(sys.argv[1]) if len(sys.argv) >= 2 else 4
shutdownPin = int(sys.argv[2]) if len(sys.argv) >= 2 else 3

quitBtn = Button(quitPin)
quitBtn.when_pressed = do_quit

rebootBtn = Button(shutdownPin)
rebootBtn.when_pressed = do_shutdown

pause()

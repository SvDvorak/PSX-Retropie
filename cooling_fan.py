
# Run cooling fan #

from gpiozero import LED
from signal import pause

cooling_fan = LED(24) # Sets pin to high, LED works fine here

cooling_fan.on()

pause()
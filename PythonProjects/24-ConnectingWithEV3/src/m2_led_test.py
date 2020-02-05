"""
The goal of this module is to practice using the rosebot library.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time
# -----------------------------------------------------------------------------
# TODO: 2.  Uncomment the line below. Then open that file and search for the
#  LED class so that you can understand what it does.
# -----------------------------------------------------------------------------

# import rosebot_ev3dev_api as rose_ev3

# -----------------------------------------------------------------------------
# TODO: 3.  Create an LED object for the right LED using the pattern shown below
# -----------------------------------------------------------------------------
left_led = rose_ev3.Led("left")

# -----------------------------------------------------------------------------
# TODO: 4.  Modify the example code below to make something interesting
#            happen with the left and right LEDs. Perhaps police lights or...
# -----------------------------------------------------------------------------
print("Look at your EV3 robot -->")
for k in range(10):
    left_led.set_color("red")
    time.sleep(0.25)
    left_led.turn_off()
    time.sleep(0.25)

left_led.set_color("green")
print("Goodbye")

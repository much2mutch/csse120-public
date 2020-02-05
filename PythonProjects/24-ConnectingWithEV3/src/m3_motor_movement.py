"""
The goal of this module is to again use the rosebot library, but with a motor

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time

# -----------------------------------------------------------------------------
# TODO: 2.  Create a Motor object for Large Motor C using the pattern below
#           You will need to open the rosebot_ev3dev_api to learn about that
#           the motor class and you will need to import that module:
#               import rosebot_ev3dev_api as rose_ev3
# -----------------------------------------------------------------------------
left_motor = rose_ev3.Motor("B")

# -----------------------------------------------------------------------------
# TODO: 2.  Modify the example code below to make something interesting
#            happen with the motors. Perhaps spinning in a circle or driving
#            in a square.
# -----------------------------------------------------------------------------
print("Look at your EV3 robot -->")
input("Press the ENTER key when ready for the robot to start moving.")
for k in range(3):
    left_motor.turn_on(30)
    time.sleep(3)
    left_motor.turn_on(80)
    time.sleep(0.5)
    left_motor.turn_off()
    time.sleep(2)

print("Goodbye")

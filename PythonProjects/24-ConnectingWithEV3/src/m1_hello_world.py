"""
The goal of this module is to practice running code on the EV3.

Authors: David Mutchler, Vibha Alangar, Dave Fisher, and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import time

# -----------------------------------------------------------------------------
# TODO: 2.  PUT YOUR NAME IN THE BELOW LINE.
#
# With your instructors help, connect to your EV3, transfer this file to the
# EV3, make an ssh connection to your EV3, get into the correct folder, then
# run this program on your robot (NOT on your computer!) using the command:
#
# python m1_hello_world.py
# -----------------------------------------------------------------------------
name = "PUT_YOUR_NAME_HERE"
for k in range(10):
    print(k, "Hello, " + name)
    time.sleep(0.75)
print("Goodbye")

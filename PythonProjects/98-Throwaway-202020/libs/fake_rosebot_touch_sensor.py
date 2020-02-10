"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the TouchSensor class, for the robot's touch sensor
that detects when the arm and claw are in the fully-up position.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.


import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    TouchSensor
###############################################################################
class TouchSensor(object):
    """
    An object associated with a physical Touch Sensor that is plugged into
    a port (1, 2, 3, or 4).  It has methods:
      get_reading    is_pressed    wait_until_pressed   wait_until_not_pressed
    """
    def __init__(self, port=None):
        """
        Constructs the underlying low-level version of this sensor.
        Doing so enforces the requirement:
          The  port  must be 1, 2, 3, 4, or None, where  None  means to attempt
          to autodetect a port into which a physical Touch Sensor is plugged.
        ---
        :param port:  The port (1, 2, 3, or 4) into which a Touch Sensor is
                      plugged, or None to attempt to autodetect such a port.
        :type port: int | None
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.touch_sensor = rose_ev3.TouchSensor(port)

    def is_pressed(self):
        """
        Returns True if this TouchSensor is pressed, else returns False.
        ---
        :rtype: bool
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        return self.touch_sensor

    def wait_until_pressed(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the touch sensor to be pressed.
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        while True:
            time.sleep(0.05)
            if self.is_pressed():
                break

    def wait_until_pressed(self):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the touch sensor to be pressed.
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------
        while True:
            time.sleep(0.05)
            if self.is_pressed():
                break

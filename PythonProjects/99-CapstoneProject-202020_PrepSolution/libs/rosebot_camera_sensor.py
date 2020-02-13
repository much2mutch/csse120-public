"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the CameraSensor.

Authors:  Your professors (for the framework) and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    CameraSensor
###############################################################################
class CameraSensor(object):
    """
    """

    def __init__(self, port):
        """
        Constructs the underlying low-level InfraredBeaconSensor.
          :type port: int
          :type channel: int
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.port = port
        self.camera = None  # Only enable the camera if it is actually used.
        self.has_been_enabled = False

    def enable(self):
        """

        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.camera = rose_ev3.Camera(2)
        self.has_been_enabled = False


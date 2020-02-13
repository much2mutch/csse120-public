"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the BeaconSensor class, for the robot's forward
facing sensor. The infrared sensor when it is in the mode does not emit light
it only looks for the light coming from the Remote Control.  The remote control
must be running in beacon mode (the top button) for this class to work.

Authors:  Your professors (for the framework) and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import rosebot_ev3dev_api as rose_ev3
import time


###############################################################################
#    BeaconSensor
###############################################################################
class BeaconSensor(object):
    """
    Methods for the forward-facing InfraredProximitySensor on the robot, including:
      get_distance     wait_until_distance_less_than
    """

    def __init__(self, port, channel, drive_system):
        """
        Constructs the underlying low-level InfraredBeaconSensor.
          :type port: int
          :type channel: int
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.port = port
        self.channel = channel
        self.drive_system = drive_system
        self.sensor = None  # To avoid conflict only make the lower level sensor if enabled.
        self.has_been_enabled = False

    def enable(self):
        self.sensor = rose_ev3.InfraredBeaconSensor(self.port, self.channel)
        self.has_been_enabled = False

    def spin_until_beacon_seen(self):
        if not self.has_been_enabled:
            self.enable()

    def drive_to_beacon(self):
        if not self.has_been_enabled:
            self.enable()
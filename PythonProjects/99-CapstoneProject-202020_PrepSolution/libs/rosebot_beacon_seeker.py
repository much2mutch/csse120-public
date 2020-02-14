"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the BeaconSensor class which is used to track the beacon
(i.e. the remote control). The beacon sensor uses the same hardware as the
infrared proximity sensor and the remote control receiver.  The infrared
sensor not emit light when set to the beacon mode (that only happen for the
infrared proximity sensor), instead it only looks for the light coming
from the Remote Control.  The remote control must be running in beacon mode
(the top button) for this class to work.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import rosebot_ev3dev_api as rose_ev3
import rosebot_drive_system


###############################################################################
#    BeaconSeeker
###############################################################################
class BeaconSeeker(object):
    """
    Methods for the forward-facing InfraredProximitySensor on the robot, including:
      get_distance     wait_until_distance_less_than
    """
    beacon_sensor: rose_ev3.InfraredBeaconSensor
    drive_system: rosebot_drive_system.DriveSystem

    def __init__(self, port, channel, drive_system):
        """
        Constructs the underlying low-level InfraredBeaconSensor.
          :type port: int
          :type channel: int
          :type drive_system: rosebot_drive_system.DriveSystem
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.port = port
        self.channel = channel
        self.drive_system = drive_system
        self.beacon_sensor = None  # To avoid conflicts only make the sensor if enabled.
        self.has_been_enabled = False

    def enable(self):
        """
        Enables the Infrared Sensor of the robot to be used with Beacon Seeking.
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.beacon_sensor = rose_ev3.InfraredBeaconSensor(self.port, self.channel)
        self.has_been_enabled = False

    def spin_until_beacon_seen(self, heading_threshold):
        """
        Spins the robot CW until the beacon is seen with an abs(heading) less
        than the given heading_threshold.  Once the beacon heading is within
        the threshold the drive system should stop.

        This method also needs to check if the beacon sensor has been enabled.
        If it has not been enabled it will call enable before it begins.
        :param heading_threshold: Required threshold for the heading (in degrees)
        :type heading_threshold: float
        """
        if not self.has_been_enabled:
            self.enable()

        self.drive_system.go(50, -50)
        while True:
            time.sleep(0.05)
            # ---------------------------------------------------------------------
            # TODO: Implement this method.
            # ---------------------------------------------------------------------

            # Solution to be removed
            heading = self.beacon_sensor.get_heading_to_beacon()
            if abs(heading) < heading_threshold:
                break
        self.drive_system.stop()

    def spin_to_track_beacon(self, duration_s):
        """
        This method should make the robot spin to follow the beacon.  The robot
        will not move forward it will only spin in place to continuously follow
        the beacon left and right.
        After duration_s seconds have passed this method will stop both motors.
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # Hint towards implementing the duration_s requirement...
        # start_time_s = time.time()
        # while True:
        #     time.sleep(0.05)
        #     if time.time() > start_time_s + duration_s:
        #         break
        # ---------------------------------------------------------------------

        # Solution to be removed
        turn_speed = 50
        start_time_s = time.time()
        while True:
            time.sleep(0.05)
            if time.time() > start_time_s + duration_s:
                break
            heading = self.beacon_sensor.get_heading_to_beacon()
            if heading < 0:
                self.drive_system.go(-turn_speed, turn_speed)
            else:
                self.drive_system.go(-turn_speed, turn_speed)

    def drive_to_beacon(self):
        """
        Drives the robot to the beacon sensor.  This method also needs to check if
        the beacon sensor has been enabled.  If it has not been enabled it will
        enable it before it begins.
        """
        if not self.has_been_enabled:
            self.enable()
        forward_speed = 40
        turn_speed = 20
        distance_0_readings = 0
        while True:
            time.sleep(0.05)
            # ---------------------------------------------------------------------
            # TODO: Implement this method.
            # ---------------------------------------------------------------------

            # Solution to be removed
            current_heading, current_distance = self.beacon_sensor.get_heading_and_distance_to_beacon()
            if current_distance == 100:
                print("IR Remote not found")
                self.drive_system.stop()
                # self.drive(-turn_speed, turn_speed)
                continue

            if abs(current_heading) < 2:
                # Close enough of a heading to move forward
                if current_distance > 0:
                    self.drive_system.go(forward_speed, forward_speed)
                elif current_distance <= 2:
                    self.drive_system.stop()
                    distance_0_readings += 1
                    if distance_0_readings > 5:
                        print("I got the beacon")
                        break  # Success!
            else:
                if abs(current_heading) > 15:
                    print("Heading is too far off to fix. ", current_heading)
                    self.drive_system.stop()
                elif current_heading < 0:
                    self.drive_system.go(-turn_speed, turn_speed)
                else:
                    self.drive_system.go(turn_speed, -turn_speed)

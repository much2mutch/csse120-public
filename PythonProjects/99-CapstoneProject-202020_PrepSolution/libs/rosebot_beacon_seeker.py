"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the BeaconSeeker class which is used to track the beacon
(i.e. the remote control).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: Put the name of EACH team member who contributes
#   to this module in the above.

import time
import rosebot_beacon_sensor
import rosebot_drive_system


###############################################################################
#    BeaconSeeker
###############################################################################
class BeaconSeeker(object):
    """
    Methods using the beacon sensor to drive the robot.
    """
    beacon_sensor: rosebot_beacon_sensor.BeaconSensor
    drive_system: rosebot_drive_system.DriveSystem

    def __init__(self, beacon_sensor, drive_system):
        """
        Constructs BeaconSeeker to track beacon.
          :type beacon_sensor: rosebot_beacon_sensor.BeaconSensor
          :type drive_system: rosebot_drive_system.DriveSystem
        """
        # ---------------------------------------------------------------------
        # TODO: With your instructor, implement this method.
        # ---------------------------------------------------------------------
        self.beacon_sensor = beacon_sensor
        self.drive_system = drive_system

    def spin_until_beacon_seen(self, speed, heading_threshold):
        """
        Spins the robot CW (left @ speed, right @ -speed) until the beacon is seen
        with an abs(heading) less than the given heading_threshold.
        Once the beacon heading is within the threshold the drive system should stop.
        :param speed: Motor speed to use 1 to 100
        :type speed: int
        :param heading_threshold: Required threshold for the heading (in degrees)
        :type heading_threshold: float
        """
        self.drive_system.go(speed, -speed)
        while True:
            time.sleep(0.05)
            # ---------------------------------------------------------------------
            # TODO: Implement this method.
            # ---------------------------------------------------------------------

            # Solution to be removed
            heading = self.beacon_sensor.get_heading()
            if abs(heading) < heading_threshold:
                break
        self.drive_system.stop()

    def spin_to_track_beacon(self, speed, duration_s):
        """
        This method should make the robot spin to follow the beacon.  The robot
        will not move forward it will only spin in place to continuously follow
        the beacon left and right.
        After duration_s seconds have passed this method will stop both motors.
    If the beacon is not seen the robot can either sit still or spin, you decide!
        :param speed: Motor speed to use 1 to 100
        :type speed: int
        :param duration_s: How long to continue this action (in seconds)
        :type duration_s: float
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method by making the robot turn left or right
        # as needed.  If the beacon is near the middle (you decide the threshold
        # then don't move left or right, just sit).
        # Hint towards implementing the duration_s requirement...
        # start_time_s = time.time()
        # while True:
        #     time.sleep(0.05)
        #     if time.time() > start_time_s + duration_s:
        #         break
        # ---------------------------------------------------------------------

        # Solution to be removed
        start_time_s = time.time()
        while True:
            time.sleep(0.05)
            if time.time() > start_time_s + duration_s:
                break
            heading = self.beacon_sensor.get_heading()
            if abs(heading) < 3:
                self.drive_system.stop
            elif heading < 0:
                self.drive_system.go(-speed, speed)
            else:
                self.drive_system.go(-speed, speed)

    def drive_to_beacon(self):
        """
        Drives the robot to the beacon sensor.  It will continue to drive to the beacon
        until it is found (distance less than the threshold you think it acceptable).
        All parameters are determined within the method.
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
            # Print things like heading and distance as you develop your algorithm.
            # One potential algorithm is shown below, but feel free to make your own!
            #
            # If the absolute value of the current_heading is less than 2, you are on the right heading.
            #     If the current_distance is 0 return from this function, you have found the beacon!
            #     If the current_distance is greater than 0 drive straight forward (forward_speed, forward_speed)
            # If the absolute value of the current_heading is NOT less than 2 but IS less than 10, you need to spin
            #     If the current_heading is less than 0 turn left (-turn_speed, turn_speed)
            #     If the current_heading is greater than 0 turn right  (turn_speed, -turn_speed)
            # If the absolute value of current_heading is greater than 10 stop and print Heading too far off
            #
            # Using that plan you should find the beacon if the beacon is in range.  If the beacon is not in range your
            # robot should just sit still until the beacon is placed into view.  It is recommended that you always print
            # something each pass through the loop to help you debug what is going on.  Examples:
            #    print("On the right heading. Distance: ", current_distance)
            #    print("Adjusting heading: ", current_heading)
            #    print("Heading is too far off to fix: ", current_heading)
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

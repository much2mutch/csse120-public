"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import time
import rosebot


def main():
    """ Test a robot's color sensor and line following. """
    print()
    print('--------------------------------------------------')
    print('Testing the Color and Infrared sensors of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot = rosebot.RoseBot()

    # -------------------------------------------------------------------------
    # STUDENTS: Do the work in this module as follows.
    #   Otherwise, you will be overwhelmed by the number of tests happening.
    #
    #   For each function that you implement:
    #     1. Locate the statements just below this comment that call TEST functions.
    #     2. UN-comment only one test at a time.
    #     3. Implement that function per its _TODO_.
    #     4. Implement as needed the appropriate class methods
    #     5. When satisfied with your work, move onto the next test,
    #        RE-commenting out the previous test to reduce the testing.
    # -------------------------------------------------------------------------

    # Color Sensor tests
    run_test_display_color_names(robot)
    run_test_drive_until_color(robot)
    run_test_display_reflected_light_readings(robot)
    run_test_line_follower(robot)

    # IR Sensor tests
    run_test_display_ir_proximity_readings(robot)
    run_test_display_until_distance(robot)
    run_test_spin_towards_beacon(robot)
    run_test_drive_towards_beacon(robot)
    run_test_pick_up_beacon(robot)


def run_test_display_color_names(robot):
    """
    Tests the
    """

    """ Test a robot's COLOR SENSOR. """
    print()
    print('--------------------------------------------------')
    print('Testing the  COLOR_SENSOR  of a robot:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Test the  get_reading   and   get_detected_color_name   methods
    # of the  color_sensor  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  GET_READING  and   GET_DETECTED_COLOR_NAME  methods")
    print(" of the  COLOR_SENSOR  of the robot.")
    input("Press the ENTER key when ready to start printing the color sensed.")

    # -------------------------------------------------------------------------
    # TODO: 3. With the robot's color_sensor, repeatedly:
    #    -- Call its   get_reading   method and print the result (an integer)
    #    -- Call its   get_detected_color_name   method
    #         and print the result (a string that is the name of a color)
    #  each time through the loop asking for input,
    #  and stopping when the user enters a string other than the empty string.
    # -------------------------------------------------------------------------


def run_test_drive_until_color(robot):
    """
    Tests the
    """
    print()
    print('--------------------------------------------------')
    print('Testing the  COLOR_SENSOR  of a robot:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # Test the  wait_until_color  method of the  color_sensor  of the robot:
    # -------------------------------------------------------------------------
    print()
    print("Testing the  WAIT_UNTIL_COLOR  method")
    print(" of the  COLOR_SENSOR  of the robot.")
    input("Press the ENTER key when ready to wait until BLACK is sensed.")

    # -------------------------------------------------------------------------
    # TODO: 4. Call the  wait_until_color  method of the   color_sensor
    #  of the robot, checking to be sure that when it senses black
    #  (which you can simulate by lifting the robot) the code continues.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # TODO: 5. Add additional tests as needed to ensure that the
    #  wait_until_color  method works correctly with each of the 7 colors
    #  that it can sense.  Test strings (upper, lower and mixed case)
    #  and numbers for the colors.
    # -------------------------------------------------------------------------


def run_test_display_reflected_light_readings(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)
        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed


def run_test_line_follower(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)
        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed



def run_test_display_ir_proximity_readings(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)
        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed


def run_test_display_until_distance(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)
        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed


def run_test_spin_towards_beacon(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)
        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed


def run_test_drive_towards_beacon(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)

        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed


def run_test_pick_up_beacon(robot):
    """
    Tests the      methods of the   class.
    """
    print('--------------------------------------------------')
    print('Testing the     methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)

        # -------------------------------------------------------------------------
        # TODO: . Call the    method of the      of the robot
        # -------------------------------------------------------------------------

        # Solution to be removed


main()

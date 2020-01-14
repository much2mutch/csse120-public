"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put your name in the above.

import rosebot
import time

def main():
    """ Calls the desired TEST functions. """
    test_digital_io()


def test_digital_io():
    """ Test a robot's Remote Control, brick buttons, and LEDs. """
    print()
    print('--------------------------------------------------')
    print('Testing the  Remote Control, Brick Buttons, and LEDs  of a robot')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.Rosebot() object.
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

    # run_test_leds_on_off(robot)
    # run_test_leds_colors(robot)
    run_test_brick_buttons(robot)
    # run_test_remote_control_with_leds(robot)
    # run_test_remote_control_with_motors(robot)


def run_test_leds_on_off(robot):
    """
    Tests the  turn_on  turn_off    methods of the Leds class.
    """
    print('--------------------------------------------------')
    print('Testing the  turn_on  turn_off    methods of the robot')
    print('--------------------------------------------------')
    while True:
        # -------------------------------------------------------------------------
        # TODO: 3. Call the  turn_on  and  turn_off method of the   leds   of the robot,
        #  so that both LEDs are on for 1 second, then off for 1 second (repeating forever)
        #  In addition to the LEDs print to the console "LEDs On" or "LEDs Off"
        #  just before the LED change line of code (so you can see it and read it)
        # -------------------------------------------------------------------------

        # Solution to be removed
        print("Both LEDs On")
        robot.leds.turn_on()
        time.sleep(1.0)

        print("Both LEDs Off")
        robot.leds.turn_off()
        time.sleep(1.0)


def run_test_leds_colors(robot):
    """
    Tests the  set_color_by_name    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  set_color_by_name   methods of the robot')
    print('--------------------------------------------------')
    while True:
        # -------------------------------------------------------------------------
        # TODO: 3. Call the  set_color_by_name  method of the   leds   of the robot,
        #  so that the color changes through each valid named color.  Instead of using
        #  a 1 second delay between colors, have the user hit the enter key to change
        #  to the next color.  "red", "green", "amber", "off", repeat.
        #
        #
        # -------------------------------------------------------------------------
        colors = ["red", "green", "amber", "off"]
        color_index = 0

        while True:
            robot.leds.set_color_by_name(colors[color_index % len(colors)])
            input("Press the ENTER key to change to the next color.")
            color_index += 1


def run_test_brick_buttons(robot):
    """
    Tests the  set_color_by_name    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  set_color_by_name   methods of the robot')
    print('--------------------------------------------------')
    while True:
        # -------------------------------------------------------------------------
        # TODO: 3. Call the  set_color_by_name  method of the   leds   of the robot,
        #  so that the color changes through each valid named color.  Instead of using
        #  a 1 second delay between colors, have the user hit the enter key to change
        #  to the next color.  "red", "green", "amber", "off", repeat.
        #
        #
        # -------------------------------------------------------------------------
        colors = ["red", "green", "amber", "off"]
        color_index = 0

        while True:
            robot.leds.set_color_by_name(colors[color_index % len(colors)])
            input("Press the ENTER key to change to the next color.")
            color_index += 1





main()

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

    run_test_leds(robot)
    # run_test_brick_buttons(robot)
    # run_test_remote_control_with_leds(robot)
    # run_test_remote_control_with_motors(robot)


def run_test_leds(robot):
    """
    Tests the  calibrate    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  calibrate   methods of the robot')
    print('--------------------------------------------------')
    while True:
        print("Arm speed should be an integer between 1 and 100.")
        arm_speed = int(input("Enter an integer for arm speed: "))
        if arm_speed == 0:
            break
        print()
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 3. Call the  calibrate_arm  method of the   arm_and_claw   of the robot,
        #   sending it the arm_speed.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.calibrate_arm(arm_speed)
        print("Position: ", robot.arm_and_claw.arm_motor.get_position()) # Optional print statement to check value


def run_test_raise_and_lower(robot):
    """
    Tests the  raise   and  lower    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  raise   and  lower   methods of the robot')
    print('--------------------------------------------------')
    while True:
        print("Arm speed should be an integer between 1 and 100.")
        arm_speed = int(input("Enter an integer for arm speed: "))
        if arm_speed == 0:
            break
        print()
        input("Press the ENTER key when ready for the robot to start moving up.")

        # -------------------------------------------------------------------------
        # TODO: 3. Call the  raise_arm  method of the   arm_and_claw   of the robot,
        #   using the input arm_speed.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.raise_arm(arm_speed)

        input("Press the ENTER key when ready for the robot to start moving back down.")

        # -------------------------------------------------------------------------
        # TODO: 3. Call the  lower_arm  method of the   arm_and_claw   of the robot,
        #   using the input arm_speed.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.lower_arm(arm_speed)


def run_test_move_arm_to_position(robot):
    """
    Tests the  move_arm_to_position    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  move_arm_to_position  method of the robot')
    print('--------------------------------------------------')
    while True:
        print("Arm speed should be an integer between 1 and 100.")
        arm_speed = int(input("Enter an integer for arm speed: "))
        if arm_speed == 0:
            break
        print("Enter an integer for the position to which")
        desired_position = int(input("to move the arm (0 to about 5100: "))
        print()
        input("Press the ENTER key when ready for the robot to start moving up.")

        # -------------------------------------------------------------------------
        # TODO: 3. Call the  raise_arm  method of the   arm_and_claw   of the robot,
        #   using the input arm_speed.
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.move_arm_to_position(desired_position)



main()

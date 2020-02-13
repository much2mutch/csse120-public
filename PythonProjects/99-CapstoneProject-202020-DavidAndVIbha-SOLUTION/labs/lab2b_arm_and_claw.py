"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   ArmAndClaw   class.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note that you will use the  rosebot  library (shorthand: rb).
#  Then change this _TODO_ to DONE.
# -----------------------------------------------------------------------------
import libs.rosebot as rb


def main():
    """ Tests the   ArmAndClaw   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  ArmAndClaw  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a RoseBot object, then sends it as an
    #  argument to the TEST functions. In those TEST functions, you will access
    #  the RoseBot object's   arm_and_claw   instance variable to make the
    #  physical Arm (and associated Claw) move.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()

    run_test_calibrate(robot)
    run_test_raise_and_lower(robot)
    run_test_move_arm_to_position(robot)


def run_test_calibrate(robot):
    """
    Tests the   calibrate   method of the   ArmAndClaw   class.
      :type robot: rb.RoseBot
    """
    print()
    print("--------------------------------------------------")
    print("Testing the   calibrate   method")
    print("  of the   ArmAndClaw   class.")
    print("--------------------------------------------------")

    print()
    print("Press the ENTER key when ready for the robot to start moving.")
    print("It should go all the way UP, then all the way DOWN.")
    print("  If it does NOT do that and seems to be stuck,")
    input("  press Control-C to force this test to stop.")
    try:
        # ---------------------------------------------------------------------
        # TODO: 4. Replace the  pass  statement below with a call to
        #  the   calibrate   method on the arm_and_claw of the given RoseBot.
        #  Then print a simple message like "Calibrated!"
        # ---------------------------------------------------------------------
        pass
        # SOLUTION CODE: Delete from the project given to students.
        robot.arm_and_claw.calibrate_arm()
        print()
        print("Calibrated!")

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_raise_and_lower(robot):
    """
    Tests the  raise   and  lower    methods of the ArmAndClaw class.
    """
    print()
    print("------------------------------------------")
    print("Testing the  raise   and  lower   methods")
    print("  of the   ArmAndClaw   class.")
    print("------------------------------------------")
    print()

    try:
        print("Press the ENTER key when ready for the robot")
        print("to go UP all the way.")
        print("  If it does NOT do that and seems to be stuck,")
        input("  press Control-C to force this test to stop.")

        # ---------------------------------------------------------------------
        # TODO: 5. Replace the  pass  statement below with a call to
        #  the   raise_arm   method on the arm_and_claw of the given RoseBot.
        #  Then print a simple message like "Raised!"
        # ---------------------------------------------------------------------
        pass
        # SOLUTION CODE: Delete from the project given to students.
        robot.arm_and_claw.raise_arm()
        print()
        print("Raised!")

        print("Press the ENTER key when ready for the robot")
        print("to go DOWN all the way.")
        print("  If it does NOT do that and seems to be stuck,")
        input("  press Control-C to force this test to stop.")

        # ---------------------------------------------------------------------
        # TODO: 6. Replace the  pass  statement below with a call to
        #  the   lower_arm   method on the arm_and_claw of the given RoseBot.
        #  Then print a simple message like "Lowered!"
        # ---------------------------------------------------------------------
        pass
        # SOLUTION CODE: Delete from the project given to students.
        robot.arm_and_claw.lower_arm()
        print()
        print("Lowered!")

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def run_test_move_arm_to_position(robot):
    """
    Tests the  move_arm_to_position    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  move_arm_to_position  method of the robot')
    print('--------------------------------------------------')

    while True:
        print("Enter an integer for the position to which")
        desired_position = int(input("to move the arm (0 to about 5100): "))
        if desired_position < 0 or desired_position > 5100:
            print("Goodbye")
            break
        print()
        input("Press the ENTER key when ready for the robot to start moving.")

        # -------------------------------------------------------------------------
        # TODO: 8. Call the  move_arm_to_position   of the robot
        # NOTICE: Your move_arm_to_position should notice that the arm has NOT
        # been calibrated and do a calibration.  You don't need to call calibrate
        # from here, your library method should notice the lack of calibration and
        # just do it before the move!
        # -------------------------------------------------------------------------

        # Solution to be removed
        robot.arm_and_claw.move_arm_to_position(desired_position)


main()

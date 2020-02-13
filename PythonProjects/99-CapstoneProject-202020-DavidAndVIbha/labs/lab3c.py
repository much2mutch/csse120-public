"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   RemoteControl   class.

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
import time


def main():
    """ Tests the   RemoteControl   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  RemoteControl  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a RoseBot object, then sends it as an
    #  argument to the TEST functions. In those TEST functions, you will
    #  access the RoseBot object's   remote_control   instance variable to make
    #  the physical Remote Control (little clicker thing) do things.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    robot = rb.RoseBot()
    run_test_remote_control(robot)


def run_test_leds_on_off(robot):
    """
    Tests the  is_pressed  and  wait_until_pressed  methods
    of the RemoteControl class.
      :type robot: rb.RoseBot
    """
    print('--------------------------------------------------')
    print('Testing the  is_pressed  and  wait_until_pressed')
    print('  methods of the RemoteControl class')
    print('--------------------------------------------------')
    while True:
        # -------------------------------------------------------------------------
        # TODO: 3. Call the  set_color  and  turn_off methods on the   leds   of the robot,
        #  so that "both" LEDs are on "red" for 1 second, then off for 1 second (repeating forever)
        #  In addition to the LEDs print to the console "Both LEDs On as Red" or "LEDs Off"
        #  just before the LED change line of code (so you can see it and read it).
        # -------------------------------------------------------------------------
        pass


def run_test_leds_colors(robot):
    """
    Tests the  set_color_by_name    methods of the ArmAndClaw class.
    """
    print('--------------------------------------------------')
    print('Testing the  set_color   methods of the robot')
    print('--------------------------------------------------')
    left_colors = ["red", "green", "amber", "off", "red", "off", "green", "off", "amber", "off"]
    right_colors = ["red", "green", "amber", "off", "off", "red", "off", "green", "off", "amber"]

    # -------------------------------------------------------------------------
    # TODO: 4. Call the  set_color  method of the   leds   of the robot,
    #  so that the color changes through each value in the lists above.
    #  Instead of using a 1 second delay between colors, have the user hit
    #  the enter key to change to the next colors.
    #
    # After the final value in the list, the program should turn off both LEDs and end.
    # Notice that this _TODO_ is not within a while True loop (unlike other parts)
    # -------------------------------------------------------------------------



def run_test_brick_buttons(robot):
    """
    Tests the  brick_buttons    methods of the BrickButton class.
    """
    print('--------------------------------------------------')
    print('Testing the  brick_buttons   methods of the robot')
    print('--------------------------------------------------')
    while True:
        time.sleep(0.05)

        # -------------------------------------------------------------------------
        # TODO: 5. Create a small program that will light the appropriate LEDs
        #   when buttons on the EV3 Brick are pressed:
        #    When up is pressed light both LEDs green
        #    When down is pressed light both LEDs red
        #    When left is pressed light the left LED amber
        #    When right is pressed light the right LED amber
        #    When backspace is pressed break from the loop and end the program
        #    When no button is pressed turn the LEDs off
        #
        #  Note, only 1 button will be pressed at a time.
        # -------------------------------------------------------------------------


def run_test_remote_control(robot):
    """
    Tests the  remote_control    methods of the RemoteControl class.
    """
    print('--------------------------------------------------')
    print('Testing the  remote_control   methods of the robot')
    print('--------------------------------------------------')

    speed = 50
    while True:
        time.sleep(0.05)

        # -------------------------------------------------------------------------
        # TODO: 6. Create a small program that will move the motors of the robot as follows
        #   when buttons on the remote control are pressed:
        #    When channel 1 red up is pressed drive the left motor forward at speed
        #    When channel 1 red down is pressed drive the left motor backwards at -speed
        #         If neither channel 1 red up or red down is pressed the left motor should stop
        #    When channel 1 blue up is pressed drive the right motor forward at speed
        #    When channel 1 blue down is pressed drive the right motor backwards at -speed
        #         If neither channel 1 blue up or blue down is pressed the right motor should stop
        #    When channel 2 red up is pressed raise the arm
        #    When channel 2 red down is pressed lower the arm (note, a calibration is needed first)
        #    When channel 2 blue up is pressed calibrate the arm
        #    When backspace is pressed on the EV3 break from the loop and end the program
        #
        # Note, MULTIPLE buttons may be pressed at the same time in the program.
        # -------------------------------------------------------------------------



main()

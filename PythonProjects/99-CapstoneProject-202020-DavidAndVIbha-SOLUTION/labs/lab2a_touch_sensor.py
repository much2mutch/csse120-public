"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In particular, it tests the   TouchSensor   class.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note below how to write an IMPORT statement
#  that imports a module that is in the  LIBS  sub-folder.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_touch_sensor as touch
import time


def main():
    """ Tests the   TouchSensor   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  TOUCH SENSOR  of a robot")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TODO: 3. The following constructs a   TouchSensor   object,
    #  then sends it as an argument to the TEST functions. In those TEST
    #  functions, you will access the methods of the TouchSensor object.
    #  Change this _TODO_ to DONE after you understand the following code.
    # -------------------------------------------------------------------------
    touch_sensor = touch.TouchSensor(1)

    run_test_get_reading(touch_sensor)
    run_test_is_pressed(touch_sensor)
    run_test_wait_until_pressed(touch_sensor)
    run_test_wait_until_released(touch_sensor)


def run_test_get_reading(touch_sensor):
    """
    Tests the   get_reading   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   get_reading   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Stop this program by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            # -----------------------------------------------------------------
            # TODO: 4. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #    a. Calls the   get_reading   method on the given TouchSensor,
            #         storing the returned value in a variable if you like.
            #    b. Prints that returned value.
            #    c. Sleeps for 0.5 seconds so that you are not overwhelmed
            #         by the output.
            # -----------------------------------------------------------------
            # SOLUTION CODE: Delete from the project given to students.
            print(touch_sensor.get_reading())
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries.  This allows the program to keep running from here.")


def run_test_is_pressed(touch_sensor):
    """
    Tests the   is_pressed   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   is_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Stop this program by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            # -----------------------------------------------------------------
            # TODO: 5. This code is inside a   try ... except  clause so that
            #  when you press  Control-C  to stop the program, it "catches"
            #  that "exception" and allows the program to continue to the
            #  next set of tests.
            #  _
            #  Replace the  pass  statement below with code that:
            #    a. Calls the   is_pressed   method on the given TouchSensor,
            #         storing the returned value in a variable if you like.
            #    b. Prints that returned value.
            #    c. Sleeps for 0.5 seconds so that you are not overwhelmed
            #         by the output.
            # -----------------------------------------------------------------
            # SOLUTION CODE: Delete from the project given to students.
            print(touch_sensor.is_pressed())
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries.  This allows the program to keep running from here.")


def run_test_wait_until_pressed(touch_sensor):
    """
    Tests the   wait_until_pressed   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   wait_until_pressed   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Press the ENTER key when ready to WAIT until the")
    input("Touch Sensor is pressed (and eventually press it!)")
    # -------------------------------------------------------------------------
    # TODO: 6. Call the   wait_until_pressed   method on the given
    #  TouchSensor object. Then print a simple message like "Pressed!"
    # -------------------------------------------------------------------------
    # SOLUTION CODE: Delete from the project given to students.
    touch_sensor.wait_until_pressed()
    print("Pressed!")


def run_test_wait_until_released(touch_sensor):
    """
    Tests the   wait_until_released   method of the   TouchSensor   class.
      :type touch_sensor: touch.TouchSensor
    """
    print("--------------------------------------------------")
    print("Testing the   wait_until_released   method")
    print("  of the   TouchSensor   class.")
    print("--------------------------------------------------")

    print("Press the ENTER key when ready to WAIT until the")
    print("Touch Sensor is RELEASED.  (So press and hold down")
    print("the Touch Sensor, then press the ENTER key.")
    input("Then, when are ready, RELEASE the (and eventually press it!)")
    # -------------------------------------------------------------------------
    # TODO: 7. Call the   wait_until_released   method on the given
    #  TouchSensor object. Then print a simple message like "Released!"
    # -------------------------------------------------------------------------
    # SOLUTION CODE: Delete from the project given to students.
    touch_sensor.wait_until_released()
    print("Released!")

"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This code defines the   DriveSystem   class  that is used to make a robot move.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAME_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note below how to write an IMPORT statement
#  that imports a module that is in the  LIBS  sub-folder.
#  This module uses code that is in the "low-level" api in rosebot_ev3dev_api.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_ev3dev_api as ev3dev
import time
import fancy_printing


###############################################################################
#    DriveSystem
###############################################################################
class DriveSystem(object):
    """
    Controls the robot's motion via methods that include:
      go                         stop
      go_straight_for_seconds    go_straight_for_inches
      spin_in_place_for_seconds  spin_in_place_for_degrees
      turn_for_seconds           turn_for_degrees
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Read and digest the following NOTE:
    #   To "go straight" means that both wheels move at the same speed.
    #     -- Positive speeds should make the robot move forward.
    #     -- Negative speeds should make the robot move backward.
    #   To "spin_in_place" means that the wheels move at speeds X and -X.
    #     -- Positive speeds should make the robot spin clockwise
    #          (i.e., left motor goes at speed X, right motor at speed -X).
    #     -- Negative speeds should make the robot spin counter-clockwise
    #          (i.e., left motor goes at speed -X, right motor at speed X).
    #   To "turn" means that one wheel does NOT move and the other DOES move:
    #     -- Positive speeds should make only the left motor move
    #          (and hence the turn is clockwise).
    #     -- Negative speeds should make only the right motor move
    #          (and hence the turn is counter-clockwise).
    #   All distances (inches or degrees) should be POSITIVE numbers.
    #   The RoseBot's "wheels" have diameter about 1.3 inches.
    #  _
    #  Once you understand the above, change this _TODO_ to DONE.
    # -------------------------------------------------------------------------
    def __init__(self, left_motor_port="B", right_motor_port="C"):
        """
        Constructs two Motor objects (for the left and right wheels), plugged
        into the given ports. Each Motor object must be a "large" motor.

        Stores those Motor objects as:
           self.left_motor
           self.right_motor

        :type  left_motor_port:  str
        :type  right_motor_port: str
          Each port must be "A", "B", "C", or "D" (defaults to "B" and "C").
        """
        # ---------------------------------------------------------------------
        # TODO: 4. Read the following, ASKING QUESTIONS AS NEEDED.
        #  Once you understand the code, change this _TODO_ to DONE.
        # ---------------------------------------------------------------------
        self.left_motor = ev3dev.Motor(port="B", motor_type="large")
        self.right_motor = ev3dev.Motor(port="C", motor_type="large")

    def go(self, left_wheel_speed, right_wheel_speed):
        """
        Makes the left and right wheel motors spin at the given speeds.
          (More accurately, at the given duty-cycle, which is a percent of
          the maximum possible speed given the current battery level.)

        Speeds are expected to be integers between -100 and 100,
          where positive means forward, negative means backward, and zero (0)
          means to coast to a stop (also see the  stop  method below).

        :type  left_wheel_speed:  int
        :type  right_wheel_speed: int
        """
        # ---------------------------------------------------------------------
        # TODO: 5. Implement this method, using code like this:
        #      self.left_motor.YOU_FIGURE_OUT_WHAT_GOES_HERE
        #      self.right_motor.YOU_FIGURE_OUT_WHAT_GOES_HERE
        #  The "dot trick" should make it clear what to put in the YOU_FIGURE...
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        self.left_motor.turn_on(left_wheel_speed)
        self.right_motor.turn_on(speed)

    def stop(self, stop_action="brake"):
        """
        Stops the left and right wheel motors.
          By default uses applies a "brake" in stopping, as opposed to
          setting a speed of 0 which allows the motor to "coast" to a stop.

        :type  stop_action: str
        """
        # ---------------------------------------------------------------------
        # TODO: 6. Implement this method, using code like this:
        #      self.left_motor.YOU_FIGURE_OUT_WHAT_GOES_HERE
        #      self.right_motor.YOU_FIGURE_OUT_WHAT_GOES_HERE
        #  The "dot trick" should make it clear what to put in the YOU_FIGURE...
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        self.left_motor.turn_off(stop_action)
        self.right_motor.turn_off(stop_action)

    def go_straight_for_seconds(self, seconds, speed=50, stop_action="brake"):
        """
        Makes the robot go straight for the given number of seconds at the
        given speed, stopping using the given stop_action.

        Speeds are expected to be integers between -100 and 100,
          where positive means forward and negative means backward.

        Prints an error message (and goes nowhere) if seconds <= 0
          or speed == 0.

        Implemented using the pattern:
          1. Start the wheel-motors moving at the specified speed
               (using the   go   method).
          2. "Sleep" (do nothing else) while the robot is moving, for the
               specified number of seconds (using the  time.sleep   function).
          3. Stop the wheel-motors (using the  stop   method).

        :type  seconds: float | int
        :type  speed:   int
        :type  stop_action: str
        """
        # Error handling:
        if seconds < 0:
            message = ("ERROR: in calling 'go_straight_for_seconds',\n"
                       + "the first argument is the seconds to move.\n"
                       + "It must be a POSITIVE number.\n"
                       + "The actual value for the first argument was:\n"
                       + "   " + str(seconds)
                       + "No movement done!")
            fancy_printing.print_colored(message, color="red")
            return -1

        # Error handling:
        if speed == 0:
            message = ("ERROR: in calling 'go_straight_for_seconds',\n"
                       + "the second argument is the speed at which to move.\n"
                       + "It must be a NON-ZERO number, but in fact was 0.\n"
                       + "No movement done!")
            fancy_printing.print_colored(message, color="red")
            return -1

        # ---------------------------------------------------------------------
        # TODO: 6. Implement this method, using three lines of code like this:
        #    1. Start both wheel-motors moving at the specified speed
        #         (using the   go   method).
        #    2. "Sleep" (do nothing else) while the robot is moving,
        #         for the specified number of seconds,
        #         using the   time.sleep   function.
        #    3.  Stop the wheel-motors (using the  stop   method).
        # ---------------------------------------------------------------------
        # SOLUTION CODE: Delete from the project given to students.
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop(stop_action)

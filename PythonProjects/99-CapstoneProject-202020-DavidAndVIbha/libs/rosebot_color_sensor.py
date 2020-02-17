"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code defines the   ColorSensor   class, for the robot's downward-facing
sensor that repeated shines right, green and blue light and measures the
intensity of the reflections, interpreting those intensities as colors.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: 1. In the above, put the names of EACH team member who contributes
#  (in any way) to this module.

# -----------------------------------------------------------------------------
# TODO: 2. Note that this module uses a library from LIBS:
#  This module uses code that is in the "low-level" api in rosebot_ev3dev_api.
#  Change this _TODO_ to DONE after you have seen how to do it.
# -----------------------------------------------------------------------------
import libs.rosebot_ev3dev_api as ev3dev
import time


###############################################################################
#    ColorSensor
###############################################################################
class ColorSensor(object):
    """
    Methods for the downward-facing ColorSensor on the robot, including:
      get_detected_color_name
      get_detected_color_number
      get_reflected_intensity
         (and OPTIONALLY   wait_until_color  and other methods of your choosing)
    """
    def __init__(self, port=3):
        """
        Constructs the underlying low-level ColorSensor.
          :type port: int
        """
        # ---------------------------------------------------------------------
        # TODO: 3. Read the following, ASKING QUESTIONS AS NEEDED.
        #  Once you understand the code, change this _TODO_ to DONE.
        # ---------------------------------------------------------------------
        self._low_level_color_sensor = ev3dev.ColorSensor(port)

    def get_color_as_name(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a string:
          - No Color, Black, Blue, Green, Yellow, Red, White, Brown
        :rtype: str
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def get_color_as_number(self):
        """
        Returns the color detected by the sensor, as best the sensor can judge
        from shining red, then green, then blue light and measuring the
        intensities returned.  The returned value is a number:
          - 0 (No Color), 1 (Black), 2 (Blue),  3 (Green),
            4 (Yellow),   5 (Red),   6 (White), 7 (Brown)
        :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def get_reflected_light_intensity(self):
        """
        Shines red light and returns the intensity of the reflected light.
        The returned value is from 0 to 100,
        but in practice more like 3 to 90+ in our classroom lighting with our
        downward-facing sensor that is about 0.25 inches from the ground.

          :return: Amount of light reflected
                   0 (no light reflected) to 100 (super bright)
          :rtype: int
        """
        # ---------------------------------------------------------------------
        # TODO: Implement this method.
        # ---------------------------------------------------------------------

    def wait_for_color(self, color):
        """
        Sits in a loop, sleeping 0.05 seconds each time through the loop,
        waiting for the given color (as a string) to be detected.
        The string can be in any case (lower, upper or mixed), e.g. BLaCk,
        but must be a string (NOT a number representing a string).
          :type color: str
        """
        # ---------------------------------------------------------------------
        # TODO: OPTIONALLY, implement this method.
        # ---------------------------------------------------------------------

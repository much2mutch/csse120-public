"""
THROW-AWAY Capstone Project. If you mess up this THROW-AWAY project, no worries.
It lets you practice skills & concepts needed for the REAL Capstone Project.

This module contains code to run on the EV3 robot (NOT on a laptop).
It defines the   RoseBot   class - the top-level class for a Snatch3r robot.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# -----------------------------------------------------------------------------
# NOTE to students:  do this exercise WITH YOUR INSTRUCTOR.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 1.  If you have not already done so, with your instructor,
#  READ and UNDERSTAND the  HowToShareModules.pdf  document in this project.
#    -- If you understand it, change this _TODO_ to DONE.
#    -- Otherwise, ** do NOT modify this module **
#         and get help before continuing.
#  _
#  Throughout this module, ** use the process in  HowToShareModules.pdf. **
#  _
#  In particular, *** only ONE team member should modify this file ***
#  (but TEAM-PROGRAMMING using the same computer).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 2. Change the   PUT_YOUR_NAMES_HERE   above to the names of
#  EACH team member who contributes (in any way) to this module.
#  _
#  REMINDER: Use ONLY ** ONE ** team member's computer to make changes herein.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# TODO: 3. With your instructor, import the modules needed herein:
#     rosebot_drive_system
#     rosebot_arm_and_claw
#     rosebot_touch_sensor
#  Make sure you understand WHY those imports are needed.
#  Make sure you understand that in code that you write elsewhere, you will
#    construct a  RoseBot  object and use that object to access ALL sub-systems.
# -----------------------------------------------------------------------------
# SOLUTION CODE: Delete later.
import rosebot_drive_system
import rosebot_arm_and_claw
import rosebot_touch_sensor


###############################################################################
#    RoseBot.
###############################################################################
class RoseBot(object):
    """ The top-level class for making a robot do things. """
    def __init__(self):
        """
        Constructs instances of each of the sub-systems of a Snatch3r robot
        and sets instance variables to them:
          self.drive_system
          self.arm_and_claw
          self.touch_sensor
        """
        # ---------------------------------------------------------------------
        # TODO: 4. With your instructor, implement this method.
        # ---------------------------------------------------------------------
        # SOLUTION, delete for final version:
        self.drive_system = rosebot_drive_system.DriveSystem("B", "C")
        self.touch_sensor = rosebot_touch_sensor.TouchSensor(1)
        self.arm_and_claw = rosebot_arm_and_claw.ArmAndClaw("A",
                                                            self.touch_sensor)

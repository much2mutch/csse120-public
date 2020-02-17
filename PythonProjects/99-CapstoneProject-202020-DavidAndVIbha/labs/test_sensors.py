"""
Capstone Team Project.  Code to run on a ROBOT (NOT a laptop).

This module is for testing STAND-ALONE code running on the ROBOT
(WITHOUT having LAPTOP GUI code running on the LAPTOP at the same time).
In tests the various SENSORS available to you.

Authors:  Your professors (for the framework).
Winter term, 2019-2020.
"""

###############################################################################
# STUDENTS: This module is ALREADY IMPLEMENTED.
#   RUN it to test the sensors.
#   You may MODIFY or AUGMENT this module as you choose.
###############################################################################

import libs.rosebot as rb
import time


def main():
    """ Tests the   various Sensors   of a Snatch3r robot. """
    print()
    print("--------------------------------------------------")
    print("Testing the  various Sensors  of a robot")
    print("--------------------------------------------------")

    print_color_sensor_readings()
    print_infrared_proximity_readings()
    print_beacon_sensor_readings()


def print_color_sensor_readings():
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("This function displays readings from the downward-facing")
    print("Color Sensor, once per second.")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            print("As name, number, reflectance: {:8} {:1} {:3}".format(
                robot.color_sensor.get_color_as_name(),
                robot.color_sensor.get_color_as_number(),
                robot.color_sensor.get_reflected_intensity()))
            time.sleep(1)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_infrared_proximity_readings():
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("This function displays readings from the forward-facing")
    print("Infrared Proximity Sensor, once per second.")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            print("Distance in inches: {:3}".format(
                robot.color_sensor.get_distance_in_inches()))
            time.sleep(1)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")


def print_beacon_sensor_readings():
    robot = rb.RoseBot()  # Fresh RoseBot so that sensors do not conflict.

    print()
    print("This function displays readings from the Beacon,")
    print("once per second.")
    print("Stop this test by pressing  Control-C  when desired.")
    input("Press the ENTER key when ready to start getting readings.")
    try:
        while True:
            print("Heading, distance: {:3} {:3}".format(
                robot.beacon_sensor.get_heading(),
                robot.beacon_sensor.get_distance()))
            time.sleep(1)

    except KeyboardInterrupt:
        print()
        print("OK, you just did a keyboard interrupt (Control-C).")
        print("No worries. The program will keep running from here.")
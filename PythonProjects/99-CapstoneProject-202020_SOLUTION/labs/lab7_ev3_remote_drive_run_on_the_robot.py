#!/usr/bin/env python3
"""
For the full problem statement and details see the corresponding lab7_pc_remote_drive_run_on_your_computer.py comments.

There are many solutions to this problem.  The easiest solution on the EV3 side is to NOT bother makes a wrapper
class for the robot object.  Since the challenge presented is very direct it's easiest to just use the Snatch3r class
directly as the delegate to the MQTT client.

The code below is all correct.  Only the loop_forever line will fail to compile.  You need to implement that function
in the Snatch3r class in the library (remember the advice from the lecture).  Pick one team member to implement it then
have everyone else Git update.

Once the EV3 code is ready, run it on the EV3 you can work on the PC side code for the MQTT Remote Control.

Authors: David Fisher and PUT_YOUR_NAME_HERE.  January 2017.
"""

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
import mqtt_remote_method_calls as com
import time

def main():
    """ Test a robot's Remote Control, Brick Buttons, and LEDs. """
    print()
    print('--------------------------------------------------')
    print(' Listening for MQTT messages from the PC')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # TODO: 2. Construct a robot, that is, a rosebot.RoseBot() object.
    # -------------------------------------------------------------------------
    robot = rosebot.RoseBot()

    # -------------------------------------------------------------------------
    # TODO: 3. Construct an MQTT client.
    # -------------------------------------------------------------------------
    mqtt_client = com.MqttClient(robot)

    # -------------------------------------------------------------------------
    # TODO: 4. Connect to talk to the laptop
    # -------------------------------------------------------------------------
    # mqtt_client.connect_to_mqtt_to_talk_to_laptop()
    mqtt_client.connect_to_mqtt_to_talk_to_laptop("broker.hivemq.com")  # Off campus use this broker

    while True:
        time.sleep(0.1)
        if robot.should_shutdown:
            break


main()

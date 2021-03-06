"""
Capstone Team Project.  Code to run on the EV3 robot (NOT on a laptop).

This code contains the one and only  MAIN  function for running on the robot.

This code constructs a robot with an associated MQTT object and runs an
infinite loop while listening for messages from the laptop and responding to
them via its "delegate" object.

This code uses what is called "multiple inheritance" to allow the 4 modules
to each have their own "delegate" class in their own modules (and hence
to reduce the likelihood of GIT conflicts).  Your professor will explain
how this fits into your own code when talking about this framework and MQTT.

Authors:  Your professors (for the framework)
    and PUT_YOUR_NAMES_HERE.
Winter term, 2019-2020.
"""
# TODO: 1.  Put the name of EACH team member in the above.

import time

import student1_robot_code
import student2_robot_code
import student3_robot_code
import student4_robot_code

import mqtt_remote_method_calls as mqtt
import rosebot
import set_robot_number


def main():
    """
    This code, which must run on the ROBOT:
      1. Constructs a robot, an MQTT SENDER, and a DELEGATE to respond
           to messages FROM the LAPTOP sent TO the ROBOT via MQTT.
      2. Stays in an infinite loop while a listener (for MQTT messages)
           runs in the background, "delegating" work to the "delegate".
    """
    robot = rosebot.RoseBot()

    delegate = DelegateForRobotCode(robot)
    mqtt_sender = mqtt.MqttClient(delegate)
    delegate.set_mqtt_sender(mqtt_sender)

    number = set_robot_number.get_robot_number()
    mqtt_sender.connect_to_mqtt_to_talk_to_laptop(lego_robot_number=number)

    time.sleep(1)  # To let the connection process complete
    print()
    print("Starting to listen for messages. The delegate responds to them.")
    print()

    # Stay in an infinite loop while the listener (for MQTT messages)
    # runs in the background:
    while True:
        time.sleep(0.01)
        if delegate.is_time_to_quit:
            break


class DelegateForRobotCode(student1_robot_code.MyRobotDelegate,
                           student2_robot_code.MyRobotDelegate,
                           student3_robot_code.MyRobotDelegate,
                           student4_robot_code.MyRobotDelegate):
    def __init__(self, robot):
        super().__init__(robot)

    def set_mqtt_sender(self, mqtt_sender):
        super().set_mqtt_sender(mqtt_sender)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

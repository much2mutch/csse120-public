from robot import motor, msleep, ao


# Put your Botball program below here.  The main function
# (where your program starts) must be called   main.
def main():
    motor(0, 100)
    motor(1, -100)
    msleep(2000)
    ao()
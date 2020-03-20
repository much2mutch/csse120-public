import math
import time

ROOT = None


def msleep(milliseconds):
    start = time.time()
    while True:
        if (time.time() - start) * 1000 >= milliseconds:
            break
    ROOT.update()


def motor(port, power_percent):
    ROBOT.velocity_x = math.cos(ROBOT.heading) * power_percent
    ROBOT.velocity_y = math.sin(ROBOT.heading) * power_percent
    print(ROBOT.velocity_x, ROBOT.velocity_y)


def ao():
    motor(0, 0)
    motor(1, 0)
    motor(2, 0)
    motor(3, 0)


class Robot(object):
    def __init__(self, x=100, y=100, heading=0):
        self.x = x
        self.y = y
        self.heading = heading
        self.velocity_x = 1
        self.velocity_y = 0
        self.board = None
        self.tag = None

    def put_on_board(self, board):
        self.board = board
        self.tag = self.board.create_oval(100, 100, 110, 110, fill="green",
                                          width=3)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def update_on_board(self):
        self.board.coords(self.tag, int(self.x), int(self.y), int(self.x + 10),
                          int(self.y + 10))
        print("update")


ROBOT = Robot()


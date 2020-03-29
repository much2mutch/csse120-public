import tkinter
from tkinter import ttk
import math
import time

# -----------------------------------------------------------------------------
# Put your Botball program below here:
# -----------------------------------------------------------------------------
def run_robot1():
    """ Code that Simulated Robot #1 will run. """
    print("Robot 1 is starting.")
    motor(0, 50)
    msleep(3000)
    motor(0, 0)


# -----------------------------------------------------------------------------
# DO NOT TOUCH ANYTHING BELOW HERE.
# The rest of this module enables the Online Botball Simulator.
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# We need to store the ROOT and ROBOT globally so that when the Botball program
# makes the robot do something, this simulator can intercept that robot command,
# change the status of the robot, and force an update of the Canvas that
# displays the Botball board.
# -----------------------------------------------------------------------------
ROOT = None  # type: tkinter.Tk
ROBOT = None  # type: Robot
LOGGING_LEVEL = 0  # 0 is NO logging, bigger means MORE logging


# -----------------------------------------------------------------------------
# Botball commands, interpreted by the simulator.
# -----------------------------------------------------------------------------
def msleep(milliseconds):
    start = time.time()
    while True:
        elapsed_seconds = time.time() - start
        log("Sleeping. Elapsed time is {}".format(elapsed_seconds), 20)
        if elapsed_seconds * 1000 >= milliseconds:
            break
        ROOT.update()


def motor(port, power_percent):
    ROBOT.velocity_x = math.cos(ROBOT.heading) * power_percent / 100
    ROBOT.velocity_y = math.sin(ROBOT.heading) * power_percent / 100
    log("Velocity: ({}, {})".format(ROBOT.velocity_x, ROBOT.velocity_y),
        log_level=9)


def ao():
    motor(0, 0)
    motor(1, 0)
    motor(2, 0)
    motor(3, 0)


# -----------------------------------------------------------------------------
# The graphical user interface (GUI).
# -----------------------------------------------------------------------------
def run_gui():
    """ Creates the GUI and starts the program running. """
    # Make the root window and put a frame on it.
    root = tkinter.Tk()
    global ROOT
    ROOT = root

    frame = ttk.Frame(root, padding=10)
    control_frame = ttk.Frame(frame, padding=10)
    board_frame = ttk.Frame(frame)

    # The canvas is the game board, on which the robots run.
    board_canvas = tkinter.Canvas(board_frame, width=400, height=400)

    # The user should press the start_button to start the simulation.
    start_button = ttk.Button(control_frame, text="Run my Botball programs")
    start_button["command"] = lambda: gui.run_botball_programs()

    # Default simulation speed.  User can change mid-run if desired.
    message = "Simulation speed (10 to 1000):   "
    simulation_speed_label = ttk.Label(control_frame, text=message)
    simulation_speed_entry = ttk.Entry(control_frame)
    simulation_speed_entry.insert(0, "1000")

    # For non-fatal error messages (e.g. user error).
    messages_label = ttk.Label(control_frame, text="Messages appear here:")

    # Placement of the widgets.
    frame.grid()
    control_frame.grid(row=0, column=0)
    board_frame.grid(row=0, column=1)

    start_button.grid(row=0, column=0)
    simulation_speed_label.grid(row=1, column=0)
    simulation_speed_entry.grid(row=1, column=1)
    ttk.Label(control_frame, text="").grid(row=2)  # Space
    messages_label.grid(row=3)

    board_canvas.grid()

    # Make the robots and the object that holds this GUI.
    # Initialize the board with the robots.
    # Make the Board and Robots from their .ini files.
    board = Board(board_canvas)
    robots = Robot.make_robots(board)

    global ROBOT
    ROBOT = robots[0]
    gui = GUI(robots, root, board, simulation_speed_entry, messages_label)

    # The main loop in which the program sits.
    root.mainloop()


class GUI(object):
    """ Objects in the GUI, bundled into a class for convenience. """
    def __init__(self, robots, root, board, simulation_speed_entry,
                 messages_label):
        """
        :type robots:  [Robot]
        :type root:    tkinter.Tk
        :type board:   Board  # has the Board's canvas
        :type simulation_speed_entry: ttk.Entry
        :type messages_label:    ttk.Label
        """
        self.robots = robots
        self.root = root
        self.board = board
        self.simulation_speed_entry = simulation_speed_entry
        self.messages_label = messages_label

        self.initialize_canvas()

    def initialize_canvas(self):
        """
        Display the Board and Robots on the board_canvas.
           :type board: Board
        """
        # TODO: Put the image of the board onto the board_canvas.
        for robot in self.robots:
            robot.put_on_canvas(self.board.canvas)

    def run_botball_programs(self):
        # Start the simulation running.
        self.root.after(1, lambda: self.run_one_step())

        # Start the robots running their programs.
        for robot in self.robots:
            self.append_message("Robot {} is running".format(robot.number))
            robot.run_program(self.root)

    def run_one_step(self):
        """
        Runs the simulation for one "step" (a few milliseconds).
        Then schedules the next step.
        """
        log("Running. Time is: {}".format(time.time()), log_level=100)
        some_running = False
        for robot in self.robots:
            if robot.is_running:
                some_running = True
                robot.move()
        self.update_board()
        if some_running:
            time_to_wait = self.get_simulation_speed()
            self.root.after(time_to_wait, lambda: self.run_one_step())
        else:
            # TODO: Should use a STATUS message.
            self.append_message("All robot programs have finished.")

    def update_board(self):
        for robot in self.robots:
            if robot.is_running:
                robot.draw()

    def get_simulation_speed(self):
        return self.get_integer(self.simulation_speed_entry)

    def get_integer(self, entry_box, return_value=10):
        """
        Return the value in the given Entry after converting it to an integer.
        If the conversion fails, display an error message
        and return the given return_value.
          :type entry_box:    ttk.Entry
          :type return_value: int
          :rtype:             int
        """
        # TODO: Associate a name with each Entry so that this can display
        #   a more precise error message.
        try:
            integer = int(entry_box.get())
            return integer
        except:
            self.append_message("Bad data in entry box")
            return return_value

    def append_message(self, message, beginning="\n", end=""):
        self.messages_label["text"] += beginning + message + end


# -----------------------------------------------------------------------------
# A simulated Botball board.
# -----------------------------------------------------------------------------
class Board(object):
    def __init__(self, canvas):
        self.canvas = canvas
        # TODO: Read the board characteristics from board.ini


# -----------------------------------------------------------------------------
# A simulated Botball robot.
# -----------------------------------------------------------------------------
class Robot(object):
    number_of_robots = 0

    @staticmethod
    def make_robots(board):
        """
        Construct and return the robots per the robots.ini file.
        :type board: Board
        """
        # TODO: Implement this.
        return [Robot(board)]

    def __init__(self, board):
        self.board = board
        self.number = Robot.number_of_robots + 1  # 1-based, not 0-based
        Robot.number_of_robots += 1
        self.is_running = True  # FIXME: Confusion re ready to run vs running

        # TODO: Read data from .ini file
        self.x = 100
        self.y = 100
        self.heading = 0

        self.width = 50
        self.height = 20
        self.color = "green"
        self.line_width = 3
        self.robot_image = self.get_robot_image()
        self.tag = None  # Set by put_on_canvas

        self.velocity_x = 1
        self.velocity_y = 0

    def get_robot_image(self):
        return self.x, self.y, self.x + self.width, self.y + self.height

    def put_on_canvas(self, canvas):
        # TODO: Get data from robots.ini
        self.tag = self.board.canvas.create_rectangle(self.get_robot_image(),
                                                      fill=self.color,
                                                      width=self.line_width)

    def move(self):
        log("Moving robot #{} by ({}, {})".format(self.number,
                                                  self.velocity_x,
                                                  self.velocity_y),
            log_level=10)
        self.x += self.velocity_x
        self.y += self.velocity_y

    def draw(self):
        log("Drawing robot #{}".format(self.number), log_level=20)
        self.board.canvas.coords(self.tag, self.get_robot_image())

    def run_program(self, root):
        log("Program for robot {} starts.".format(self.number))
        try:
            self.is_running = True
            function_to_run = "run_robot{}".format(self.number)
            end_status = globals()[function_to_run]()
            self.is_running = False
            log("Program for robot {} ends with status {}.".format(self.number,
                                                                   end_status))
        except:
            # Exit the program if error occurs while running a Botball program.
            root.destroy()
            raise


def log(*args, log_level=1):
    """
    Prints the given string if LOGGING_LEVEL >= specified log_level,
    else does nothing.
      :type log_level: int
    """
    if LOGGING_LEVEL >= log_level:
        print(*args)


run_gui()
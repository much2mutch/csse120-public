import tkinter
from tkinter import ttk


def gui_main():
  """ Creates the GUI and starts the program running. """
  # Make the root window and put a frame on it.
  root = tkinter.Tk()
  frame = ttk.Frame(root)
  control_frame = ttk.Frame(frame)
  board_frame = ttk.Frame(frame)

  # The canvas is the game board, on which the robots run.
  board = tkinter.Canvas(board_frame, width=400, height=400)

  # The user should press the start_button to start the simulation.
  start_button = ttk.Button(control_frame, text="Run my Botball program")
  start_button["command"] = lambda: \
      run_botball_program(root)

  # Default simulation speed.  User can change mid-run if desired.
  simulation_speed_entry = ttk.Entry(frame)
  simulation_speed_entry.insert(0, "1000")

  # For non-fatal error messages (e.g. user error).
  message = "Error messages appear here:\n\n\n"
  error_label = ttk.Label(control_frame, text=message)

  # Placement of the widgets.
  frame.grid()
  control_frame.grid(row=0, column=0)
  board_frame.grid(row=0, column=1)

  start_button.grid()
  simulation_speed_entry.grid()
  error_label.grid()

  board.grid()

  # Will run the simulation (i.e., advance the robots)
  # every few milliseconds.
  robots = []
  root.after(1, lambda: simulate_one_step(root, board, simulation_speed_entry,
                                          error_label, robots))

  # The main loop in which the program sits.
  root.mainloop()


def run_botball_program(root):
  try:
      robot_1_program.main()
  except:
      # Exit the program if an error occurs while running the Botball program.
      root.destroy()
      raise

def simulate_one_step(root, board, simulation_speed_entry, error_label, robots):
  """
  Runs the simulation for one "step" (a few milliseconds).
  Then schedules the next step.
   :type root:                   tkinter.Tk
   :type board:                  tkinter.Canvas
   :type simulation_speed_entry: ttk.Entry
   :type error_label:            ttk.Label
   :type robots: [Robot]
  """
  # Update the robot's position.
  # Redraw the screen.
  print("Run one step.")
  for robot in robots:
      robot.update_position()
  update_board(board, robots)
  root.update()

  simulation_speed = get_integer_from_entry(simulation_speed_entry,
                                            error_label)
  root.after(simulation_speed,
             lambda: simulate_one_step(root, board, simulation_speed_entry,
                                       error_label, robots))

def update_board(board, robots):
  pass

def get_integer_from_entry(entry_box, error_label, default_return=10):
  # Get the value from the given Entry box and convert it to an integer.
  # Fail gracefully if an Exception occurs.
  try:
      integer = int(entry_box.get())
      return integer
  except:
      error_label["text"] = "Bad data in entry box"
      return default_return

gui_main()
"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Derek Whitley, their colleagues, and PUT_YOUR_NAME_HERE.
"""
###############################################################################
# TODO: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   Define a complete program that:
#     a.  Imports  rosegraphics
#     b.  Defines a   main   function that:
#          - Constructs a TurtleWindow.
#          - Calls the function that YOU define (see next bullet, below) TWICE
#              (with different arguments each time) to TEST your function.
#          - Asks the TurtleWindow to wait for a mouse click, then close.
#     c.  Defines another function that takes three parameters:
#             a SimpleTurtle, a string that represents a color,
#             and an integer for the distance to move (in pixels),
#         and causes the SimpleTurtle to:
#           - Move backward the given distance.
#           - Change its Pen's color to the given color.
#           - Turn left 90 degrees.
#           - Move forward twice the given distance.
#     d.  Calls main.
###############################################################################

import rosegraphics as rg

def t_move(turtle, color, dist):
    turt = rg.SimpleTurtle(turtle)
    turt.backward(dist)
    turt.pen = rg.Pen(color, 3)
    turt.left(90)
    turt.forward(dist*2)



def main():
    window = rg.TurtleWindow()

    t_move("classic", "blue", 40)
    t_move("turtle", "red", 100)

    window.close_on_mouse_click()

main()
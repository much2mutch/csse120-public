"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Derek Whitley, their colleagues, and Seth Mutchler.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

import rosegraphics as rg

###############################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#  +
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#  _
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#  _
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#  _
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import math



square_turtle = rg.SimpleTurtle("turtle")
square_turtle.pen = rg.Pen("lightblue", 2)
square_turtle.speed = 100

octagon_turtle = rg.SimpleTurtle("turtle")
octagon_turtle.pen = rg.Pen("DarkGoldenrod2", 2)
octagon_turtle.speed = 100

c_turtle = rg.SimpleTurtle("turtle")
c_turtle.pen = rg.Pen("firebrick", 2)
c_turtle.speed = 100

size = 5

window = rg.TurtleWindow()
window.tracer(200)

for k in range(1000):
    square_turtle.draw_square(size)
    square_turtle.pen_up()
    square_turtle.left(45+(k**2))
    square_turtle.forward(7)
    square_turtle.right(45+k)
    square_turtle.pen_down()

    octagon_turtle.draw_regular_polygon(8, size)
    octagon_turtle.pen_up()
    octagon_turtle.left(45+2*k)
    octagon_turtle.forward(5)
    octagon_turtle.right(45+2*k)
    octagon_turtle.pen_down()

    c_turtle.draw_circle(size)
    c_turtle.pen_up()
    c_turtle.left(45+k)
    c_turtle.forward(5)
    c_turtle.right(45+k)
    c_turtle.pen_down()

    size = size + (k * 2)

window.close_on_mouse_click()


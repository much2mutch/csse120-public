"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python. 
  
Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Derek Whitley, their colleagues, and Seth Mutchler.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

# -----------------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# -----------------------------------------------------------------------------

##############################################################################
# DONE: 2. Read the following, then change its _TODO_ to DONE.
#   Throughout these exercises, you must use  RANGE  statements.
#   At this point of the course, you are restricted to the SINGLE-ARGUMENT
#   form of RANGE statements, like this:
#         range(blah):
#   There is a MULTIPLE-ARGUMENT form of RANGE statements (e.g. range(a, b))
#   but you are NOT permitted to use the MULTIPLE-ARGUMENT form yet, for
#   pedagogical reasons.  Change the above _TODO_ to DONE after reading this.
###############################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    # run_test_draw_squares_from_circle()
    # run_test_draw_circles_from_rectangle()
    run_test_draw_lines_from_rectangles()


def run_test_draw_squares_from_circle():
    """ Tests the   draw_squares_from_circle  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_squares_from_circle  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # TWO tests on ONE window.
    # -------------------------------------------------------------------------
    title = "Tests 1 and 2 of DRAW_SQUARES_FROM_CIRCLE: "
    title = title + " 7 little squares from green circle, 4 big squares"
    window1 = rg.RoseWindow(650, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(100, 100), 20)
    circle.fill_color = "green"
    draw_squares_from_circle(7, circle, window1)

    # Test 2:
    circle = rg.Circle(rg.Point(350, 70), 50)
    draw_squares_from_circle(4, circle, window1)
    window1.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # A third test on ANOTHER window.
    # -------------------------------------------------------------------------
    title = "Test 3 of DRAW_SQUARES_FROM_CIRCLE: "
    title += " 20 teeny squares from blue circle!"
    window2 = rg.RoseWindow(525, 300, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 50), 10)
    circle.fill_color = "blue"
    draw_squares_from_circle(20, circle, window2)

    window2.close_on_mouse_click()


def draw_squares_from_circle(n, circle, window):
    circle.attach_to(window)
    radius = circle.radius
    diameter = radius * 2
    x = circle.center.x
    y = circle.center.y

    for _ in range (n):
        rg.Square(rg.Point(x,y),diameter).attach_to(window)
        x = x + radius
        y = y + radius

    window.render()

    """
    What comes in:  Three arguments:
      -- A positive integer n.
      -- An rg.Circle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   3_draw_squares_from_circle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Circle on the given rg.RoseWindow.
      Then draws  n  rg.Squares on the given rg.RoseWindow, such that:
        -- The first rg.Square circumscribes the given rg.Circle.
        -- Each subsequent rg.Square has its upper-left quarter
             on top of the lower-right quarter of the previous rg.Square,
             so that the squares form an overlapping sequence
             that goes down and to the right.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n:      int
      :type circle: rg.Circle
      :type window: rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #      as in   draw_row_of_circles   in m1e,
    #      instead of directly using the loop variable.
    #  ########################################################################
    #  HINT: To figure out the code that computes the necessary
    #        positions of each square,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    #  ########################################################################
    # -------------------------------------------------------------------------


def run_test_draw_circles_from_rectangle():
    """ Tests the   draw_circles_from_rectangle  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_circles_from_rectangle  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # -------------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  draw_circles_from_rectangle  function
    #   defined below.  Include at least **   3   ** tests, of which
    #      ***  at least TWO tests are on ONE window and
    #      ***  at least ONE test is on a DIFFERENT window.
    #  ########################################################################
    #  HINT: Consider using the same test cases as suggested by the
    #    pictures in  4_draw_circles_from_rectangle.pdf   in this project.
    #    Follow the same form as the example in a previous problem.
    #  ########################################################################
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # TWO tests on ONE window.
    # -------------------------------------------------------------------------
    title = "Tests 1 and 2 of DRAW_CIRCLES_FROM_RECTANGLE: "
    title = title + " 4 green-filled circles, 5 black-outlined circles"
    title = title + " and 8 blue-filled circles, 3 red-outlined circles"
    window1 = rg.RoseWindow(720, 500, title)

    # Test 1:
    rectangle = rg.Rectangle(rg.Point(400, 250),rg.Point(440, 325))
    rectangle.fill_color = "green"
    rectangle.outline_color = "black"
    rectangle.outline_thickness = 5
    draw_circles_from_rectangle(4,5,rectangle,window1)

    # Test 2:
    rectangle = rg.Rectangle(rg.Point(600, 400),rg.Point(500, 450))
    rectangle.fill_color = "blue"
    rectangle.outline_color = "red"
    rectangle.outline_thickness = 3
    draw_circles_from_rectangle(8,3,rectangle,window1)

    window1.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # A third test on ANOTHER window.
    # -------------------------------------------------------------------------
    title = "Test 3 of DRAW_CIRCLES_FROM_RECTANGLE: "
    title = title + " 6 yellow-filled circles and 10-brown outlined circles"
    window2 = rg.RoseWindow(620, 380, title)

    # Test 3:
    rectangle = rg.Rectangle(rg.Point(375, 330),rg.Point(350, 280))
    rectangle.fill_color = "yellow"
    rectangle.outline_color = "brown"
    rectangle.outline_thickness = 5
    draw_circles_from_rectangle(6,10,rectangle,window2)

    window2.close_on_mouse_click()


def draw_circles_from_rectangle(m, n, rectangle, window):
    # draw rectangle
    rectangle.attach_to(window)

    # rectangle variables
    height = rectangle.get_height()
    width = rectangle.get_width()
    rectangle_center = rectangle.get_center()

    # circle variables
    diameter1 = height
    radius1 = diameter1 / 2
    diameter2 = width
    radius2 = diameter2 / 2

    # color variables
    fill_color = rectangle.fill_color
    outline_color = rectangle.outline_color

    # setting circle center
    circle_center_x = rectangle_center.x - (width/2) - radius1
    circle_center_y = rectangle_center.y
    circle_center = rg.Point(circle_center_x,circle_center_y)

    # initial circle
    circle = rg.Circle(circle_center, radius1)
    circle.fill_color = fill_color
    circle.attach_to(window)

    for _ in range (m-1):
        circle_center_x = circle_center_x - diameter1
        circle = rg.Circle(rg.Point(circle_center_x, circle_center_y), radius1)
        circle.fill_color = fill_color
        circle.attach_to(window)

    # circle center
    circle_center_x = rectangle_center.x
    circle_center_y = rectangle_center.y - (height / 2) - radius2
    circle_center = rg.Point(circle_center_x, circle_center_y)

    # initial circle
    circle = rg.Circle(circle_center, radius2)
    circle.outline_color = outline_color
    circle.attach_to(window)

    for _ in range (n-1):
        circle_center_y = circle_center_y - diameter2
        circle = rg.Circle(rg.Point(circle_center_x, circle_center_y), radius2)
        circle.outline_color = outline_color
        circle.attach_to(window)

    window.render()

    """
    What comes in:  Four arguments:
      -- Positive integers m and n.
      -- An rg.Rectangle.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   4_draw_circles_from_rectangle.pdf   in this project for pictures
        that may help you better understand the following specification:

      First draws the given rg.Rectangle on the given rg.RoseWindow.
      Then draws  m  rg.Circles on the given rg.RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the height
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately to the left of the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately to the left
             of the previous rg.Circle, so that the circles form a row
             that goes to the left.
        -- Each rg. Circle has the same fill_color as the given
             rg.Rectangle (and has no outline_color).
      Then draws  n  rg.Circles on the given RoseWindow, such that:
        -- The diameter of each rg.Circle is the same as the width
             of the given rg.Rectangle.
        -- The first rg.Circle is immediately above the
             given rg.Rectangle
        -- Each subsequent rg.Circle is immediately above the previous
             rg.Circle, so that the circles form a column that goes up.
        -- Each rg.Circle has the same outline_color as the given
             rg.Rectangle (and has no fill_color).
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type m:         int
      :type n:         int
      :type rectangle: rg.Rectangle
      :type window:    rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #      as in   draw_row_of_circles   in m1e,
    #      instead of directly using the loop variable.
    #  ########################################################################
    #  HINT: To figure out the code that computes the necessary
    #        positions of each circle,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    #  ########################################################################
    # -------------------------------------------------------------------------


def run_test_draw_lines_from_rectangles():
    """ Tests the   draw_lines_from_rectangles  function. """
    print()
    print("--------------------------------------------------")
    print("Testing the  draw_lines_from_rectangles  function:")
    print("  See the graphics windows that pop up.")
    print("--------------------------------------------------")

    # TWO tests on ONE window.
    title = "Tests 1 & 2 of DRAW_LINES_FROM_RECTANGLES:"
    title += "  5 lines, 8 lines!"
    window1 = rg.RoseWindow(900, 400, title)

    rectangle1 = rg.Rectangle(rg.Point(100, 25), rg.Point(150, 125))
    rectangle2 = rg.Rectangle(rg.Point(300, 150), rg.Point(400, 175))
    rectangle1.outline_color = "red"
    rectangle2.outline_color = "blue"
    draw_lines_from_rectangles(rectangle1, rectangle2, 5, window1)

    rectangle1 = rg.Rectangle(rg.Point(870, 30), rg.Point(750, 100))
    rectangle2 = rg.Rectangle(rg.Point(700, 90), rg.Point(650, 60))
    rectangle2.outline_color = "green"
    draw_lines_from_rectangles(rectangle1, rectangle2, 8, window1)

    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = "Test 3 of DRAW_LINES_FROM_RECTANGLES:  11 lines!"
    window2 = rg.RoseWindow(700, 700, title)

    rectangle1 = rg.Rectangle(rg.Point(550, 200), rg.Point(650, 100))
    rectangle2 = rg.Rectangle(rg.Point(600, 50), rg.Point(650, 75))
    rectangle1.outline_color = "brown"
    rectangle2.outline_color = "cyan"
    rectangle2.outline_thickness = 10
    draw_lines_from_rectangles(rectangle1, rectangle2, 11, window2)

    window2.close_on_mouse_click()


def draw_lines_from_rectangles(rectangle1, rectangle2, n, window):
    # draw both rectangles
    rectangle1.attach_to(window)
    rectangle2.attach_to(window)

    # define attributes of rectangles
    r1_center = rectangle1.get_center() # rect. 1 center
    r2_center = rectangle2.get_center() # rect. 2 center
    r1_h = rectangle1.get_height()      # rect. 1 height
    r1_w = rectangle1.get_width()       # rect. 1 width
    r1_color = rectangle1.outline_color # rect. 1 outline color
    r2_color = rectangle2.outline_color # rect. 2 outline color

    # define starting attributes of points
    p1x = r1_center.x                   # point 1 starting x
    p1y = r1_center.y                   # point 1 starting y
    p2x = r2_center.x                   # point 2 starting x
    p2y = r2_center.y                   # point 2 starting y

    # draw line 1
    line = rg.Line(rg.Point(p1x,p1y),rg.Point(p2x,p2y))
    line.thickness = 5
    line.color = r1_color
    color = line.color
    line.attach_to(window)
    # print(rg.Point(p1x,p1y))
    # print("starting color is",line.color)
    # print("r1 color is",r1_color)

    # loop
    for _ in range (n-1):

        # point 1
        p1x = p1x - (r1_w / 2)
        p1y = p1y + (r1_h / 2)
        point1 = rg.Point(p1x,p1y)
        # print("p1 = ",point1)

        # point 2
        p2x = p2x - (r1_w / 2)
        p2y = p2y + (r1_h / 2)
        point2 = rg.Point(p2x,p2y)
        # print("p2 = ",point2)

        # create line
        line = rg.Line(point1,point2)

        # thickness
        line.thickness = 5

        # color
        if color == r1_color:
            # print("line color is r1; switching to r2")
            color = r2_color
        else:
            # print("line color is r2; switching to r1")
            color = r1_color
        line.color = color

        # attach to window
        line.attach_to(window)

    # render final drawing
    # print("rendering")
    window.render()

    """
    What comes in:  Four arguments:
      -- Two rg.Rectangles.
      -- A positive integer n.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   5_draw_lines_from_rectangles.pdf   in this project
      for pictures that may help you better understand
      the following specification:

      First draws the given rg.Rectangles on the given rg.RoseWindow.
      Then draws  n  rg.Lines on the given rg.RoseWindow, such that:
        -- The 1st rg.Line goes from the center of one of the
             1st rg.Rectangle to the center of the 2nd rg.Rectangle.
        -- The 2nd rg.Line goes from the lower-left corner of the
              1st rg.Rectangle and is parallel to the 1st rg.Line,
              with the same length and direction as the 1st rg.Line.
        -- Subsequent rg.Lines are shifted from the previous rg.Line in
              the same way that the 2nd rg.Line is shifted from the 1st.
        -- Each of the rg.Lines has thickness 5.
        -- The colors of the rg.Lines alternate, as follows:
             - The 1st, 3rd, 5th, ... rg.Line has color R1_color
             - The 2nd, 4th, 6th, ... rg.Line has color R2_color
            where
             - R1_color is the outline color of the 1st rg.Rectangle
             - R2_color is the outline color of the 2nd rg.Rectangle
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type rectangle1: rg.Rectangle
      :type rectangle2: rg.Rectangle
      :type n:          int
      :type window:     rg.RoseWindow
      """
    # -------------------------------------------------------------------------
    # TODO: 6. Implement and test this function.
    #          Tests have been written for you (above).
    #  _
    #  CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #      as in   draw_row_of_circles   in m1e,
    #      instead of directly using the loop variable.
    #  ########################################################################
    #  HINT: To figure out the code that computes the necessary
    #        endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    #  ########################################################################
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

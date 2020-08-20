"""
This project lets you practice NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and Seth Mutchler.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, "Upside-down wall, Tests 1 and 2")

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """

    original = rectangle.clone()
    x = rectangle.get_width()
    y = rectangle.get_height()
    c1 = rectangle.corner_1
    c2 = rectangle.corner_2

    for j in range(n):
        fill = 'blue'
        for k in range(n-j):
            new_rect = rg.Rectangle(c1,c2)
            new_rect.fill_color = fill
            new_rect.attach_to(window)
            c1.move_by(x/2,-y)
            c2.move_by(x/2,-y)
        c1 = original.corner_1.clone()
        c2 = original.corner_2.clone()
        fill = 'red'
        # print("orig c1 is ",original.corner_1)
        for l in range(j):
            c1.move_by((x/2),y)
            c2.move_by((x/2),y)


    window.render()








    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()

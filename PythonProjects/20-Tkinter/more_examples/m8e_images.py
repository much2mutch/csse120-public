"""
Example showing for tkinter and ttk how to:
  -- Read an IMAGE from a FILE (jpeg, png, gif, ...)
  -- Resize that image
  -- Put the image on a Button, Canvas, ...

Note: This example requires that you install the PILLOW library.
If you have not already done so, install PILLOW like this:
   File ~ Settings
   Expand Project, then select Python Interpreter
   On the right-hand-side, find and select the little  +   sign
      (you may have to make the window wider to see it)
   In the dialog that pops up, type    pillow   and select it,
     make the  Install to user's site-packages ...   checkbox be UN-checked,
     then press the Install Package button.
     (If the install fails, try again with that checkbox checked.)

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


def main():
    # The usual tkinter.Tk, ttk.Frame, and also a tkinter.Canvas.
    root = tkinter.Tk()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    canvas = tkinter.Canvas(main_frame, width=500, height=300)
    canvas.grid()

    # The next line assumes that the file named   queen_of_hearts.jpeg  is in
    # the current folder.  Change the name/pathname as needed for your files.
    image = Image.open("queen_of_hearts.jpeg")  # Can be jpeg, png, ...

    # The following line is not necessary, it just shows the image size et al.
    print(image.format, image.size, image.mode)

    # Resize the image to 400 wide by 200 tall (stretching the image),
    # and also to 1/3 of its current size:
    image1 = image.resize((400, 200))  # Will stretch the image
    image2 = image.resize((image.size[0] // 3, image.size[1] // 3))

    # The following makes tkinter images from the Pillow images.
    # Use tkinter images in all your  tkinter/ttk  code.
    tk_image1 = ImageTk.PhotoImage(image1)
    tk_image2 = ImageTk.PhotoImage(image2)
    tk_image3 = ImageTk.PhotoImage(image)  # Fromi the un-resized image.

    # Put the tkinter images onto a Canvas (twice) and a Button, where the
    # coordinates on the Canvas are for the CENTER of the image (by default):
    canvas.create_image(200, 150, image=tk_image1)
    canvas.create_image(400, 75, image=tk_image2)

    button1 = ttk.Button(main_frame, image=tk_image3)
    button1.grid()
    button1['command'] = lambda: print('hello')

    root.mainloop()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

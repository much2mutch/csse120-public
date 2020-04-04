"""
Example showing a "kitchen sink" of tkinter/ttk widgets.

Do NOT use the CODE herein as an example -- it is TERRIBLE code
spliced together from the INDIVIDUAL examples in this project.

Look at those INDIVIDUAL examples for CODE to use as examples.

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""

import tkinter
from tkinter import ttk
import time


def main():
    # Root (main) window
    root = tkinter.Tk()
    root.title("A kitchen sink of ttk/Tkinter widgets")

    # Menu
    make_menu(root)

    # Frame and sub-frames
    frame = ttk.Frame(root, padding=20)
    frame1 = ttk.Frame(frame, padding=20, relief="raised")
    frame2 = ttk.Frame(frame, padding=20, relief="groove")

    frame.grid()
    frame1.grid()
    frame2.grid()

    # Key binding
    windows = []
    number = 1
    root.bind_all("<Key-Up>", lambda event: pop_up(windows, number))

    # Labels
    message = ""
    message = message + "This shows a 'kitchen sink' of tkinter/ttk widgets.\n"
    message = message + " Try its various buttons et al to experience them.\n\n"
    message = message + "      Do NOT use this CODE as an example;\n"
    message = message + "             it has TERRIBLE style.\n"
    message = message + "      Instead, look at the CODE in the\n"
    message = message + "     INDIVIDUAL examples in this project."
    label = ttk.Label(frame1, text=message)
    label.grid(row=0, column=0, columnspan=2)

    text = "Press the UP ARROW key \n   to get a new window"
    label = ttk.Label(frame1, text=text)
    label.grid(row=0, column=2)

    show_data_label = ttk.Label(frame1, text="")
    show_data_label.grid(row=1, column=2)

    message = ""
    message = message + " Type something in the Entry box.\n"
    message = message + "Then press the APPEND DATA button."
    label = ttk.Label(frame1, text=message)
    label.grid(row=1, column=0)
    # Entry box
    entries = []
    entry_box = ttk.Entry(frame1)
    entry_box.grid(row=1, column=1)

    # Buttons
    open_canvas_button = ttk.Button(frame1, text="Open a canvas for drawing")
    open_canvas_button["command"] = lambda: make_canvas()
    open_canvas_button.grid(row=2, column=0)

    more_data_button = ttk.Button(frame1, text="Append data from Entry Box")
    more_data_button["command"] = lambda: append_data(entry_box,
                                                      show_data_label)
    more_data_button.grid(row=2, column=1)

    quit_button = ttk.Button(frame1, text="Quit")
    quit_button["command"] = lambda: root.destroy()
    quit_button.grid(row=2, column=2)

    # Checkboxes and radiobuttons
    make_checkbox_and_radiobuttons(frame2)
    root.mainloop()


def make_menu(root):
    # The default is for menus to be "tear-off" -- they can be dragged
    # off the menubar.  Use whichever style best suits your GUI.
    root.option_add("*tearOff", False)

    # Step 1:  Make the menu bar
    menubar = tkinter.Menu(root)
    root["menu"] = menubar

    # Step 2:  Make the pull-down menu's on the menu bar.
    choose_demo = tkinter.Menu(menubar)
    menubar.add_cascade(menu=choose_demo, label="Choose what to demo")

    # Step 3:  Make menu items for each menu on the menu bar.
    # Bind callbacks using lambda, as we have seen elsewhere,
    # but this time with a    command=...   optional argument supplied.
    choose_demo.add_command(label="Canvas to draw things",
                            command=lambda: make_canvas())
    choose_demo.add_command(label="Show an image",
                            command=lambda: show_image(tkinter.Toplevel()))
    choose_demo.add_command(label="Show events and binding",
                            command=lambda: show_events())


class PenData(object):
    def __init__(self):
        self.color = 'blue'
        self.mouse_position_x = None
        self.mouse_position_y = None
        self.is_dragging = False


def make_canvas():
    pen_data = PenData()

    window = tkinter.Toplevel()
    main_frame = ttk.Frame(window, padding=5)
    main_frame.grid()

    instructions = 'Click the left mouse button to make circles,\n'
    instructions = instructions + 'drag the left mouse button to draw'
    label = ttk.Label(main_frame, text=instructions)
    label.grid()

    # Make a tkinter.Canvas on a Frame.
    # Note that Canvas is a tkinter (NOT a ttk) class.
    canvas = tkinter.Canvas(main_frame, background='lightgray')
    canvas.grid()

    # Make callbacks for mouse events.
    canvas.bind('<Button-1>', lambda event: left_mouse_click(event))
    canvas.bind('<B1-Motion>',
                lambda event: left_mouse_drag(event, pen_data))
    canvas.bind('<B1-ButtonRelease>',
                lambda event: left_mouse_release(pen_data))  # @UnusedVariable

    # Make a button to change the color.
    button = ttk.Button(main_frame, text='Flip pen color')
    button.grid()
    button['command'] = lambda: flip_pen_color(pen_data)


def left_mouse_click(event):
    canvas = event.widget
    canvas.create_oval(event.x - 10, event.y - 10,
                       event.x + 10, event.y + 10,
                       fill='green', width=3)


def left_mouse_drag(event, data):
    # data.mouse_position_x and _y keep track of the PREVIOUS mouse
    # position while we are dragging.
    canvas = event.widget
    if data.is_dragging:
        canvas.create_line(data.mouse_position_x, data.mouse_position_y,
                           event.x, event.y,
                           fill=data.color, width=5)
    else:
        data.is_dragging = True  # Start dragging

    data.mouse_position_x = event.x
    data.mouse_position_y = event.y


def left_mouse_release(data):
    data.is_dragging = False


def flip_pen_color(data):
    if data.color == 'blue':
        data.color = 'red'
    else:
        data.color = 'blue'


def pop_up(windows, number):
    """ Pops up a window, with a Label that shows some info. """
    window = tkinter.Toplevel()  # Note Toplevel, NOT Tk.
    windows.append(window)

    label = ttk.Label(window, text="Window #{}".format(number))
    label.grid()

    add_window_button = ttk.Button(window, text="Add another window")
    add_window_button["command"] = lambda: pop_up(windows, number + 1)
    add_window_button.grid()

    close_windows_button = ttk.Button(window, text="Close all these windows")
    close_windows_button["command"] = lambda: destroy_windows(windows)
    close_windows_button.grid()


def destroy_windows(windows):
    """ Destroys all the given windows. """
    for window in windows:
        window.destroy()


def make_checkbox_and_radiobuttons(frame):
    # Checkbutton's and Radiobutton's have their own labels.
    checkbutton = ttk.Checkbutton(frame, text='Robots rule!')

    # Radiobutton's. We often put them onto a sub-frame,
    # to group them visually.  The 'value' identifies which is selected.
    radio_frame = ttk.Frame(frame, borderwidth=10, relief='groove')
    radio1 = ttk.Radiobutton(radio_frame, text='Peter Pevensie',
                             value='peter')
    radio2 = ttk.Radiobutton(radio_frame, text='Susan Pevensie',
                             value='susan')
    radio3 = ttk.Radiobutton(radio_frame, text='Edmund Pevensie',
                             value='edmund')
    radio4 = ttk.Radiobutton(radio_frame, text='Lucy Pevensie',
                             value='lucy')

    # This Button will show how it can interact with other widgets.
    button = ttk.Button(frame, text='Reset the other widgets')

    # Checkbutton's and Radiobutton's can have an "observer" variable
    # that is bound to the state of the Checkbutton / Radiobutton.
    checkbutton_observer = tkinter.StringVar()
    checkbutton['variable'] = checkbutton_observer

    radio_observer = tkinter.StringVar()
    for radio in [radio1, radio2, radio3, radio4]:
        radio['variable'] = radio_observer  # They all need the SAME observer

    # Bind callbacks using 'command' and lambda, as we have seen elsewhere.
    checkbutton['command'] = lambda: checkbutton_changed(checkbutton_observer)

    for radio in [radio1, radio2, radio3, radio4]:
        radio['command'] = lambda: radiobutton_changed(radio_observer)

    button['command'] = lambda: button_pressed(checkbutton_observer,
                                               radio_observer)

    # Layout the widgets (here, in a row with padding between them).
    # You can see more on layout in a subsequent example.
    c = 0
    for widget in [checkbutton, radio_frame, button]:
        widget.grid(row=0, column=c, padx=20)
        c = c + 1

    for radio in [radio1, radio2, radio3, radio4]:
        radio.grid(sticky='w')


def checkbutton_changed(checkbutton_observer):
    print('The checkbutton changed to', checkbutton_observer.get())


def radiobutton_changed(radiobutton_observer):
    print('The radiobutton changed to', radiobutton_observer.get())


def button_pressed(checkbutton_observer, radiobutton_observer):
    print('After 2 seconds, I will toggle the Checkbutton')
    print('and reset the radiobutton to Peter\'s.')
    time.sleep(2)

    if checkbutton_observer.get() == '1':
        checkbutton_observer.set('0')
    else:
        checkbutton_observer.set('1')

    radiobutton_observer.set('peter')


def show_image(window):
    photo = tkinter.PhotoImage(file="tkinter_mqtt_ev3.gif")

    label = ttk.Label(window, image=photo)
    label.image = photo
    label.grid()


def append_data(entry_box, label):
    data = entry_box.get()
    label["text"] = label["text"] + "\n" + data


class Data(object):
    def __init__(self):
        self.number = 0
        self.entry_box1 = None
        self.entry_box2 = None
        self.number_label = None


def show_events():
    data = Data()

    root = tkinter.Toplevel()

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    intro = 'This example shows how keys can be associated\n' \
            + 'with widgets.  The widget must have the "focus"\n' \
            + 'for its event to fire.\n\n' \
            + 'In this example, the <Return> (Enter key) event\n' \
            + 'is associated with each of the 2 Entry boxes,\n' \
            + 'and the u and d keys and mouse press are associated\n' \
            + 'with the button.\n\n' \
            + 'Try the u and d keys, with and without the button having\n' \
            + 'the focus.  Try entering numbers in the Entry boxes\n' \
            + 'with and without pressing the Enter key.\n'
    intro_label = ttk.Label(main_frame, text=intro)
    intro_label.grid()

    number_text = 'The number is {}'.format(data.number)
    number_label = ttk.Label(main_frame, text=number_text)
    number_label.grid()
    data.number_label = number_label

    # --------------------------------------------------------------------
    # In the previous module, you saw   bind_all   which binds the Event
    # to ALL the widgets on the root.  If you want the callback to occur
    # only when a certain Widget has the "focus" (and the Event occurs),
    # use   bind   (not bind_all), per the following examples:
    # --------------------------------------------------------------------

    entry1 = ttk.Entry(main_frame, width=4)
    entry1.grid()
    entry1.bind('<Return>', lambda event: callback1(event, data))
    data.entry_box1 = entry1

    entry2 = ttk.Entry(main_frame, width=4)
    entry2.grid()
    entry2.bind('<Return>', lambda event: callback2(event, data))
    data.entry_box2 = entry2

    # --------------------------------------------------------------------
    # You can bind Events to Buttons (and any other Widget).  So the
    # first   button.bind   below shows an alternative to ['command'].
    # --------------------------------------------------------------------

    button_text = 'Use the TAB key to give me the "focus",'
    button_text = button_text + '\n then press the u or d key'
    button = ttk.Button(main_frame, text=button_text)
    button.grid()

    button.bind('<Button-1>', lambda event: callback3(event, data))
    button.bind('<Key-u>', lambda event: callback3(event, data))
    button.bind('<Key-d>', lambda event: callback3(event, data))

    root.mainloop()


def callback1(event, data):
    """
    Increases the number in the given Data object by the value
    of the Entry box bound to the given Event.
    """
    widget = event.widget
    number_in_entry_box = int(widget.get())
    print('This is callback1, which uses Widget: ' + str(widget))
    data.number = data.number + number_in_entry_box

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


def callback2(event, data):
    """
    Decreases the number in the given Data object by the value
    of the Entry box bound to the given Event.
    """
    widget = event.widget
    number_in_entry_box = int(widget.get())
    print('This is callback2, which uses Widget: ' + str(widget))
    data.number = data.number - number_in_entry_box

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)


def callback3(event, data):
    """
    Increments or decrements the number in the given Data object
    depending on the given Event.
    """
    print('hello')
    if event.type == '2':  # 2 is the KEY type in Windows, it seems
        if event.keysym == 'u':
            print('u key was pressed while the button had focus')
            data.number = data.number + 1
        elif event.keysym == 'd':
            print('d key was pressed while the button had focus')
            data.number = data.number - 1
        else:
            print('Unexpected - key ' + event.keysym + ' was pressed.')
    elif event.type == '4':  # 4 is the BUTTON type in Windows, it seems
        print('button was pressed')
        data.number = data.number + 1  # So mouse press is same as u key.
    else:
        print('Unexpected - event type ' + event.type + ' occurred.')

    print('  The number is now ' + str(data.number))
    data.number_label['text'] = 'The number is {}'.format(data.number)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

"""
tkinter
GUI (Graphical User Interface)

Life cycle:
1- import tkinter
2- Main Window (entry point)
3- Widgets .....
4- Mainloop (to keep the app alive)

https://docs.python.org/3/library/tkinter.html
"""

import tkinter as tk

# main window
m = tk.Tk()


#
 # WIDGETS -> Controls (Buttons, Text, Label, Frame ...)
#





# last line -> mainloop
m.mainloop()


"""
Widget Placement:

1- pack() -> puts the widgets one after another (top to bottom or from left to right)
2- grid() -> puts the widgets in a grid (row, column base)
3- place() -> puts widget in exact location on the window (x=100, y=300 text unit)

"""
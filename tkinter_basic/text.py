# import
import tkinter as tk
from tkinter import Text

# Text: multi line text input (text box)

# main window
window = tk.Tk()
window.title('Tkinter Basics - Text')
window.geometry('600x400')  # width x height


# Text Widget (Text Area)
txt = Text(window, height=5, width=40)


# place the widget
txt.pack()

# last line -> mainloop
window.mainloop()

# import
import tkinter as tk
from tkinter import Frame, Button

# Frame: container that holds other widgets

# main window
window = tk.Tk()
window.title('Tkinter Basics - Frame')
window.geometry('600x400')  # width x height


# Frame Widget
frame = Frame(window)

# Buttons
btnLeft = Button(master=frame, text='Frame Button Left', bg='black', fg='white')
btnLeft.pack(side=tk.LEFT)

btnRight = Button(master=frame, text='Frame Button Right', bg='black', fg='white')
btnRight.pack(side=tk.RIGHT)

# place the widgets
frame.pack()

# last line -> mainloop
window.mainloop()

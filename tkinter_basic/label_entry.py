# import
import tkinter as tk
from tkinter import Label, Entry

# Label -> read only text on screen
# Entry -> one line text box

# main window
window = tk.Tk()
window.title('Tkinter Basics - Label - Entry')
window.geometry('600x400')  # width x height


# Label Widgets
lblName = Label(master=window, text='Name')
lblLastName = Label(window, text='Last Name')

# Entry Widgets
entName = Entry(window)
entLastName = Entry(window)


# place the label - entry
lblName.grid(row=0, column=0)
entName.grid(row=0, column=1)

lblLastName.grid(row=1)
entLastName.grid(row=1, column=1)


# last line -> mainloop
window.mainloop()

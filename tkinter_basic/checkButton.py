# import
import tkinter as tk

# main window
window = tk.Tk()
window.title('Tkinter Basics - CheckButton')
window.geometry('600x400')  # width x height


# CheckButton widget
chkBtn_1 = tk.Checkbutton(master=window, text='Correct')
chkBtn_2 = tk.Checkbutton(master=window, text='Incorrect')


# place the check button
chkBtn_1.grid(row=0, column=0)
chkBtn_2.grid(row=1, column=0)

# last line -> mainloop
window.mainloop()

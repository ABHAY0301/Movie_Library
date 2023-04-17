# import
import tkinter as tk

# main window
window = tk.Tk()
window.title('Tkinter Basics - Button')
window.geometry('600x400')  # width x height


# Button Widget
btn = tk.Button(master=window,
                text='Close',
                width=45,  # text-unit -> width (width of one char of text)
                height=10,  # height (height of one char of text)
                bg='orange',
                fg='blue',
                command=window.destroy  # what to do when clicked
                )

# place the button
btn.pack()

# last line -> mainloop
window.mainloop()













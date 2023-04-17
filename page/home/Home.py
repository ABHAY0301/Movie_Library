import tkinter as tk
from PIL import Image, ImageTk

from data.colors import COLORS

class Home:
    """It creates the Home Page."""

    def __init__(self, window, bg_color, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='home',
            relief=relief,
            bg=bg_color
        )
        self.side = side
        self.bg_color = bg_color
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        course = tk.Label(self.frame,
                          text='Capstone Project - Movie Library with Tkinter',
                          font=('Helvetica', 18, 'bold'),
                          fg=COLORS.BLACK,
                          bg=self.bg_color)
        course.place(x=135, y=40)

        instructor = tk.Label(self.frame,
                              text='(Abhay Soni)',
                              font=('Helvetica', 18, 'bold'),
                              fg=COLORS.BLACK,
                              bg=self.bg_color)
        instructor.place(x=630, y=640)

        self.render_image()

    def render_image(self):
        load = Image.open('images/home/python_logo.png')
        render = ImageTk.PhotoImage(load)
        img_lb = tk.Label(self.frame, image=render, bg=self.bg_color)
        img_lb.image = render
        img_lb.place(x=130, y=100)
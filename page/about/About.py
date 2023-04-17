import tkinter as tk
from PIL import Image, ImageTk

from data.colors import COLORS

class About:
    """It creates the About Page."""

    def __init__(self, window, bg_color, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='about',
            relief=relief,
            bg=bg_color
        )
        self.side = side
        self.bg_color = bg_color
        self.description()
        self.add_frame()

    def add_frame(self):
        self.add_page_title('                                            About                                            ')
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def add_page_title(self, title):
        lbl = tk.Label(self.frame, text=title, height=3,
                       bg=COLORS.BLACK, fg=COLORS.WHITE, font=('Arial', 12, 'bold'))
        lbl.grid(row=0, column=0, columnspan=8, padx=190, pady=(0, 8), sticky='we')  #we means west east


    def description(self):
        course = tk.Label(self.frame,
                          text="I have developed a movie library project using Python and Tkinter that displays the\n"
                               "top 245 movies from IMDB.This project involved web scraping and GUI development,\n"
                               "using Tkinter, requests, and  BeautifulSoup modules. Utilized web scraping to extract\n"
                               "movie titles and ratings, and used Tkinter to create an interactive GUI that displays\n"
                               "the data.\n\n\n"
                               "This project allowed me to gain experience in web scraping, data visualization, and\n"
                               "GUI development using Python and Tkinter. It also showcased my ability to work with\n "
                               "third-party modules and libraries to create useful and interactive applications.\n",
                          font=('Arial', 15),
                          fg=COLORS.BLACK,
                          bg=self.bg_color)
        course.place(x=20, y=120)

        instructor = tk.Label(self.frame,
                              text='(Abhay Soni)',
                              font=('Helvetica', 18, 'bold'),
                              fg=COLORS.BLACK,
                              bg=self.bg_color)
        instructor.place(x=630, y=630)

import tkinter as tk
from data.colors import COLORS

from page import Home, MovieList, MovieDetail, About

class RightFrame:
    """It will hold the pages on the right frame."""

    # class attribute
    bg_color = COLORS.ORANGE

    def __init__(self, window, name, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name=name,
            relief=relief,
            bg=RightFrame.bg_color
        )
        self.side = side
        self.add_frame()

    def add_frame(self):
        # frame content
        self.frame_content()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self, page_name='home'):
        try:
            incoming_frame = self.frame
        except:
            incoming_frame = self
        finally:
            if page_name == 'home':
                # add home page
                Home(incoming_frame, RightFrame.bg_color)
            elif page_name == 'movieList':
                # add movie list page
                MovieList(incoming_frame, RightFrame.bg_color)
            elif page_name == 'movieDetail':
                # add movie detail page
                MovieDetail(incoming_frame, RightFrame.bg_color)
            elif page_name == 'about':
                # add movie detail page
                About(incoming_frame, RightFrame.bg_color)


    # static method -> Class Method (no self parameter)
    def destroy_children(frame):
        # destroy the children
        for child in frame.winfo_children():
            child.destroy()

"""
This is the main file of Movie Library:
Pages:
    1- Home
    2- Movie List
    3- Movie Detail

https://www.imdb.com/chart/top/
"""

from widgets import Window, LeftFrame , RightFrame

if __name__ == '__main__':

    # Root Window
    root = Window('Movie Library')

    # LEFT FRAME
    left_frame = LeftFrame(root.window, 'leftFrame')
    #
    # RIGHT FRAME
    right_frame = RightFrame(root.window, 'rightFrame')

    # start root window -> mainloop()
    root.start_method()


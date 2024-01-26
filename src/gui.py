import tkinter as tk
from tkinter import filedialog, Canvas, Button, Frame, Tk, Entry
from header import Header
from draw_pad import DrawPad


class gui:
    def __init__(self):
        root = Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.title("Handwriting Recognition")
        #root.geometry(str(screen_width) + "x" + str(screen_height))
        #root.resizable(width=False, height=False)
        self.upper_frame = Frame(root, width=screen_width, height=screen_height)
        self.header = Header(self.upper_frame, screen_width, screen_height)
        self.upper_frame.grid(row=0, column=0)
        self.lower_frame = Frame(root, width=screen_width, height=screen_height)
        self.lower_frame.grid(row=1, column=0)
        self.draw_pad = DrawPad(root, screen_width/2, screen_height/2)
        root.mainloop()
gui()
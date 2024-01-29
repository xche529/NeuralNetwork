import tkinter as tk
from tkinter import filedialog, Canvas, Button, Frame, Tk, Entry
from header import Header
from draw_pad import DrawPad
from result_display_board import ResultDisplayBoard
from number_reader import NumberReader

class gui:
    def __init__(self):
        self.number_reader = NumberReader()
        self.root = Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.title("Handwriting Recognition")
        #root.geometry(str(screen_width) + "x" + str(screen_height))
        #root.resizable(width=False, height=False)
        self.upper_frame = Frame(self.root, width=screen_width, height=screen_height)
        self.upper_frame.grid(row=0, column=0)
        self.lower_frame = Frame(self.root, width=screen_width, height=screen_height)
        self.lower_frame.grid(row=1, column=0)
        self.lower_left_frame = Frame(self.lower_frame, width=screen_width/2, height=screen_height/2)
        self.lower_left_frame.grid(row=0, column=0)
        self.lower_right_frame = Frame(self.lower_frame, width=screen_width/2, height=screen_height/2)
        self.lower_right_frame.grid(row=0, column=1)
        self.draw_pad = DrawPad(self.lower_left_frame, screen_width/2, screen_height/2)
        self.header = Header(self.upper_frame, screen_width, screen_height, self.recognize, self.draw_pad.clear, self.number_reader.read_weights,self.draw_pad.update_line_width)

        self.result_display_board = ResultDisplayBoard(self.lower_right_frame, screen_width/2, screen_height/2, [0.1,0.2,0.3,0.4])
        self.root.mainloop()
        
    def recognize(self):
        pixels = self.draw_pad.extract_pixels()
        for i in range(len(pixels)):
            pixels[i] = 255 - pixels[i]
        result_list = self.number_reader.read(pixels)
        print(result_list)
        self.result_display_board.refresh(result_list)
gui()
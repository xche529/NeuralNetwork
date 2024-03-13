import tkinter as tk
from tkinter import Canvas, filedialog, Tk, Button,Entry,Frame
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt
import numpy
from draw_pad import DrawPad


class train_gui:
    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.draw_pad = DrawPad(master, width/2, height/2)

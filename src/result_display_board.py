
import tkinter as tk
from tkinter import Canvas, filedialog, Tk, Button,Entry,Frame
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt
import numpy

class ResultDisplayBoard:
    def __init__(self, master, width, height,result_list):
        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE,font=('Arial', 20), width=int(width/50), height=int(height/30))
        self.result_label = tk.Label(master, text='', font=('Arial', 20), width=10, height=2)
        self.listbox.grid(row=0, column=0)
        self.result_label.grid(row=0, column=1)
        
    def refresh(self,result_list):
        self.listbox.delete(0, tk.END)
        for i in range(len(result_list)):
            self.listbox.insert(tk.END, str(i) + ': ' + str(round(result_list[i][0]*100,3))+ '%')
        result = numpy.argmax(result_list)
        self.result_label['text'] = result
        self.result_label.update()



import tkinter as tk
from tkinter import Canvas, filedialog, Tk, Button,Entry,Frame
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt
import numpy

class ResultDisplayBoard:
    def __init__(self, master, width, height,result_list):
        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE)
        for i in range(len(result_list)):
            if isinstance(result_list[i], list):
                value = result_list[i][0]  # 如果是列表，取第一个元素
            else:
                value = result_list[i]
            self.listbox.insert(tk.END, str(i) + ': ' + str(value * 100)+ '%')
        result = numpy.argmax(result_list)
        self.result_label = tk.Label(master, text=result)
        self.listbox.grid(row=0, column=0)
        self.result_label.grid(row=0, column=1)
        
    def refresh(self,result_list):
        self.listbox.delete(0, tk.END)
        for i in range(len(result_list)):
            self.listbox.insert(tk.END, str(i) + ': ' + str(result_list[i])+ '%')
        result = numpy.argmax(result_list)
        self.result_label['text'] = result
        self.result_label.update()


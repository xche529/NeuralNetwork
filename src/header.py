import tkinter as tk
from tkinter import Canvas, filedialog, Tk, Button,Entry,Frame
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt

class Header:
    def __init__(self, master, width, height, Recognize, Clear, ReadWeights, UpdateWidth):
        self.scale = tk.Scale(master, from_=1, to=20, orient="horizontal", command=UpdateWidth)
        self.clear_button = Button(master, text="clear", command=(Clear))
        self.license_file_entry = Entry(master,width=30)
        self.choose_file_button = Button(master, text="Load Weights File:", command=lambda: self.open_file_dialog([("json", "*.json"), ("All files", "*.*")],ReadWeights))
        self.clear_button.grid(row=0, column=4,padx=10)
        self.scale.grid(row=0, column=3,padx=10)
        self.label = tk.Label(master, text="Line Width:")
        self.label.grid(row=0, column=2,padx=10)
        self.license_file_entry.grid(row=0, column=1,padx=10)
        self.choose_file_button.grid(row=0, column=0,padx=10)
        self.recognize_button = Button(master, text="Recognize", command=(Recognize))
        self.recognize_button.grid(row=0, column=5,padx=10)

    def open_file_dialog(self, file_types, ReadWeights):
        file_path = filedialog.askopenfilename(title = "choose weights file", filetypes = file_types)
        self.license_file_entry.delete(0, tk.END)  
        self.license_file_entry.insert(tk.END, file_path) 
        ReadWeights(file_path)
        return file_path
    

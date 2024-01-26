import tkinter as tk
from tkinter import Canvas, filedialog, Tk, Button,Entry,Frame
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt

class Header:
    def __init__(self, master, width, height):
        self.increase_line_width_button = Button(master, text="increase line width", command=())
        self.decrease_line_width_button = Button(master, text="decrease line width", command=())
        self.clear_button = Button(master, text="clear", command=())
        self.license_file_entry = Entry(master,width=30)
        self.choose_file_button = Button(master, text="Choose File", command=lambda: self.open_file_dialog([("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")]))
        self.clear_button.grid(row=0, column=4,padx=10)
        self.increase_line_width_button.grid(row=0, column=3,padx=10)
        self.decrease_line_width_button.grid(row=0, column=2,padx=10)
        self.license_file_entry.grid(row=0, column=1,padx=10)
        self.choose_file_button.grid(row=0, column=0,padx=10)
    
    def open_file_dialog(self, file_types, ):
        file_path = filedialog.askopenfilename(title = "选择文件", filetypes = file_types)
        self.license_file_entry.delete(0, tk.END)  
        self.license_file_entry.insert(tk.END, file_path) 
        return file_path
    

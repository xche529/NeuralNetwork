import tkinter as tk
from tkinter import Canvas, filedialog, Tk
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt

class DrawPad:
    def __init__(self, master, width, height):
        self.width = int(width*3/4)
        self.height = int(height*3/4)
        self.master = master
        self.canvas = Canvas(master, width=self.width, height=self.height, bg="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.old_coords = None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.release)
        self.transparent_image = tk.PhotoImage(width=self.width, height=self.height)
        self.canvas.create_image((0, 0), image=self.transparent_image, anchor="nw", state="normal")


    def paint(self, event):
        print(event.x, event.y)
        x1, y1 = (event.x), (event.y)
        if self.canvas.old_coords:
            x2, y2 = self.canvas.old_coords
            self.canvas.create_line(x1, y1, x2, y2, width=7, fill="black")
        self.canvas.old_coords = x1, y1

    def release(self, event):
        self.canvas.old_coords = None
        
    def clear(self):
        self.canvas.delete("all")

    def extract_pixels(self):
        img = Image.new("RGB", (self.width, self.height), color="white")
        draw = ImageDraw.Draw(img)
        items = self.canvas.find_all()
        for item in items:
            if self.canvas.type(item) == "line":
                coords = self.canvas.coords(item)
                line_width = 3
                item_config = self.canvas.itemconfig(item)
                line_width = int(float(item_config["width"][-1])) 
                draw.line(coords, fill="black", width=int(line_width))
        img = img.convert('L')
        resized_image = img.resize((28, 28))
        pixels = list(resized_image.getdata())
        self.display_image(pixels)
        return pixels

    def display_image(self, pixels):
        if hasattr(self, "label"):
            self.label.destroy()
        img = Image.new("L", (28, 28), color='white')
        img.putdata(pixels)
        img = img.resize((self.width, self.height))
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(self.master, image=img_tk)
        label.image = img_tk
        self.label = label
        label.grid(row=1, column=0)

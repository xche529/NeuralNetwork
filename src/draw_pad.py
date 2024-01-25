import tkinter as tk
from tkinter import Canvas, filedialog, Tk
from PIL import Image, ImageDraw,ImageTk
import matplotlib.pyplot as pImageTklt

class DrawPad:
    def __init__(self, master, width, height):
        self.width = int(width)
        self.height = int(height)
        self.master = master
        self.canvas = Canvas(master, width=int(width), height=int(height), bg="white")
        self.canvas.pack()
        self.canvas.old_coords = None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.release)
        self.transparent_image = tk.PhotoImage(width=int(width), height=int(height))
        self.canvas.create_image((0, 0), image=self.transparent_image, anchor="nw", state="normal")


    def paint(self, event):
        print(event.x, event.y)
        x1, y1 = (event.x), (event.y)
        if self.canvas.old_coords:
            x2, y2 = self.canvas.old_coords
            self.canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
        self.canvas.old_coords = x1, y1

    def release(self, event):
        self.canvas.old_coords = None

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
        pixels = list(img.getdata())
        return pixels

    def display_image(self, pixels):
        if hasattr(self, "label"):
            self.label.destroy()
        img = Image.new("RGB", (self.width, self.height), color="white")
        img.putdata(pixels)
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(self.master, image=img_tk)
        label.image = img_tk
        self.label = label
        self.label.pack()


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Draw Pad")

draw_pad = DrawPad(root, screen_width/2, screen_height/2)

button = tk.Button(root, text="Test", command=lambda: draw_pad.display_image(draw_pad.extract_pixels()))
button.pack()
root.mainloop()

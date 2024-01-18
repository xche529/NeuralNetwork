from tkinter import*

class draw_pad:
    def __init__(self, master, width, height):
        self.master = master
        self.canvas = Canvas(master, width=width, height=height, bg="white")
        self.canvas.pack()
        self.canvas.old_coords = None
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.release)


    def paint(self, event):
        print(event.x, event.y)
        x1, y1 = (event.x), (event.y)
        if self.canvas.old_coords:
            x2, y2 = self.canvas.old_coords
            self.canvas.create_line(x1, y1, x2, y2)
        self.canvas.old_coords = x1, y1

    def release(self, event):
        self.canvas.old_coords = None






root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Draw Pad")

root.geometry("%dx%d" % (screen_width/2, screen_height/2))

draw_frame = Frame(root)
draw_frame.pack()

draw_pad = draw_pad(draw_frame, screen_width/2, screen_height/2)
root.mainloop()

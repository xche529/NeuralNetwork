import tkinter as tk
from tkinter import filedialog, Canvas, Button, Frame, Tk, Entry

class DrawPad:
    def __init__(self, master, width, height):
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
            self.canvas.create_line(x1, y1, x2, y2, width=3, fill="black")
        self.canvas.old_coords = x1, y1

    def release(self, event):
        self.canvas.old_coords = None


class TestBoard:
    def __init__(self, master, width, height):
        self.button = Button(master, text="Test", command=())
        self.license_file_entry = Entry(root,width=30)
        self.choose_file_button = Button(root, text="Choose File", command=lambda: self.open_file_dialog(self.license_file_entry,[("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")],))
        self.button.grid(row=0, column=0)
        self.license_file_entry.grid(row=1, column=0)
        self.choose_file_button.grid(row=2, column=0)
    
    def open_file_dialog(entry_widget, file_types, ):
        file_path = filedialog.askopenfilename(title = "选择文件", filetypes = file_types)
        entry_widget.delete(0, tk.END)  
        entry_widget.insert(tk.END, file_path) 
        return file_path



root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Draw Pad")


draw_frame = Frame(root)
test_frame = Frame(root)    
draw_frame.grid(row=0, column=0)
test_frame.grid(row=0, column=1)

draw_pad = DrawPad(draw_frame, screen_width/2, screen_height/2)
test_board = TestBoard(test_frame, screen_width/2, screen_height/2)
root.mainloop()

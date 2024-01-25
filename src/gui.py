import tkinter as tk
from tkinter import filedialog, Canvas, Button, Frame, Tk, Entry



class TestBoard:
    def __init__(self, master, width, height):
        self.button = Button(master, text="Test", command=())
        self.license_file_entry = Entry(root,width=30)
        self.choose_file_button = Button(root, text="Choose File", command=lambda: self.open_file_dialog([("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")]))
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

test_board = TestBoard(test_frame, screen_width/2, screen_height/2)
root.mainloop()

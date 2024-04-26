import tkinter as tk
from tkinter import messagebox
import pyperclip
import os

def start_drag(event):
    # This function will copy the file path to the clipboard
    # Note: This does not implement actual drag-and-drop to other applications,
    # but simulates dragging by using the clipboard.
    file_path = "test_fst.fst"  # Replace with your file path
    if os.path.exists(file_path):
        pyperclip.copy(file_path)
        messagebox.showinfo("Drag Started", "File path copied to clipboard!\nYou can paste it in the target application.")
    else:
        messagebox.showerror("Error", "File does not exist.")

def create_app():
    root = tk.Tk()
    root.title("Draggable File Button")

    # Create a button that starts the drag
    btn_drag_file = tk.Button(root, text="Drag Me", padx=10, pady=5)
    btn_drag_file.pack(pady=20)

    # Bind the button event
    btn_drag_file.bind("<Button1-Motion>", start_drag)

    root.mainloop()

create_app()


### DOESNT WORK SO Well
# might need to translate my program into pyqt5

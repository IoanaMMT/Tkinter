import tkinter as tk
from tkinter import ttk

root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text = "User Name: ")
name_label.pack(side = "left")
name_entry = ttk.Entry(root, width = 15, textvariable = user_name)
name_entry.pack(side = "left")
name_entry.focus()

def to_print():
	print(f"Hello, {user_name.get() or 'World'}")

green_button = ttk.Button(root, text = "Print", command = to_print)
green_button.pack(side = "left")

quit_button = ttk.Button(root, text = "Quit", command = root.destroy)
quit_button.pack(side = "right")


root.mainloop()
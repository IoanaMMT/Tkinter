import tkinter as tk
from tkinter import ttk

root = tk.Tk()

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding = (20, 10, 20, 0))
input_frame.pack(fill = "both")

name_label = ttk.Label(input_frame, text = "User Name: ")
name_label.pack(side = "left")
name_entry = ttk.Entry(input_frame, width = 15, textvariable = user_name)
name_entry.pack(side = "left")
name_entry.focus()

buttons = ttk.Frame(root, padding = (20, 10))
buttons.pack(fill = "both")


def to_print():
	print(f"Hello, {user_name.get() or 'World'}")

green_button = ttk.Button(buttons, text = "Print", command = to_print)
green_button.pack(side = "left", fill = "x", expand = True)

quit_button = ttk.Button(buttons, text = "Quit", command = root.destroy)
quit_button.pack(side = "right", fill = "x", expand = True)


root.mainloop()
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable = selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Friday")
weekday["state"] = "readonly"
weekday.pack()

def handle_selection(event):
	print("Today is ", selected_weekday.get())
	print("But we are going to change it to Friday")
	#selected_weekday.set()
	print(weekday.current())

weekday.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()

print(selected_weekday.get(), "was selected.")
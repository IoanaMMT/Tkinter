import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

langs = tk.StringVar(value = programming_languages)
langs_select = tk.Listbox(root, listvariable = langs, height = 6)
langs_select["selectmode"] = "extended" #browse
langs_select.pack()

def handle_selection_change(event):
	selected_indices = langs_select.curselection()
	for i in selected_indices:
		print(langs_select.get(i))

langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()
####### Combobox ########
'''selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable = selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Friday")
weekday["state"] = "readonly" #normal
weekday.pack()

def handle_selection(event):
	print("Today is ", selected_weekday.get())
	print("But we are going to change it to Friday")
	#selected_weekday.set()
	print(weekday.current())

weekday.bind("<<ComboboxSelected>>", handle_selection)

root.mainloop()

print(selected_weekday.get(), "was selected.")
'''
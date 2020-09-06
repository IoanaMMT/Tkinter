import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = tk.Frame(root)
main.pack(side = "left", fill = "both", expand = True)

second = tk.Frame(root)
second.pack(side = "top", fill = "both", expand = True)

tk.Label(main, text = "Label top", bg = "red", fg = "white").pack(side = "top", expand = True, fill = "both")
tk.Label(second, text = "Label top", bg = "red", fg = "white").pack(side = "top", expand = True, fill = "both")
tk.Label(root, text = "Label left", bg = "green", fg = "white").pack(side = "left", expand = True, fill = "both")
tk.Label(second, text = "Lable", bg = "yellow", fg = "black").pack(side = "top", expand = True, fill = "both")

root.mainloop()
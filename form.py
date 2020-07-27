from Tkinter import *

screen = Tk()

def clickLeft(event):
	print("Left")

def clickRight(event):
	print("Right")

frame = Frame(screen, width = 200, height = 200)
frame.bind('<Button-1>', clickLeft)
frame.bind('<Button-3>', clickRight)
frame.pack()



#################### Mouse Click Events #################

'''
def printName():
	print("My name is Ioana")

button_1 = Button(screen, text = "Print my name", command = printName)
button_1.pack()
'''

# OR


'''
def printName(event):
	print("My name is Ioana")


button_1 = Button(screen, text = "Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()
'''
############## GRID LAYOUT ####################
'''
label_1 = Label(screen, text = "Name")
label_2 = Label(screen, text = "Password")

entry_1 = Entry(screen)
entry_2 = Entry(screen)

label_1.grid(row = 0, sticky = E)
label_2.grid(row = 1, sticky = E)

entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

check_box = Checkbutton(screen, text = "Keep me logged in")
check_box.grid(columnspan = 2)
'''

########### FITTING YOUR WIDGETS IN THE LABLE ################ ORGANIZING LAYOUT
'''
one = Label(screen, text = "One", fg = "blue", bg = "white")
one.pack(fill = X)
two = Label(screen, text = "Two", fg = "white", bg = "green")
two.pack(fill = X)
three = Label(screen, text = "Three", fg = "white", bg = "green")
three.pack(side = LEFT, fill = Y)
'''
######### CREATING BUTTONS ###############
'''
topFrame = Frame(screen)
topFrame.pack()
bottomFrame = Frame(screen)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg = "blue")
button2 = Button(topFrame, text = "Button 2", fg = "red")
button3 = Button(bottomFrame, text = "Button 3", fg = "green")
button4 = Button(bottomFrame, text = "Button 4", fg = "yellow")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

'''

screen.mainloop()

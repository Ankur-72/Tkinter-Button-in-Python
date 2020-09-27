from tkinter import *
root = Tk()

def clickMe():
	mylabel = Label(root,text = "Hey,look over there!")
	mylabel.pack()

myButton = Button(root,text = "Click Me!", padx = 100, pady = 100, command=clickMe , fg = "black", bg = "orange")

myButton.pack()
root.mainloop()



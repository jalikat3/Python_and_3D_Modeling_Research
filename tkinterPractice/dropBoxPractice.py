from tkinter import *
from PIL import ImageTk, Image

root=Tk()

# each item is assigned to a variable
# tkinter variable

clicked=StringVar()

# default 
clicked.set("Monday")

options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# each item is assigned to a variable
drop = OptionMenu(root, clicked, *options)
drop.pack()

def show():
    myLabel = Label(root, text=clicked.get()).pack()

myButton=Button(root, text="Show selection", command=show).pack()


root.mainloop()

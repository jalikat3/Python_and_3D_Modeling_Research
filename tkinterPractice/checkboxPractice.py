from tkinter import *
from PIL import ImageTk, Image

root=Tk()

var = StringVar()

def show():
    myLabel=Label(root, text=var.get()).pack()

c= Checkbutton(root, text="check this box, you coward >:)", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myLabel = Label(root, text=var.get()).pack()
myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()

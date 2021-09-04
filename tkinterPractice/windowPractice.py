from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()


def open():
    global my_image
    top= Toplevel()
    my_image = ImageTk.PhotoImage(Image.open("images/image1.jpg"))
    my_label=Label(top, image=my_image).pack()
    top.title("Image window")
    btn2=Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()

mainloop()

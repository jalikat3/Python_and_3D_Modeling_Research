from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# make noises (windows only?)


def popup():
    response=messagebox.askyesno("This is my popup", "Hello World!")

    # if ask question, response=="yes"
    if response==1:
        Label(root, text="You clicked yes!").pack()
    if response==0:
        Label(root, text="You clicked no :(").pack()
    
Button(root, text="Popup", command=popup).pack()

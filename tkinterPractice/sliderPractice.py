
from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.geometry('400x400')

vertical = Scale(root, from_ = 0, to=400)
vertical.pack()

def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x400")

# could use slider to resize insead of button with slide(var)
# command=slide in horizontal

horizontal = Scale(root, from_ = 0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text="Click Me!", command=slide).pack()

horizontal.get
root.mainloop()

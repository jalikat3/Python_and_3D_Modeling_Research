from tkinter import *
from PIL import ImageTk, Image

root=Tk()

r=IntVar()

MODES=[
        #text        mode
        ("Pepperoni ","Pepperoni"),
        ("Cheese","Cheese"),
        ("Hawaian","Hawaian"),
        ("Sausage","Sausage")
    ]

pizza=StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel=Label(root, text=value )
    myLabel.pack()

myButton=Button(root, text="Click me!", command=lambda:clicked(pizza.get()))
myButton.pack()
    
#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()



# keeps track of changes over time

#frame = LabelFrame(root, text="This is my frame...", padx=50, pady=50)
#frame.pack(padx=10, pady=10)

#b = Button(frame, text="Don't click here!")

#can use grid system even if frame is packed
#b.grid(row=0, column=0)

root.mainloop()

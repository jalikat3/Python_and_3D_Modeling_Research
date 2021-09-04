import tkinter as tk

class practiceTk():
    def __init__(self):
            self.root = tk.Tk()

            #e = Entry(root, width=50, fg="red", borderwidth=5)
            #e.pack()
            #e.insert(0, "Enter your name: ")
            self.myButton = tk.Button(self.root,text="Click me!", padx=50, pady=50, command=self.changeColor, fg="red", highlightbackground='pink')
            self.myButton.pack()
            self.root.mainloop()

    #def myClick():
    #    hello = ("Hello " +e.get())
    #    myLabel=Label(root, text=hello)
    #    myLabel.pack()
    #    selfx.myButton.configure(highlightbackground='red')

    def changeColor(self):
        self.myButton["fg"]='blue'
        self.myButton["highlightbackground"]='green'


    # bg=highlightbackground


    # Could do Label().grid()
    #myLabel1 = Label(root, text="Hello World!")
    #myLabel2 = Label(root, text="My name is Jali Purcell")
    #myLabel3 = Label(root, text=" ")

    #myLabel1.grid(row=0, column=0)
    #myLabel2.grid(row=1, column=5)
    #myLabel3.grid(row=1, column=1)

app=practiceTk()    

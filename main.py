'''
ictCarbonAnalysis
    main.py
    ICTFootprints.csv

By Jali Purcell
09/04/2021

Following research about the Information and Communication Technology sector's
impact regarding carbon or greenhouse gas emissions, and energy consumption.
A data analysis tool to calculate an individual's impact in owning these devices.
More development could be added with design, calculating totals, and comparing
values to recognized other carbon emitters.

'''



import webbrowser
from tkinter import *
import pandas as pd
import csv

root = Tk()
root.geometry("450x200")
deviceList = []
data = pd.read_csv("ICTFootprints.csv")
df = pd.DataFrame(data)
#import math
i=1
j=1

root.title("Carbon and Electricity Analysis")
x=[]

def learnMore():
    webbrowser.open_new_tab(url="https://www.mdpi.com/2071-1050/10/9/3027/htm")

def displayResults():

    with open("ICTFootprints.csv", "r") as f:
        reader = csv.reader(f)
        for device in deviceList:
            for row in reader:
                if device==row:
                    x.append(row)
        print(x)

    window = Toplevel()

    # col0, col1, col3
    devicedata=[[],[],[]]
    devicedata[0].append("ICT Sector")
    devicedata[1].append("Energy (KWh)")
    devicedata[2].append("GHG (MtCO2e)")
    #energyTotal=0;
    #ghgTotal=0;
    for device in deviceList:
        with open("ICTFootprints.csv", "r") as f:
            reader = csv.reader(f)
            for line_num, content in enumerate(reader):
                if content[0] == device:
                    devicedata[0].append("      "+ content[0]+"    ")
                    devicedata[1].append(content[1])
                    #energyTotal=str(int(energyTotal)+int(math.floor(content[1])))
                    devicedata[1].append("  ")
                    devicedata[2].append(content[2])
                    #ghgTotal=str(int(ghgTotal)+int(math.floor(content[2])))
                    devicedata[2].append("  ")

    # error received when calculating/adding totals
    #devicedata[1].append(energyTotal)
    #devicedata[2].append(ghgTotal)

    # why is laptop pcs inserted with {}?
    label1=Label(window,text=devicedata[0], padx=50, pady=10).grid(row=0, column=0)
    label2=Label(window,text=devicedata[1], padx=10).grid(row=1, column=0, columnspan=2)
    label3=Label(window,text=devicedata[2], padx=10).grid(row=2, column=0, columnspan=2)
    learn_button=Button(window, text="Click to learn more", height=5, command=learnMore).grid(row=3, column=0, columnspan=3)
    print(devicedata)


def add(device):
    deviceList.append(device)

# buttons for device selection window
intro_label=Label(root,anchor=CENTER, text="Click which of these devices you have to see their environmental impact.").grid(row=0, column=0, columnspan=2)
laptop_button = Button(root, text='laptop', command=lambda: add('Laptop PCs'), width=20).grid(row=1, column=0)
smartphone_button = Button(root, text='smartphone', command=lambda: add('Smartphones'), width=20).grid(row=2, column=0)
tablet_button = Button(root, text='tablet', command=lambda: add('Tablets'), width=20).grid(row=3, column=0)
desktop_display = Button(root, text='desktop', command=lambda: add('Desktop PCS'), width=20).grid(row=4, column=0)
projector_button = Button(root, text='projector', command=lambda: add('Projectors'), width=20).grid(row=5, column=0)
enter_button = Button(root, text='ENTER', command=displayResults).grid(row=3, column=1)
root.mainloop()

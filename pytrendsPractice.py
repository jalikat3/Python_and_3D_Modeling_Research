
from pytrends.request import TrendReq
import pytrends
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
import seaborn as sns
import csvPractice



# tkinter GUI
root=Tk()
root.title("Search for Interest")
global keywordList
keywordList=[]

# Entry box
e=Entry(root, width=35, borderwidth=5)
e.pack()

# Label instructions
my_label=Label(root, text="What keyword would you like to look for? (Max 5)").pack()

# initialize empty list for keywords



# Building trend graph

def plot_keywords(df):

    # returns: axis handle
    fig=plt.figure(figsize=(15,8))
    ax=fig.add_subplot(111)
    df.plot(ax=ax)
    plt.ylabel('Relative search term frquency')
    plt.xlabel('Date')
    plt.ylim((0,120))
    plt.legend(loc='lower left')
    return ax

# after finish button is pressed,
# last word is added to list and
# figure is generated

def keywordFinish():
    keywordLast = e.get()
    e.delete(0, END)
    keywordList.append(keywordLast)
    csvPractice.createCSV(keywordList)


    timeframe = "2010-01-01 2020-01-01"
    pytrends = TrendReq(hl='en-US', tz=360)

    pytrends.build_payload(keywordList, timeframe=timeframe)

    trends = pytrends.interest_over_time()

    trends.tail()

    if all(trends.isPartial == False):
        del trends['isPartial']

    plt.style.use('ggplot')
    ax = plot_keywords(trends)
    plt.show()

# after enter is pressed, word is added to list
def keywordEnter():
    keywordCur=e.get()
    e.delete(0, END)
    keywordList.append(keywordCur)

# buttons initialized after writing commands

my_button=Button(root, text="Enter", command=keywordEnter).pack()
global my_second_button
my_second_button=Button(root, text="Click this on last word", command=keywordFinish).pack()

# keep window open
root.mainloop()

















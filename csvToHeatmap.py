import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

#
#
# # read file
#
# def findIndex(df,input):
#     df = df
#
#     index = 0
#     for row in df:
#         # print row
#         if row[0] == input:
#             return index
#         else:
#             index += 1


def heatmap(keywordList):



    df = pd.read_csv('search_trends.csv')

    # for row in df:
    #     for element in df.columns[0]:
    #         if row==0 :
    #             return
    #         else:
    #             df.replace(to_replace=element, value=row)





    # drop date column

    df.drop(columns=['date'], inplace=True, axis=1)


    # insert new date column




    # # for each element, iterating through rows and columns
    # for row in df:
    #     for column in df:
    #         # if the column is 0 and the row is not 0
    #         if row !=0:
    #             if findIndex(df, df.at[row, column]):
    #             # replace the value with the row number
    #                 df.replace(value=df[row, column], inplace=row)

    # month since Jan 1, 2010
    # i = 0
    # for element in df:
    #     for row in df:
    #         if element in row[0]:
    #             df.replace(element, value=i, inplace=True)
    #             i = i+1

    # create a copy of the dataframe, and add columns for month and year

    fig, ax = plt.subplots(figsize=(11, 9))


    hm=sb.heatmap(df)
    hm.set_xlabel("Key words")
    hm.set_ylabel("Months since 2010")

    plt.title("Relative search term frequency over Jan 2010-Jan 2020")

    plt.show()
# heatmap(['dog','cat','cow'])
from pytrends.request import TrendReq
import pandas as pd
import time
import csvToHeatmap
import csv

# parameters: keywordList

def expandCSV(keywordsList):
     startTime = time.time()
     pytrend = TrendReq(hl='en-US', tz=360)

     df2=keywordsList

     dataset = []

     for x in range(0,len(df2)):
          keywords = [df2[x]]
          pytrend.build_payload(
          kw_list=keywords,
          cat=0,
          timeframe='2010-01-01 2020-01-01',
          geo='US')
          data = pytrend.interest_over_time()
          if not data.empty:
               data = data.drop(labels=['isPartial'],axis='columns')
               dataset.append(data)

     result = pd.concat(dataset, axis=1)
     result.to_csv('search_trends.csv')
     csvToHeatmap.heatmap('search_trends.csv')

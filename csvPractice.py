import csv
import keywordsToPytrends

def createCSV(keywordList):
    with open('keyword_list.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)



        for x in range(len(keywordList)):
            thewriter.writerow([keywordList[x]])
        keywordsToPytrends.expandCSV(keywordList)





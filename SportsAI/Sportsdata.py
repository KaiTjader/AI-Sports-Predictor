import os
import pandas as pd
import array

#Get data
dataFrame = pd.read_csv('./NFLTeamScores/nflTeams.csv')
print(dataFrame.head(10))

#Reading data
#topics = dataFrame.columns
#iterate threw rows
myList = []
#for index in dataFrame['Abbreviation']:
    #myList.append(dataFrame['Abbreviation'][index])
print(myList)
#print(dataFrame['Abbreviation'])
#for index, row in dataFrame.iterrows():
#    print(row)
#dataFrame.loc[dataFrame['Abbreviation'] == "RES"]
import os
import pandas as pd

#Get data
dataFrame = pd.read_csv('./SportsAI/nflData.csv')
print(dataFrame.head(10))

#Reading data
#topics = dataFrame.columns
#iterate threw rows
#for index, row in dataFrame.iterrows():
#    print(index, row)
#dataFrame.loc[dataFrame['Position'] == "RES"]
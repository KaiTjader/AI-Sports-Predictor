import os
import pandas as pd
import array

#Get data
winLossDF = pd.read_csv('/workspaces/SportsPredictor/SportsAI/nflTeams.csv')
matchUpsDF = pd.read_csv('/workspaces/SportsPredictor/SportsAI/weeklyContenders.csv')

def getPercentage(team):
    for index in range(len(winLossDF)):
        if winLossDF['Name'][index] == team:
            wins = winLossDF['Wins'][index]
            losses = winLossDF['Losses'][index]
            ties = winLossDF['Ties'][index]
            totalGames = wins + losses + ties
            winPercentage = round((wins + (.5*ties))/totalGames, 10)
    return winPercentage
for index in range(len(matchUpsDF)):
    #Get teams > win percentage
    #Get away team
    #homeTeamAdvantage = 0.031
    awayTeam = matchUpsDF['Away'][index]
    homeTeam = matchUpsDF['Home'][index]
    awayPercentage = getPercentage(awayTeam)
    homePercentage = getPercentage(homeTeam)# + homeTeamAdvantage
    if awayPercentage > homePercentage:
        predictedWinner = awayTeam
    elif awayPercentage == homePercentage:
        predictedWinner = "Tie"
    else:
        predictedWinner = homeTeam
    print(awayTeam + " @ " + homeTeam + " Winner is " + str(predictedWinner))
    print(str(awayPercentage) + " @ " + str(homePercentage))
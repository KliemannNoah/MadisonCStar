from CSLplayers import pages
from CSLcalculator import calculations
from CSLrank import ranking
from CSLregion import region
from CSLteams import teams
from CSLcsvmaker import teamCSV, playerCSV
import datetime

#page_link = 'https://cstarleague.com/lol/standings?division=Star+League&year=2019-2020'
#leagueSelection = 'Star'

page_link = 'https://cstarleague.com/lol/standings?division=Open+League&year=2019-2020'
leagueSelection = 'Open'

#page_link = 'https://cstarleague.com/lol/standings?division=Gold+League&year=2019-2020'
#leagueSelection = 'Gold'

#page_link = 'https://cstarleague.com/lol/standings?division=Junior+Varsity+2&year=2018-2019'
#leagueSelection = 'GoldOld2'

print("\nStarting Full Scrape - " + datetime.datetime.now().strftime("%I:%M:%S %p"))

print("\tScraping Standings Page - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
teams(page_link, leagueSelection)

print("\tScraping Teams Pages - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
calculations(leagueSelection)

#print("\tScraping Players Pages - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
#pages(leagueSelection)

print("\n\tEnd Scraping")
print("\tStart Processing\n")

print("\tCalculating Team Ranks - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
ranking(leagueSelection)

print("\tGenerating Ranks - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
region(leagueSelection)

print("\tGenerating Team CSV - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
teamCSV(leagueSelection)

print("\tGenerating Player CSV - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
playerCSV(leagueSelection)

print("Complete - " + datetime.datetime.now().strftime("%I:%M:%S %p"))


playerDict = {
    'name': 'IGN',
    'team': 'Team',
    'region': 'Region',
    'rank': 'Rank',
    'rankValue': 'Rank Value',
    'op.gg': 'OP.GG'
}

leagueDict = {
    'teamName': 'Team Name',
    'region': 'Region',
    'link': 'CSL Link',
    'seriesWins': 'Series Wins',
    'seriesLosses': 'Series Losses',
    'gameWins': 'Game Wins',
    'gameLosses': 'Game Losses',
    'playerList': [],
    'rank': 'Average Rank',
    'rankValue': 'Average Rank Value',
    'rank5': 'Top 5 Rank',
    'rank5Value': 'Top 5 Rank Value',
    'opgg1': 'OP.GG 1',
    'opgg2': 'OP.GG 2'
}

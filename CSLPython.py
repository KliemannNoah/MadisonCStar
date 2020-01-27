from CSLplayers import pages
from CSLcalculator import calculations
from CSLrank import ranking
from CSLregion import region
from CSLteams import teams
import datetime

#page_link = 'https://cstarleague.com/lol/standings?division=Star+League&year=2019-2020'
#page_link = 'https://cstarleague.com/lol/standings?division=Open+League&year=2019-2020'
page_link = 'https://cstarleague.com/lol/standings?division=Gold+League&year=2019-2020'

print("\nStarting Full Scrape - " + datetime.datetime.now().strftime("%I:%M:%S %p"))

print("\tScraping Standings Page - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
#teams(page_link)

print("\tScraping Teams Pages - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
#calculations()

#print("\tScraping Players Pages - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
#pages()

print("\tCalculating Team Ranks - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
ranking()

#print("\tGenerating Ranks - " + datetime.datetime.now().strftime("%I:%M:%S %p"))
#region()

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
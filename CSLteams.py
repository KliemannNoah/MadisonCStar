from bs4 import BeautifulSoup
from CSLplayers import players
#from CSLcalculator import better
from CSLregion import region
import requests
import csv
import re
import datetime
import json

r = requests.get('https://cstarleague.com/lol/standings?division=Open+League&year=2019-2020', timeout=30)
soup = BeautifulSoup(r.content, 'html.parser')

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

teamList = {}

for table in soup.find_all('table'):
    region = table.th.text
    for team in table.tbody.find_all('tr'):
        cells = team.find_all('td')
        link = cells[0].find_all('a')[1]['href'].strip()
        name = cells[0].find_all('a')[1].text.strip()
        record1 = [x.strip() for x in cells[1].text.strip().replace('(', '').replace(')', '').split('|')]
        record = [y.split('-') for y in record1]
        teamList[name] = {
            'teamName': name,
            'region': region,
            'link': link,
            'seriesWins': record[0][0].strip(),
            'seriesLosses': record[0][1].strip(),
            'gameWins': record[1][0].strip(),
            'gameLosses': record[1][1].strip(),
        }

with open('OpenLeagueTeams.json', 'w') as outfile:
    json.dump(teamList, outfile)

# import csv
# import math
# from collections import OrderedDict
import json
from bs4 import BeautifulSoup
import requests
import re

rankDistribution = {
    "Unranked": 0,
    "RANK NOT FOUND": 0,
    "Iron 4": 1,
    "Iron 3": 2,
    "Iron 2": 3,
    "Iron 1": 4,
    "Bronze 4": 5,
    "Bronze 3": 6,
    "Bronze 2": 7,
    "Bronze 1": 8,
    "Silver 4": 9,
    "Silver 3": 10,
    "Silver 2": 11,
    "Silver 1": 12,
    "Gold 4": 13,
    "Gold 3": 14,
    "Gold 2": 15,
    "Gold 1": 16,
    "Platinum 4": 17,
    "Platinum 3": 18,
    "Platinum 2": 19,
    "Platinum 1": 20,
    "Diamond 4": 21,
    "Diamond 3": 22,
    "Diamond 2": 23,
    "Diamond 1": 24,
    "Master": 25,
    "Grandmaster": 26,
    "Challenger": 27
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

#teamList[name] = [{
#    'teamName': name,
#    'region': region,
#    'link': link,
#    'seriesWins': record[0][0].strip(),
#    'seriesLosses': record[0][1].strip(),
#    'gameWins': record[1][0].strip(),
#    'gameLosses': record[1][1].strip(),
#}]

# list out keys and values separately
key_list = list(rankDistribution.keys())
val_list = list(rankDistribution.values())

league = {}


def teams(url):
    r2 = requests.get(url, timeout=30)
    soup2 = BeautifulSoup(r2.content, "html.parser")
    textContent = []
    opgg = []
    # Retrieve names on a individual webpage
    for tag in soup2.find_all("span", title=re.compile("In-Game")):
        ign = tag.get('title').split(': ')[1]
        textContent.append(ign)
        #opgg.append("https://na.op.gg/summoner/userName=" + ign)
    # op.gg
    query1 = 'https://na.op.gg/multi/query='
    query2 = 'https://na.op.gg/multi/query='
    if len(textContent) <= 10:
        for ign in textContent:
            query1 = query1 + ign + ','
    else:
        for ign in textContent[:10]:
            query1 = query1 + ign + ','
        for ign in textContent[10:]:
            query2 = query2 + ign + ','
    return [textContent, query1, query2]


with open('OpenLeagueTeams.json', 'r') as f:
    league = json.load(f)
# print(league)
for key, value in league.items():
    data = teams('https://cstarleague.com' + league[key]['link'])
    league[key]['playerList'] = data[0]
    league[key]['opgg1'] = data[1]
    league[key]['opgg2'] = data[2]
    #print(league[key])

with open('OpenLeagueTeams2.json', 'w') as outfile:
    json.dump(league, outfile)

from bs4 import BeautifulSoup
from CSLplayers import players
from CSLcalculator import better
from CSLregion import region
import requests
import csv
import re
import datetime
import json

r = requests.get('https://cstarleague.com/lol/standings?division=Open+League&year=2019-2020', timeout=30)
soup = BeautifulSoup(r.content, 'html.parser')

# Temporary Arrays
teamName = []
teamRegion = []
teamSeriesWins = []
teamSeriesLosses = []
teamGameWins = []
teamGameLosses = []
teamLink = []

#teamSeriesRecord = []
#teamGameRecord = []
#averageRank = []
#averageRankValue = []
#averageRank5 = []
#averageRank5Value = []
#teamOPGG1 = []
#teamOPGG2 = []

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
    'CSLlink': 'CSL Link',
    'seriesWins': 'Series Wins',
    'seriesLosses': 'Series Losses',
    'gameWins': 'Game Wins',
    'gameLosses': 'Game Losses'
    # Average rank
    # Average Value
    # First OP.GG
    # Second OP.GG
    # Series and Game Record
}

teams = {}

def teams(url, name, region):
    page_link2 = url
    r2 = requests.get(page_link2, timeout=30)
    soup2 = BeautifulSoup(r2.content, "html5lib")
    textContent = []
    opgg = []
    # Retrieve names on a individual webpage
    for tag in soup2.find_all("span", title=re.compile("In-Game")):
        ign = tag.get('title').split(': ')[1]
        textContent.append(ign)
        opgg.append("https://na.op.gg/summoner/userName=" + ign)
    # op.gg
    query1 = 'https://na.op.gg/multi/query='
    query2 = 'https://na.op.gg/multi/query='
    if len(textContent) <= 10:
        for ign in textContent:
            query1 = query1 + ign + ','
        #teamOPGG1.append(query1.encode("utf-8"))
        #teamOPGG2.append('')
    else:
        for ign in textContent[:10]:
            query1 = query1 + ign + ','
        for ign in textContent[10:]:
            query2 = query2 + ign + ','
        #teamOPGG1.append(query1.encode("utf-8"))
        #teamOPGG2.append(query2.encode("utf-8"))

def old():
    # Select the Team Name, Region, and URL
    for tag in soup.find_all("table"):
        print("Starting Region: " + tag.th.text)
        print(datetime.datetime.now())
        for team in tag.find_all('h3'):
            teamLink.append('https://cstarleague.com' + team.a['href'])
            teamRegion.append(tag.th.text)
            teamName.append(team.text)
            #teams('https://cstarleague.com' + team.a['href'], team.text, tag.th.text)

    # Select the Series and Game Record
    for table in soup.find_all('tr', tag.get('class') is re.compile("match-up")):
        for a in table.find_all('td', string=re.compile('|')):
            b = a.string.split('\n')
            if len(b) == 3:

                c = b[1].strip()
                c = c.replace('(', '')
                c = c.strip(')')
                c = c.split('|')

                series = c[0].strip().split('-')
                match = c[1].strip().split('-')

                #teamSeriesRecord.append(c[0].strip())
                #teamGameRecord.append(c[1].strip())
                teamSeriesWins.append(series[0].strip())
                teamSeriesLosses.append(series[1].strip())
                teamGameWins.append(match[0].strip())
                teamGameLosses.append(match[1].strip())


for table in soup.find_all('table'):
    region_raw = table.th.text
    #if region_raw not in regions:
    regions[region_raw] = []
    for team in table.tbody.find_all('tr'):
        cells = team.find_all('td')
        link = cells[0].find_all('a')[1]['href'].strip()
        name = cells[0].find_all('a')[1].text.strip()

        record1 = [x.strip() for x in cells[1].text.strip().replace('(', '').replace(')', '').split('|')]
        record = [y.split('-') for y in record1]
        regions[region_raw].append({
            'name': name,
            'link': link,
            'seriesWins': record[0][0].strip(),
            'seriesLosses': record[0][1].strip(),
            'gameWins': record[1][0].strip(),
            'gameLosses': record[1][1].strip(),
            'playerlist': []
        })

for r, teams in regions.items():
    print(r)
    for t in teams:
        print('\t{}, {}, {}, {}, {}, {}'.format(t['name'], t['seriesWins'], t['seriesLosses'], t['gameWins'], t['gameLosses'], t['link']))
    print('\n')


def after():
    combined = []
    print(datetime.datetime.now())
    combined.append(['Team Name', 'Region', 'CSL Link', 'Series Wins', 'Series Losses', 'Game Wins', 'Game Losses'])
    print("\n****************************************************\n")
    for i in range(len(teamName)):
        combined.append([teamName[i], teamRegion[i], teamLink[i], teamSeriesWins[i], teamSeriesLosses[i], teamGameWins[i], teamGameLosses[i]])
    print("Number of Total Teams Recorded: " + str(len(combined)))

    #with open('OpenLeagueTeams.csv', 'w') as csvFile:
    #    writer = csv.writer(csvFile)
    #    writer.writerows(combined)
    #csvFile.close()
    with open('OpenLeagueTeams.txt', 'w') as outfile:
        json.dump(combined, outfile)

print('Python and Players Complete')

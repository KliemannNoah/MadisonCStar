from bs4 import BeautifulSoup
from CSLplayers import players
from CSLcalculator import better
from CSLregion import region
import requests
import csv
import re
import datetime

page_link = 'https://cstarleague.com/lol/standings?division=Open+League&year=2019-2020'
r = requests.get(page_link, timeout=30)
soup = BeautifulSoup(r.content, "html5lib")

# Temporary Arrays
teamName = []
teamRegion = []
teamSeriesRecord = []
teamSeriesWins = []
teamSeriesLosses = []
teamGameWins = []
teamGameLosses = []
teamGameRecord = []
teamLink = []
averageRank = []
averageRankValue = []
teamOPGG1 = []
teamOPGG2 = []


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
        #print "https://na.op.gg/summoner/userName=" + ign
    # op.gg
    query1 = 'https://na.op.gg/multi/query='
    query2 = 'https://na.op.gg/multi/query='
    if len(textContent) <= 10:
        for ign in textContent:
            query1 = query1 + ign + ','
        teamOPGG1.append(query1.encode("utf-8"))
        teamOPGG2.append('')
    else:
        for ign in textContent[:10]:
            query1 = query1 + ign + ','
        for ign in textContent[10:]:
            query2 = query2 + ign + ','
        teamOPGG1.append(query1.encode("utf-8"))
        teamOPGG2.append(query2.encode("utf-8"))
    value = players(opgg, name, region)
    averageRank.append(value[0])
    averageRankValue.append(value[1])



# Select the Team Name, Region, and URL
for tag in soup.find_all("table"):
    print "Starting Region: " + tag.th.text
    print(datetime.datetime.now())
    for team in tag.find_all('h3'):
        teamLink.append('https://cstarleague.com' + team.a['href'])
        teamRegion.append(tag.th.text)
        teamName.append(team.text)
        teams('https://cstarleague.com' + team.a['href'], team.text, tag.th.text)
        #teamOPGG1.append('')
        #teamOPGG2.append('')

# Select the Series and Game Record
for table in soup.find_all('tr', tag.get('class') is re.compile("match-up")):
    for a in table.find_all('td', string=re.compile('|')):
        b = a.string.split('\n')
        if len(b) is 3:

            c = b[1].strip()
            c = c.replace('(', '')
            c = c.strip(')')
            c = c.split('|')
            #print c
            series = c[0].strip().split('-')
            match = c[1].strip().split('-')

            teamSeriesRecord.append(c[0].strip())
            teamGameRecord.append(c[1].strip())
            teamSeriesWins.append(series[0].strip())
            teamSeriesLosses.append(series[1].strip())
            teamGameWins.append(match[0].strip())
            teamGameLosses.append(match[1].strip())

combined = []
print(datetime.datetime.now())
combined.append(['Team Name', 'Region', 'CSL Link', 'Series Record', 'Series Wins', 'Series Losses', 'Game Record', 'Game Wins', 'Game Losses', 'Average Rank','Average Rank Number', 'First OP.GG', 'Second OP.GG'])
# Sanity Check
print "All Values should be Equal:"
print "\tNumber of Team Names: " + str(len(teamName))
print "\tNumber of Team Regions: " + str(len(teamRegion))
print "\tNumber of Team URL Links: " + str(len(teamLink))
print "\tNumber of Series Record's: " + str(len(teamSeriesRecord))
print "\tNumber of Games Record's: " + str(len(teamGameRecord))
print "\tNumber of OP.GG's: " + str(len(teamOPGG1))

print "\n****************************************************\n"

for i in range(len(teamGameRecord)):
    combined.append([teamName[i], teamRegion[i], teamLink[i], teamSeriesRecord[i], teamSeriesWins[i], teamSeriesLosses[i], teamGameRecord[i], teamGameWins[i], teamGameLosses[i], averageRank[i], averageRankValue[i], teamOPGG1[i], teamOPGG2[i]])
print "Number of Total Teams Recorded: " + str(len(combined))

with open('OpenLeagueTeams.csv', 'wb') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(combined)
csvFile.close()
print 'Python and Players Complete'
better()
print 'Better Players Complete'
region()
print 'Region Complete'

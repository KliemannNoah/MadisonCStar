from bs4 import BeautifulSoup
import requests
import json
import csv
teamList = []
playoffTeams = {}
league = {}
league2 = {}
playoffPlayers = {}

def playoffPage(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')

    for tag in soup.find_all('div', {"class": "tournament-bracket-container double-elim"}):
        vals = str(tag.get('data-bracket-teams'))
        x = vals.replace('[', '').replace(']', '')
        record1 = [q.strip() for q in x.replace('{', '').replace('\"', '').split('}')[:-1]]
        for record in record1:

            if record.find('null') == -1:
                record2 = record[1:].split(',')[0].split(':')[1].strip()
                teamList.append(record2)
            else:
                record2 = record[1:].split(',')[1].split(':')[1].strip()
                teamList.append(record2)

    with open('OpenLeagueRank.json', 'r') as f:
        league = json.load(f)

    for team in teamList:
        playoffTeams[team] = {
                'teamName': league[team]['teamName'],
                'region': league[team]['region'],
                'link': league[team]['link'],
                'seriesWins': league[team]['seriesWins'],
                'seriesLosses': league[team]['seriesLosses'],
                'gameWins': league[team]['gameWins'],
                'gameLosses': league[team]['gameLosses'],
                'playerList': league[team]['playerList'],
                'rank': league[team]['rank'],
                'rankValue': league[team]['rankValue'],
                'rank5': league[team]['rank5'],
                'rank5Value': league[team]['rank5Value'],
                'opgg1': league[team]['opgg1'],
                'opgg2': league[team]['opgg2']
        }

    with open('OpenPlayoffLeagueRank.json', 'w') as outfile:
        json.dump(playoffTeams, outfile)
    teamCSV()
    playerPage()


def teamCSV():
    csvleague = {}
    csv_columns = ['teamName', 'region', 'link',  'seriesWins', 'seriesLosses', 'gameWins',
                   'gameLosses', 'rank5', 'rank5Value', 'rank', 'rankValue', 'playerList', 'opgg1', 'opgg2']
    with open('OpenPlayoffLeagueRank.json', 'r') as f:
        csvleague = json.load(f)

    leagueList = [v for v in csvleague.values()]

    with open('OpenPlayoffLeagueRank.csv', 'w', newline="", encoding="UTF-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in leagueList:
            writer.writerow(data)


def playerPage():
    with open('OpenLeaguePlayers.json', 'r') as f:
        league2 = json.load(f)
    for team in teamList:
        for play in league2:
            #print(play)
            #print(league2[play]['team'])
            if league2[play]['team'] == team:
                playoffPlayers[league2[play]['name']] = {
                        'name': league2[play]['name'],
                        'team': league2[play]['team'],
                        'region': league2[play]['region'],
                        'rank': league2[play]['rank'],
                        'rankValue': league2[play]['rankValue'],
                        'op.gg': league2[play]['op.gg']
        }

    with open('OpenPlayoffLeaguePlayers.json', 'w') as outfile:
        json.dump(playoffPlayers, outfile)

    playerCSV()

def playerCSV():
    leaguePlayers = {}
    csv_columns = ['name', 'team', 'region', 'rank', 'rankValue', 'op.gg']

    with open('OpenPlayoffLeaguePlayers.json', 'r') as f:
        leaguePlayers = json.load(f)

    leagueList = [v for v in leaguePlayers.values()]

    with open('OpenLeaguePlayoffsPlayers.csv', 'w', newline="", encoding="UTF-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in leagueList:
            writer.writerow(data)


playoffPage('https://cstarleague.com/lol/playoffs?division=96&year=2019-2020')

from bs4 import BeautifulSoup
import requests
import json
import csv
teamList = []
playoffTeams = {}
league = {}

def playoffPage(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.content, 'html.parser')

    for tag in soup.find_all('div', {"class": "tournament-bracket-container"}):
        vals = str(tag.get('data-bracket-teams'))
        x = vals.replace('[', '').replace(']', '')
        record1 = [q.strip() for q in x.replace('{', '').replace('\"', '').split('}')[:-1]]
        for record in record1:
            record2 = record[1:].split(',')[0].split(':')[1].strip()
            teamList.append(record2)

    with open('GoldLeagueRank.json', 'r') as f:
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

    with open('GoldPlayoffLeagueRank.json', 'w') as outfile:
        json.dump(playoffTeams, outfile)
    teamCSV()


def teamCSV():
    csvleague = {}
    csv_columns = ['teamName', 'region', 'link',  'seriesWins', 'seriesLosses', 'gameWins',
                   'gameLosses', 'rank5', 'rank5Value', 'rank', 'rankValue', 'playerList', 'opgg1', 'opgg2']
    with open('GoldPlayoffLeagueRank.json', 'r') as f:
        csvleague = json.load(f)

    leagueList = [v for v in csvleague.values()]

    with open('GoldPlayoffLeagueRank.csv', 'w', newline="", encoding="UTF-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in leagueList:
            writer.writerow(data)


playoffPage('LINK')

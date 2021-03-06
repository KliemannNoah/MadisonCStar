import csv
import json


def teamCSV(leagueName):
    league = {}
    csv_columns = ['teamName', 'region', 'link', 'rank', 'rankValue', 'seriesWins', 'seriesLosses', 'gameWins',
                   'gameLosses', 'rank5', 'rank5Value', 'playerList', 'opgg1', 'opgg2']
    with open(leagueName + 'LeagueRank.json', 'r') as f:
        league = json.load(f)

    leagueList = [v for v in league.values()]

    with open(leagueName + 'LeagueRank.csv', 'w', newline="", encoding="UTF-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in leagueList:
            writer.writerow(data)


def playerCSV(leagueName):
    league = {}
    csv_columns = ['name', 'team', 'region', 'rank', 'rankValue', 'op.gg']

    with open(leagueName + 'LeaguePlayers.json', 'r') as f:
        league = json.load(f)

    leagueList = [v for v in league.values()]

    with open(leagueName + 'LeaguePlayers.csv', 'w', newline="", encoding="UTF-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in leagueList:
            writer.writerow(data)

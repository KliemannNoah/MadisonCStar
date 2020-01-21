import csv
import json

league = {}
#csv_columns = ['name', 'team', 'region', 'rank', 'rankValue', 'op.gg']
csv_columns = ['teamName', 'region', 'link', 'rank', 'rankValue', 'seriesWins', 'seriesLosses', 'gameWins', 'gameLosses', 'rank5', 'rank5Value', 'playerList', 'opgg1', 'opgg2']

with open('OpenLeagueRank.json', 'r') as f:
    league = json.load(f)

leagueList = [v for v in league.values()]

with open('OpenLeagueRank.csv', 'w', newline="", encoding="UTF-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in leagueList:
        writer.writerow(data)

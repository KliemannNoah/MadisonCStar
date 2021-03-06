from bs4 import BeautifulSoup
import requests
import json

teamList = {}


def teams(url, leagueName):
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.content, 'html.parser')

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

    with open(leagueName + 'LeagueTeams.json', 'w') as outfile:
        json.dump(teamList, outfile)

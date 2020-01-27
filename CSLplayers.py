from bs4 import BeautifulSoup
import requests
from multiprocessing.dummy import Pool as ThreadPool
import concurrent.futures
import json
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
playerDict = {
    #'name': 'IGN',
    #'team': 'Team',
    #'region': 'Region',
    #'rank': 'Rank',
    #'rankValue': 'Rank Value',
    #'op.gg': 'OP.GG'
}
pool = ThreadPool(10)


def parallel(package):
    player = package[0]
    team = package[1]
    region = package[2]
    r = requests.get("https://na.op.gg/summoner/userName=" + player, timeout=30)
    soup = BeautifulSoup(r.content, "html.parser")

    playerDict[player] = {
        'name': player,
        'team': team,
        'region': region,
        'rank': "NOT INPUT",
        'rankValue': -1,
        'op.gg': "https://na.op.gg/summoner/userName=" + player
    }

    try:
        a = soup.select_one("[class~=TierRank]" or "[class~=TierRank unranked]").text.strip()
        # Line is for Gold only
        #if rankDistribution[a] < 17:
        playerDict[player]['rank'] = a
        playerDict[player]['rankValue'] = rankDistribution[a]
    except AttributeError:
        playerDict[player]['rank'] = "RANK NOT FOUND"
        playerDict[player]['rankValue'] = 0


def players(URLlist, name, region):
    executor = concurrent.futures.ThreadPoolExecutor(10)
    futures = [executor.submit(parallel, [player, name, region]) for player in URLlist]
    concurrent.futures.wait(futures)


def pages():
    with open('GoldLeagueTeams2.json', 'r') as f:
    #with open('OpenLeagueTeams2.json', 'r') as f:
    # with open('StarLeagueTeams2.json', 'r') as f:
        league = json.load(f)

    for key, value in league.items():
        players(league[key]['playerList'], league[key]['teamName'], league[key]['region'])

    with open('GoldLeaguePlayers.json', 'w') as outfile:
    #with open('OpenLeaguePlayers.json', 'w') as outfile:
    # with open('StarLeaguePlayers.json', 'w') as outfile:
        json.dump(playerDict, outfile)

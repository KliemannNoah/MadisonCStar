from bs4 import BeautifulSoup
import requests
import csv
import math
from multiprocessing.dummy import Pool as ThreadPool
import concurrent.futures

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
pool = ThreadPool(10)


def parallel(player):
    r = requests.get("https://na.op.gg/summoner/userName=" + player, timeout=30)
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        a = soup.select_one("[class~=TierRank]" or "[class~=TierRank unranked]").text.strip()
        return [[a, rankDistribution[a], player.encode("utf-8")], rankDistribution[a]]

    except AttributeError:
        return [["RANK NOT FOUND", 0, player.encode("utf-8")], 0]

def players(URLlist, name, region):
    playerList = []
    playerRankFull = []
    data = []
    #for player in URLlist:
    executor = concurrent.futures.ThreadPoolExecutor(10)
    futures = [executor.submit(parallel, player) for player in URLlist]
    concurrent.futures.wait(futures)
            #executor.map(parallel(player, name, region), range(3))
        #data.append(pool.apply_async(parallel, (player, name, region)).get())
        # playerList.append(data[0])
        # playerRankFull.append(data[1])

    #pool.close()
    #pool.join()
    for i in data:
        playerList.append(i[0])
        playerRankFull.append(i[1])

    #with open('OpenLeaguePlayers.csv', 'ab') as csvFile:
    #    writer = csv.writer(csvFile)
    #    writer.writerows(playerList)
    #csvFile.close()

    teamrank = 0
    teamrank5 = 0

    for rank in playerRankFull:
        teamrank = teamrank + rank

    playerRankFull.sort(reverse=True)

    for rank in playerRankFull[:5]:
        teamrank5 = teamrank5 + rank

    if len(playerRankFull) != 0:
        average = math.ceil(teamrank / len(playerRankFull))
        average5 = math.ceil(teamrank5 / 5)
        response = [key_list[val_list.index(average)], average, key_list[val_list.index(average5)], average5]
    else:
        response = ["No Players Found", 0, "No Players Found", 0]
    print("Finished Team")
    return response

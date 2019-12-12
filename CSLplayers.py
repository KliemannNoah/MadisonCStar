from bs4 import BeautifulSoup
import requests
import csv
import re
import datetime
import math

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
# list out keys and values separately
key_list = list(rankDistribution.keys())
val_list = list(rankDistribution.values())


def players(URLlist, name, region):
    playerList = []
    playerRank = []
    sum = 0
    for player in URLlist:
        page_link = player
        r = requests.get(page_link, timeout=30)
        soup = BeautifulSoup(r.content, "html5lib")
        try:
            a = soup.select_one("[class~=TierRank]" or "[class~=TierRank unranked]").text.strip()
            playerList.append([name, region, a, rankDistribution[a], player.encode("utf-8")])
            playerRank.append(rankDistribution[a])
        except AttributeError:
            playerList.append([name, region, "RANK NOT FOUND", 0, player.encode("utf-8")])
            playerRank.append(0)


    with open('OpenLeaguePlayers.csv', 'ab') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(playerList)
    csvFile.close()

    for rank in playerRank:
        sum = sum + rank

    if len(playerRank) != 0:
        average = math.ceil(sum / len(playerRank))
        response = [key_list[val_list.index(average)], average]
    else:
        response = ["No Players Found", 0]

    return response

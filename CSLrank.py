import math
from multiprocessing.dummy import Pool as ThreadPool
import concurrent.futures
import json
import datetime
from collections import defaultdict

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
league = {}
teamDict = {}

key_list = list(rankDistribution.keys())
val_list = list(rankDistribution.values())
val_list2 = list(league.values())

teams = {}
players = {}

def determineTeamRank(listOfPlayerVals):
    teamrank = 0
    teamrank5 = 0

    for rank in listOfPlayerVals:
        teamrank = teamrank + rank

    listOfPlayerVals.sort(reverse=True)

    for rank in listOfPlayerVals[:5]:
        teamrank5 = teamrank5 + rank

    if len(listOfPlayerVals) != 0:
        average = math.ceil(teamrank / len(listOfPlayerVals))
        average5 = math.ceil(teamrank5 / 5)
        response = [key_list[val_list.index(average)], average, key_list[val_list.index(average5)], average5]
    else:
        response = ["No Players Found", 0, "No Players Found", 0]
    #print(response)
    return response


with open('OpenLeagueTeams2.json', 'r') as f:
    t = json.load(f)

with open('OpenLeaguePlayers.json', 'r') as f:
    p = json.load(f)


tempTeams = {}
permanentTeams = {}

for team in teams:
    tempTeams[team] = []

pkeys = players.keys()
for key in pkeys:
    tempPlayer = players[key]
    tempTeams[tempPlayer["team"]].append(tempPlayer["rankValue"])

for key in tempTeams:
    statement = determineTeamRank(tempTeams[key])
    permanentTeams[key] = {
        'rank': statement[0],
        'rankValue': statement[1],
        'rank5': statement[2],
        'rank5Value': statement[3]
    }
    print(key, permanentTeams[key])

compositeDict = defaultdict(dict)

for dictionary in (t, permanentTeams):
    for key, value in dictionary.items():
        compositeDict[key].update(value)

with open('OpenLeagueRank.json', 'w') as outfile:
    json.dump(compositeDict, outfile)
import csv
from collections import defaultdict
import math
import json

league = {}


def region():
    rankMapping = {
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

    # defaultdict allows a dictionary with a list as a value
    regionRankList = defaultdict(list)

    # Numb is for the numerical value associated with the rank based on
    allRank = []
    allRankNumb = []
    top2Rank = []
    top2RankNumb = []
    top4Rank = []
    top4RankNumb = []
    top6Rank = []
    top6RankNumb = []
    top8Rank = []
    top8RankNumb = []
    top10Rank = []
    top10RankNumb = []

    regionName = []
    # final output
    combined = []
    # Splitting of the rankMapping dictionary to use the rank name (Platinum 4) to get it's number value (17)
    key_list = list(rankMapping.keys())
    val_list = list(rankMapping.values())

    # Read in File of Teams
    # with open('GoldLeagueRank.json', 'r') as f:
    with open('OpenLeagueRank.json', 'r') as f:
        jsonData = json.load(f)

    for key, value in jsonData.items():
        if jsonData[key]['region'] in regionRankList:
            regionRankList[jsonData[key]['region']].append(jsonData[key]['rank5Value'])
        else:
            regionRankList[jsonData[key]['region']] = [jsonData[key]['rank5Value']]

    # Sort within each conference
    for conference in regionRankList:
        regionRankList[conference].sort(reverse=True)

    # Link talks about the reason for needing the 'float' operation
    # https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10

    # Total Roster
    for team in regionRankList:
        regionName.append(team)
        regionRank = 0
        members = 0
        for member in regionRankList[team]:
            regionRank += int(float(member))
            members = members + 1
        a = math.ceil(regionRank/members)
        allRank.append(a)
        allRankNumb.append(key_list[val_list.index(a)])

    # Top 2 Teams
    for team in regionRankList:
        regionRank = 0
        members = 0
        for member in regionRankList[team][:2]:
            regionRank += int(float(member))
            members = members + 1
        a = math.ceil(regionRank/members)
        top2Rank.append(a)
        top2RankNumb.append(key_list[val_list.index(a)])

    # Top 4 Teams
    for team in regionRankList:
        regionRank = 0
        members = 0
        for member in regionRankList[team][:4]:
            regionRank += int(float(member))
            members = members + 1
        a = math.ceil(regionRank/members)
        top4Rank.append(a)
        top4RankNumb.append(key_list[val_list.index(a)])

    # Top 6 Teams
    for team in regionRankList:
        regionRank = 0
        members = 0
        for member in regionRankList[team][:6]:
            regionRank += int(float(member))
            members = members + 1
        a = math.ceil(regionRank/members)
        top6Rank.append(a)
        top6RankNumb.append(key_list[val_list.index(a)])

    # Top 8 Teams
    for team in regionRankList:
        regionRank = 0
        members = 0
        for member in regionRankList[team][:8]:
            regionRank += int(float(member))
            members = members + 1
        a = math.ceil(regionRank/members)
        top8Rank.append(a)
        top8RankNumb.append(key_list[val_list.index(a)])

    # Top 10 Teams
    for team in regionRankList:
        regionRank = 0
        members = 0
        for member in regionRankList[team][:10]:
            regionRank += int(float(member))
            members = members + 1
        a = math.ceil(regionRank/members)
        top10Rank.append(a)
        top10RankNumb.append(key_list[val_list.index(a)])

    combined.append(['Region Name', 'All Teams', 'All Teams #', '2 Best Teams', '2 Best Teams #', '4 Best Teams', '4 Best Teams #', '6 Best Teams', '6 Best Teams #', '8 Best Teams', '8 Best Teams #', '10 Best Teams', '10 Best Teams #'])
    for i in range(len(regionRankList)):
        combined.append([regionName[i], allRankNumb[i], allRank[i], top2RankNumb[i], top2Rank[i], top4RankNumb[i], top4Rank[i], top6RankNumb[i], top6Rank[i], top8RankNumb[i], top8Rank[i], top10RankNumb[i], top10Rank[i]])

    # with open('GoldLeagueRegion.csv', 'w', newline='') as csvFile:
    with open('OpenLeagueRegion.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(combined)
    csvFile.close()

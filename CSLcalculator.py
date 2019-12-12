import csv
import math
from collections import OrderedDict


def better():
    rankDistribution2 = {
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
    rankDistribution = OrderedDict()
    teamRegion = []
    teamranked = []
    teamRankedRank = []
    teamranked2 = []
    teamRankedRank2 = []
    teams = []
    key_list = list(rankDistribution2.keys())
    val_list = list(rankDistribution2.values())

    with open('OpenLeaguePlayers.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for key in csv_read:
            if key[0] in rankDistribution:
                rankDistribution[key[0]].append(int(float(key[3])))
            else:
                rankDistribution[key[0]] = [int(float(key[3]))]
                teamRegion.append(key[1])

    #sort
    for team in rankDistribution:
        rankDistribution[team].sort(reverse=True)

    # Total Roster
    for team in rankDistribution:
        teamrank = 0
        members = 0
        teams.append(team)
        for member in rankDistribution[team][:5]:
            teamrank += int(member)
            members = members + 1
        a = math.ceil(teamrank/members)
        teamranked2.append(a)
        teamRankedRank2.append(key_list[val_list.index(a)])

        teamrank = 0
        members = 0
        for member in rankDistribution[team]:
            teamrank += int(member)
            members = members + 1
        a = math.ceil(teamrank/members)
        teamranked.append(a)
        teamRankedRank.append(key_list[val_list.index(a)])

    combined = []
    combined.append(['Team Name', 'Team Region', '5 Best Players', '5 Best Players Number', 'All Players', 'All Players Number'])
    for i in range(len(teams)):
        combined.append([teams[i], teamRegion[i], teamRankedRank2[i], teamranked2[i], teamRankedRank[i], teamranked[i]])

    with open('OpenLeagueTeam2.csv', 'wb') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(combined)
    csvFile.close()


    #print teamranked
    #print teamranked2

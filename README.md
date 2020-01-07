# MadisonCStar
Repository for all of the scripts and various bits for the UW Madison League of Legends Team

# Current Use Case
Currently the script is run by calling CSLPython while having an Internet Connection. It is expected to take up to 2 hours to run correctly at the current moment. Output is kept for any players already recorded, but the teams information won't save unless the program fully executes

# Script Descriptions

### CSLPython
This is the main program to be run, and contains code within it that kicks off the CSLplayers and CSLregion scripts. 
It crawls the CSL standings page first grabbing Team Name, Region and Team page URL before handing the team page URL to a helper funtion that collects the OP.GG's of the team and calls CSLplayers.
It then crawls the entire page a second time, this time grabbing all of the Series and Game records for each team.
It then takes all of the crawled Data and writes it to a file.
After it has writted to the OpenLeagueTeams.csv, it then calls the CSLregion in order to get the region ranking.

### CSLplayers
Takes a individual teams CSL page and scrapes it for all of the players on that team. It then looks up their OP.GG and takes their current rank.
It also equates each rank to a numerical value, and calculates the average rank of the entire team, and then the average rank of their top 5 players.
Player specific information is sent to a CSV that will contian every player, their team name, their region, their rank and OP.GG.
The calculations for team rank are sent back to the main program to be added to the team CSV.

### CSLregion
Reads in the team file and averages out how strong that region is relative to the other regions. Has lots of different divisions to give a better picture of division strength, All and Top10 fields may be unnessecary.

### CSLcalculator
Now deprecated file that took in the CSLplayers page as input, and worked on ranking each team by their top 5 players. Functionality has now been rolled into the CSLPlayer and CSLPython scripts.

# CSV File Descriptions
CSV files are a type of data storage similar to a spreadsheet and can be open in traditional spreadsheet applications like Excell and Google Sheets, but some low importance columns do not work well in Excell so Google Sheets is recommended. 

### OpenLeagueTeams
This file contains all of the information related to a single team, namely their name, region, standing, average rank and list of players.

### OpenLeaguePlayers
This file is a master list of every CSLplayer in that League. Namely stores region, team name, player name, rank, and op.gg

### OpenLeagueRegion
This file contains a ranking of all of the regions in the League.

# Areas of Futre Improvement

### Planned
- Multi-Thread HTTP Requests to speed up performance
- Modularize some function methods to make it easier to run without needing to run the whole script
- Better comments are needed in order to pass on this script to new users
- Find a way to create a historical set of CSV files to look at past information
- Extract and manipulate previous season ranks from OP.GG for after rank reset
- Modularize ouput to allow users to only export columns they want to see
- Save the team data continuously encase of failover

### Stretch Goals
- Include Visualization Metrics into the site for apperance purposes
- Possibly change data structures to dict of dicts instead of dict with a list
- Create documentation on how to do some of the website parsing work from scratch incase of CSL changes
- Find a way to replicate this for playoffs
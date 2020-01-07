from bs4 import BeautifulSoup
from CSLplayers import pages
from CSLcalculator import calculations
from CSLrank import ranking
from CSLregion import region
from CSLteams import teams
import csv
import datetime

page_link = 'https://cstarleague.com/lol/standings?division=Open+League&year=2019-2020'

print("Starting Full Scrape")
print(datetime.datetime.now())

print("\tScraping Standings Page")
teams(page_link)
print(datetime.datetime.now())

print("\tScraping Teams Pages")
calculations()
print(datetime.datetime.now())

print("\tScraping Players Pages")
pages()
print(datetime.datetime.now())

print("\tCalculating Team Ranks")
ranking()
print(datetime.datetime.now())

print("\nComplete")


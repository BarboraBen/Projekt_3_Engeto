"""
election_scraper.py: třetí projekt do Engeto Online Python Akademie
author: Barbora Benešová
email: benes.barbora@seznam.cz
discord: barbora_benesova
"""
from project_3_modules import parsing_url
from project_3_modules import scrape_code
from project_3_modules import scrape_location
from project_3_modules import scrape_location_url
from project_3_modules import scrape_registered
from project_3_modules import scrape_envelopes
from project_3_modules import scrape_valid
from project_3_modules import scrape_votes
import pandas as pd
import sys
import re

if len(sys.argv) != 3:
    print("It is necessary to input 2 arguments. Ending the program...")
    exit()

url = sys.argv[1]
name_csv = sys.argv[2]

if re.fullmatch(r"^https://volby.cz/pls/ps2017nss/ps3\d{1,2}\?xjazyk=CZ&xkraj=\d{1,2}&xnumnuts=\d{4}$", url):
    pass
else:
    print("Wrong link, ending the program...")
    exit()

if re.fullmatch(r"\w*.csv", name_csv):
    pass
else:
    print("File name must contains alphanumeric characters and suffix '.csv', ending the program...")
    exit()

print(f" Loading data from {url}.")
soup = parsing_url(url)

df = pd.DataFrame(scrape_code(soup), columns=["Code"])
df["Location"] = scrape_location(soup)

location_url = scrape_location_url(soup)
soups = [parsing_url(i) for i in location_url]

df["Registered"] = [scrape_registered(i) for i in soups]
df["Envelopes"] = [scrape_envelopes(i) for i in soups]
df["Valid"] = [scrape_valid(i) for i in soups]

data = [scrape_votes(i) for i in soups]
df = df.join(pd.DataFrame(data, index=df.index))

df.to_csv(name_csv, index=False)
print(f" Data was succesfully loaded to {name_csv} file.")
print("Ending the program.")

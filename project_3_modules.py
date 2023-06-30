"""
project_3_modules.py: třetí projekt do Engeto Online Python Akademie
author: Barbora Benešová
email: benes.barbora@seznam.cz
discord: barbora_benesova
"""
from requests import get
from bs4 import BeautifulSoup as bs
import re
import urllib.parse


def parsing_url(url):
    data = get(url)
    return bs(data.text, features="html.parser")


def scrape_code(soup):
    "Function to scrape codes of locations in chosen district."
    return [i.text for i in soup.find_all('td', headers=re.compile(r"t\dsa1 t\dsb1"))
            if re.fullmatch(r"\d{6}", i.text)]


def scrape_location(soup):
    "Function to scrape names of locations in chosen district."
    return [i.text for i in soup.find_all('td', "overflow_name")]


def scrape_location_url(soup):
    """Function to find links for results in individual locations.
    Firstly function makes list of relative paths, then base adress is joined."""
    web_links = []
    for i in soup.find_all("td", headers=re.compile(r"t\dsa1 t\dsb1")):
        for j in i.find_all("a"):
            web_links.append(j.get("href"))
    base = "https://volby.cz/pls/ps2017nss/"
    return [urllib.parse.urljoin(base, i) for i in web_links]


def scrape_registered(soup):
    "Function returns number of registred voters in particular location."
    registered = soup.find('td', headers="sa2").text
    return registered.replace("\xa0", "")


def scrape_envelopes(soup):
    "Function returns number of envelopes in particular location."
    envelopes = soup.find('td', headers="sa3").text
    return envelopes.replace("\xa0", "")


def scrape_valid(soup):
    "Function returns number of valid votes in particular location."
    valid = soup.find('td', headers="sa6").text
    return valid.replace("\xa0", "")


def scrape_votes(soup):
    """Function returns dictionary with elected parties and number of votes
     in particular location."""
    parties = [i.text for i in soup.find_all('td', "overflow_name")]
    votes = [i.text for i in soup.find_all('td', headers=re.compile(r"t\dsa2 t\dsb3"))]
    return {parties[i]: votes[i] for i in range(len(parties))}

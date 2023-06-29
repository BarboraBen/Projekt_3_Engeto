# Projekt_3_Engeto
Project 3 Engeto Python Academy

## Description

Program for scraping data from Election to Chamber of Deputies in 2017. Link is here: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

## Installing modules
Modules needed for executing the program are listed in file requirments.txt. 
It is recomended to install necessary modules to new virtual environment. We can install modules as following:
```pip install -r requirements.txt```

## Executing program

To execute the program it is necessary to input 2 arguments:
* Link to election results in a chosen district
* Name of output file in csv format

python election_scraper.py <link for chosen district> <name of output file>

## Example
### Results for district Příbram
1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111`
2. argument: `pribram_results.csv`
`python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111" "pribram_results.csv"`

### Downloading process
```
 python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111" "pribram_results.csv"
 Loading data from https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2111.
 Data was succesfully loaded to pribram_results.csv file.
 Ending the program.
```
### Partial output
```
Code,Location,Registered,Envelopes,Valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,...
529672,Bezděkov pod Třemšínem,134,105,103,12,0,0,10,0,13,11,2,0,1,0,1,11,0,0,0,32,0,1,3,0,0,0,1,5,0
564559,Bohostice,167,108,108,12,0,0,9,0,5,22,1,0,0,0,0,7,0,0,5,37,0,0,4,0,0,0,1,5,0
539953,Bohutín,1417,925,920,93,1,2,50,0,45,75,12,6,13,2,1,88,1,1,50,348,1,2,30,1,7,2,0,88,1
539970,Borotice,302,202,202,18,1,0,20,0,13,13,3,0,0,0,0,23,0,0,9,65,0,0,15,0,4,0,1,16,1
539988,Bratkovice,252,167,166,29,0,0,11,0,11,15,1,0,1,0,0,11,0,0,9,40,0,0,9,0,7,0,0,22,0
```

import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

matches_per_year = {}

#function that calculates the number of matches
def matches (eachrow , matches_per_year):
    if eachrow['season'] in matches_per_year:
        matches_per_year[eachrow['season']] += 1
    else :
        matches_per_year[eachrow['season']] = 1



def calculate ():

    with open ('data/matches.csv') as CSV_file:

        csv_reader = csv.DictReader(CSV_file)

        for eachrow in csv_reader:
            matches(eachrow , matches_per_year)


#plot function

def plot(matches_per_year):

    season = list(matches_per_year.keys())
    matches = list(matches_per_year.values())

    plt.bar(season , matches)
    plt.title('Matches per Season')
    plt.xlabel('Season')
    plt.ylabel('Number Of Matches')
    plt.tight_layout()
    plt.show()

def exicute ():

    calculate()
    plot(matches_per_year)


exicute()
    


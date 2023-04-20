import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

matches_id_of_2016 = set()

extras_per_team = {}

#function that gives ID's of Matches Played in 2016 
def calculate_matches_2016 ():

    with open('data/matches.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:

            if eachrow['season'] == '2016':
                matches_id_of_2016.add(eachrow['id'])


#Function that fills extras per team in 2016 dictionary
def extras_of_eachteam(eachrow , extras_per_team):

    if eachrow['match_id'] in matches_id_of_2016:
        if eachrow['bowling_team'] in extras_per_team:
            extras_per_team[eachrow['bowling_team']] += int(eachrow['extra_runs'])
        else :
            extras_per_team[eachrow['bowling_team']] = int(eachrow['extra_runs'])

def calculate ():

    calculate_matches_2016()

    with open('data/deliveries.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            extras_of_eachteam(eachrow, extras_per_team)


def plot (extras_per_team):

    team = list(extras_per_team.keys())

    extras = list(extras_per_team.values())

    plt.barh(team , extras)
    plt.title('Extras Of Each Team in 2016')
    plt.xlabel('Teams')
    plt.ylabel('Extras')
    plt.tight_layout()
    plt.show()


def exicute():

    calculate()
    plot(extras_per_team)

exicute()


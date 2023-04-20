import csv
import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')



runs_by_eachteam = {}



#funtion to create a dictionary of runs by each team

def scoredruns(eachrow , runs_by_eachteam):

    if eachrow['batting_team'] in runs_by_eachteam:
        runs_by_eachteam[eachrow['batting_team']]+=int(eachrow['total_runs'])
    else :
        runs_by_eachteam[eachrow['batting_team']]=int(eachrow['total_runs'])


#Calculate function for reading data from csv file and calls scoresruns each iteration

def calculate():

    with open('data/deliveries.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            scoredruns(eachrow,runs_by_eachteam)

#plot fuuntion to plot a graph 
def plot(runs_by_eachteam):

    teams = list(runs_by_eachteam.keys())
    scores = list(runs_by_eachteam.values())


    plt.barh(teams,scores)
    plt.title('Total runs of each team Through History of IPL')
    plt.xlabel('Runs')
    plt.ylabel('Teams')
    plt.tight_layout()
    plt.show()
    

def exicute():
    calculate()
    plot(runs_by_eachteam)

exicute()


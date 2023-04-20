import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


batters_of_rcb = {}



#funtion to create a dictionary of runs by each team

def runsofeachbatter (eachrow,batters_of_rcb):

    if eachrow['batting_team'] == 'Royal Challengers Bangalore' and eachrow['batsman'] in batters_of_rcb:
        batters_of_rcb[eachrow['batsman']]+=int(eachrow['batsman_runs'])
    else :
        if eachrow['batting_team'] == 'Royal Challengers Bangalore' and not (eachrow['batsman'] in batters_of_rcb) :
            batters_of_rcb[eachrow['batsman']]=int(eachrow['batsman_runs'])


#Calculate function for reading data from csv file and calls runsofeachbatter() each iteration

def calculate():

    with open('data/deliveries.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:
            runsofeachbatter(eachrow , batters_of_rcb)

#plot fuuntion to plot a graph 
def plot(batters_of_rcb):

    batterslist = list(batters_of_rcb.items())

    for i in range(0,len(batterslist)):
        for j in range(i+1 , len(batterslist)):

            if batterslist[i][1]<batterslist[j][1]:
                batterslist[j] , batterslist[i] = batterslist[i] , batterslist[j]
    
    toptenbatters = batterslist[:10]
    print (toptenbatters)
    batters = []
    scores = []

    for batsman in toptenbatters :
        batters.append(batsman[0])
        scores.append(batsman[1])


    plt.bar(batters,scores)
    plt.title('Top 10 RCB Batters')
    plt.xlabel('Batsman')
    plt.ylabel('Scores')
    plt.tight_layout()
    plt.show()
    

def exicute():
    calculate()
    plot(batters_of_rcb)

exicute()


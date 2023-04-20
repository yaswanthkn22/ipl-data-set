import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

matches_id_of_2015 = set()
bowler_dict = {}
bowler_economy = {}

def get_matches_id ():

    with open ('data/matches.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:

            if eachrow['season'] == '2015':
                matches_id_of_2015.add(eachrow['id'])


def calculate_bowler_dict ():

    with open('data/deliveries.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for eachrow in csv_reader:

            if eachrow['match_id'] in matches_id_of_2015:

                if eachrow['bowler'] in bowler_dict:
                    bowler_dict[eachrow['bowler']][0] +=1
                    bowler_dict[eachrow['bowler']][1] += int(eachrow['total_runs'])
                else :
                    bowler_dict[eachrow['bowler']] = []
                    bowler_dict[eachrow['bowler']].append(1)
                    bowler_dict[eachrow['bowler']].append(int(eachrow['total_runs']))

def bowlerEconomy(bowler_dict):

    for key , value in bowler_dict.items():

        bowler_economy[key]= round (value[1]/(value[0]/6) , 2)

def plot (bowler_economy):

    list_of_bowlers = list(bowler_economy.items())

    for i in range(0,len(list_of_bowlers)):
        for j in range(i+1 , len(list_of_bowlers)):
            if list_of_bowlers[i][1] > list_of_bowlers[j][1]:
                list_of_bowlers[j],list_of_bowlers[i] = list_of_bowlers[i],list_of_bowlers[j]

    
    bowlers = []
    economies = []

    for bowler , economy in list_of_bowlers[:10]:
        bowlers.append(bowler)
        economies.append(economy)
        
    print(bowlers)
    print(economies)
    plt.bar(bowlers, economies) 
    plt.title('Top 10 Economic Bowlers in 2015')
    plt.xlabel('Bowler')
    plt.ylabel('Economy')
    plt.tight_layout()
    plt.show()


def exicute():

    get_matches_id()
    calculate_bowler_dict()
    bowlerEconomy(bowler_dict)
    plot(bowler_economy)

exicute()


    

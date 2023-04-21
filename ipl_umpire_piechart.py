import csv
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

umpires_count_by_countries = {}

# function calculates the countries of umpires and their count
def fill_umpires_countries_count(eachrow , umpires_count_by_countries):

    if eachrow['country'] in umpires_count_by_countries:

        umpires_count_by_countries[eachrow['country']] += 1
    else : 
        if eachrow['country'].upper() != 'India'.upper():
            umpires_count_by_countries[eachrow['country']] = 1


def calculate():
     
    with open ('data/umpires.csv') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for eachrow in csv_reader:
            fill_umpires_countries_count(eachrow, umpires_count_by_countries)


# ploting the pie chart for the above umpires_count_by_countirs dictionary by unpacking it
def plot():

    countries = []

    country_count = []

    for country , count in umpires_count_by_countries.items():

        countries.append(country)
        country_count.append(count)

    plt.pie(country_count , labels=countries , wedgeprops={'edgecolor':'black'} , autopct='%0.1f%%')
    plt.title('Umpires from different parts of the world in IPL except India')
    plt.tight_layout()
    plt.show()

def exicute():

    calculate()
    plot()


# exicute function perfarms the entire task by calling calculate() and plot()
exicute()




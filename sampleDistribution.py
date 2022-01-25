import plotly.figure_factory as ff 
import random 
import pandas as pd 
import csv
import statistics 

df = pd.read_csv('medium_data.csv')
medium_data = df['id'].tolist()
population_mean = statistics.mean(medium_data)
population_standardDiviation = statistics.stdev(medium_data)

def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(medium_data)-1)
        value = medium_data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showfig(meanlist):
    df = meanlist
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["id"],show_hist = False)
    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setOfmean = randomsetofmean(100)
        meanlist.append(setOfmean)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    print("meanOfSampleDistribution",mean)

setup()
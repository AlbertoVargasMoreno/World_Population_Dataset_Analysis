import matplotlib.pyplot as plt
import squarify
import plotly.express as px
import pandas as pd
#import functions as functions

def generate_bar_chart(labels, values, country):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.gca().get_yticks()
    plt.title(country)
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.show()

def generate_pie_chart(labels, values, country):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.title(country)
    ax.axis("equal")
    plt.show()

def tree_map_chart(labels, values, country):
    fig, ax = plt.subplots()
    plt.title(country)
    squarify.plot(label=labels, sizes=values, pad=True)
    plt.axis('off')
    plt.show()

def tree_map_chart_px():
    df = pd.read_csv('world_population.csv', header=True, sep=',')
    print(df)
    #px.treemap(data_frame=)
    return df

""" #prueba
def mex_values(data):
    
    mex_labels = [i for i in data[131].keys()]
    mex_labels = mex_labels[5:13]
    mex_labels = [ i[0:4] for i in mex_labels]
    #Obtener values
    mex_values = [j for j in data[131].values()]
    mex_values = mex_values[5:13]
    mex_values = [int(j) for j in mex_values]

    #print("\n", mex_labels)
    #print("\n", mex_values)
    return mex_labels, mex_values
    #generate_bar_chart(mex_labels,mex_values)
    """

"""
#Reto 2

    #continent_countries = list(filter(lambda item : item["Country/Territory"], region))
    continent_countries = [countries["Country/Territory"] for countries in region]
    continent_area = [int(countries['Area (km²)']) for countries in region]
    print(continent_countries)
    print(continent_area)
    generate_bar_chart(continent_countries,continent_area,"Continent")
"""
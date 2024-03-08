import csv
from charts import *

#Funcion para cargar el CSV
def read_csv(path):
    """ Funcion para abrir CSV"""
    with open(path,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def options_menu():
    print("\nLas acciones disponibles son las siguientes:")
    print("  1. Seleccionar país y graficar poblacion por periodo de tiempo")
    print("  2. Seleccionar pais y obtener su información")
    print("  3. Seleccionar continente y graficar por poblacion")
    print("  4. Seleccionar continente y graficar por territorio")
    print("  5. Funcion especial: Treemap Poblacion Mundial")
    print("  0. Salir")
    option = int(input("\nIngresa una opción: "))
    while option < 0 or option > 5:
        print("Seleccion invalida. Inténtalo otra vez.")
        option = int(input("Ingresa una opción: "))
    return option

def population_country(data, country):
    result = list(filter(lambda item : item["Country/Territory"] == country, data))
    return result

def get_population(country_dict):
  population_dict = {
    '1970': int(country_dict['1970 Population']),
    '1980': int(country_dict['1980 Population']),
    '1990': int(country_dict['1990 Population']),
    '2000': int(country_dict['2000 Population']),
    '2010': int(country_dict['2010 Population']),
    '2015': int(country_dict['2015 Population']),
    '2020': int(country_dict['2020 Population']),
    '2022': int(country_dict['2022 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_region(data, continent):
    region = list(filter(lambda item : item["Continent"] == continent, data))
    return region

def get_info(result):
    result = result[0]
    #print(result)
    #return 0
    print("\nCountry/Territory:", result["Country/Territory"])
    print("Capital:", result["Capital"])
    print("Continent:",result["Continent"])
    print("CCA3:", result["CCA3"])
    print("Area (km\²):",int(result["Area (km2)"]))
    print("Rank:", result["Rank"])
    print("Density (per km²):",float(result["Density (per km2)"]))
    print("Growth Rate:",float(result["Growth Rate"]))
    print("World Population Percentage:",float(result["World Population Percentage"]))

def get_continent_area(data, continent):
    region = population_region(data, continent)
    continent_countries = [countries["Country/Territory"] for countries in region]
    continent_area = [int(countries['Area (km²)']) for countries in region]
    
    return continent_countries, continent_area    
def get_continent_population(data, continent):
    region = population_region(data, continent)
    continent_countries = [countries["Country/Territory"] for countries in region]
    continent_population = [int(countries['2022 Population']) for countries in region]
    return continent_countries, continent_population



from charts import *
from functions import *
import tkinter


if __name__ == "__main__":
    
    #Cargamos el CSV
    data = read_csv("world_population.csv")
    print("\nBienvenido al script de 'Poblacion Mundial'!!!")
    #MENU

    opcion = 1
while opcion != 0:

    #Se muestra el menu
    opcion = options_menu()

    #1.- Seleccionar país y graficar poblacion por periodo de tiempo
    if opcion == 1:
        country =  input("Escribe el nombre del pais a consultar: ").title()
        result = population_country(data, country)
        if len(result) > 0:
            country = result[0]
            labels, values = get_population(country)
            generate_bar_chart(labels,values, country["Country/Territory"])

    #2.- Seleccionar pais y obtener su información
    elif opcion == 2:
        country =  input("Escribe el nombre del pais a consultar: ").title()
        result = population_country(data, country)
        get_info(result)

    #3.- Seleccionar continente y graficar por poblacion
    elif opcion == 3:
        continent =  input("Escribe el nombre del continente a consultar: ").title()
        region = population_region(data, continent)
        continent_countries, continent_area = get_continent_area(region, continent)
        generate_pie_chart(continent_countries,continent_area, continent)

    #4.- Seleccionar continente y graficar por territorio
    elif opcion == 4:
        continent =  input("Escribe el nombre del continente a consultar: ").title()
        region = population_region(data, continent)
        continent_countries, continent_population = get_continent_population(region, continent)
        #generate_pie_chart(continent_countries, continent_population, continent)
        tree_map_chart(continent_countries, continent_population, continent)

    #5.- Funcion especial: Treemap Poblacion Mundial
    elif opcion == 5:    
        df = pd.read_csv('world_population.csv', sep=',')
        fig = px.treemap(data_frame=df, path=[px.Constant("World Population"), "Continent" ,"Country/Territory"], values="World Population Percentage")
        fig.update_traces(root_color="lightgrey")
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        fig.show()

    elif opcion == 0:
        print("\nHas decidido salir.")

    
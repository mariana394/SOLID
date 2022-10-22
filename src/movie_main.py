from movie_getinfo import Movies_data
from movie_fetcher import Data
from movie_export import Data_Export

def main():
    # URL to download imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'

    #Creamos objeto para recibir la informacion de un url y pasarla a variables
    data_info = Movies_data()
    data_info.data_movie_info(url)

    #creamos un objeto para llenar los registros de las columnas con la info correspondientre

    data_load = Data(data_info)
    data_load.data_format()

    #creamos el objeto para exportarlo a CSV
    data_export = Data_Export(data_load.data)
    data_export.TO_CSV()

if __name__ == '__main__':
    main()
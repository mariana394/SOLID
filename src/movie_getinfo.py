import requests
from bs4 import BeautifulSoup

#obtener la informacion de las peliculas y traducir de la pagina a variables
class Movies_data:
#inicializar
    def __init__(self):
        self.movies = None
        self.links = None
        self.crew = None
        self.ratings = None
        self.votes = None
    
    #Metodo para obtener la informacion de la pagina y traducirla a variables
    def data_movie_info(self,url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        self.movies = soup.select('td.titleColumn')
        self.links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        self.crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        self.ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        self.votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

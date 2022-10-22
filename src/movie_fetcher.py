import re

#En esta clase lo que queremos hacer es llenar los registros que obtuvimos del URL
class Data:

    def __init__(self, data_info):
        self.data_info = data_info
        self.data = None

#Metodo para darle formato a la informacion. Organizarla y limpiarla. 
    def data_format(self):
   
        # create a empty list for storing
        # movie information
        list = []

        # Iterating over movies to extract
        # each movie's details
        for index in range(0, len(self.data_info.movies)):
        # Separating movie into: 'place',
        # 'title', 'year'
            movie_string = self.data_info.movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": self.data_info.crew[index],
                "rating": self.data_info.ratings[index],
                "vote": self.data_info.votes[index],
                "link": self.data_info.links[index],
                "preference_key": index % 4 + 1}
            list.append(data)
        self.data = list


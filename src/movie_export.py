import csv

# En esta clase se puede poner metodos para diferentes formatos
class Data_Export:
    
    def __init__(self, data: list):
        self.data = data
    
    def TO_CSV(self):
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in self.data:
                writer.writerow({**movie})

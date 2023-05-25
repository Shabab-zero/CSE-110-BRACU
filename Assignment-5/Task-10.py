# Task-10

given_dictionary = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure':9}
most_sold_genre = list(given_dictionary.keys())[0]

for genre in given_dictionary.keys():
    if given_dictionary[genre] > given_dictionary[most_sold_genre]:
        most_sold_genre = genre

print(f"The highest selling book genre is '{most_sold_genre}' and the number of books sold are {given_dictionary[most_sold_genre]}")
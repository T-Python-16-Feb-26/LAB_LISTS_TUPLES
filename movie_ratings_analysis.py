movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def filter_movies(movies: list) -> list:

    filtered_movies =[]

    for movie in movies:
        title, year, ratings = movie
        average_rating = sum(ratings) / len(ratings)
        if average_rating >= 6:
            filtered_movies.append((title, year, average_rating))
    
    filtered_movies.sort(key=lambda filtered_movie: filtered_movie[2], reverse=True)

    for index, movie in enumerate(filtered_movies, start=1):
        title, year, average_rating = movie
        print(f"{index}. {title} ({year}) - Average Rating: {average_rating:.2f} ★")

    return filtered_movies
    
filter_movies(movies)
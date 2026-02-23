movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
    
]

filtered_movies = []

for movie in movies:
    title, year, ratings = movie
    average_rating = round(sum(ratings) / len(ratings), 2)

    if average_rating >= 6.0:
        filtered_movies.append((title, year, average_rating))

sorted_movies = sorted(filtered_movies, key=lambda movie: movie[2], reverse=True)

for title, year, avg in sorted_movies:
    print(f"{title} ({year}) - Average Rating: {avg} *")
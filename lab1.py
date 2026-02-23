
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

movies.sort(key=lambda x: sum(x[2])/len(x[2]), reverse=True)

counter = 1
for movie_title, movie_year, movie_rating in movies:
    avg = sum(movie_rating) / len(movie_rating)

    if avg >= 6.0:
        print(f"{counter} . {movie_title} ({movie_year}) - Average rating: {avg:.2f}")
        counter += 1


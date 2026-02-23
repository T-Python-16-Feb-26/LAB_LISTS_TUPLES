movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

good_movies = list()
for movie in movies:
    total_rating = 0
    for rating in movie[2]:
        total_rating += rating
    average_rating = total_rating / len(movie[2])
        
    if average_rating >= 6:
        good_movies.append((movie[0],movie[1],round(average_rating,2)))

for index,movie in enumerate(good_movies,start=1):
    print(f"{index}. {movie[0]} {movie[1]} - Average Rating: {movie[2]} ★")    
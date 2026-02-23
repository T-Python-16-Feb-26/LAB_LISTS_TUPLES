movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

highly_rated_movies = []
#counter = 1
for movie in movies:
    avg_rating = sum(movie[2]) / len(movie[2])
    if avg_rating >= 6:
        #print(f"{counter}. {movie[0]} ({movie[1]}) - Avergae rating: {avg_rating:.2f} ★")  
        highly_rated_movies.append([movie[0], movie[1], format(avg_rating, '.2f')])
        #counter += 1
#print("---------------------------")
highly_rated_movies.sort(key=lambda x: x[2], reverse=True)
#highly_rated_movies = sorted(highly_rated_movies, key=lambda x: x[2], reverse=True)
counter = 1
for movie in highly_rated_movies:
    print(f"{counter}. {movie[0]} ({movie[1]}) - Avergae rating: {movie[2]} ★") 
    counter += 1

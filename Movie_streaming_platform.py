#Movie Streaming platform
'''
This program:
1- Takes a list of movies.
2- Calculates the average rating for each movie.
3- Keeps only movies with average rating 6 or higher.
4- Sorts movies from highest to lowest rating.
5- Prints the movie title, year, and average rating.
'''
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])]

result = []

for movie in movies:
    avg = sum(movie[2]) / len(movie[2])

    if avg >= 6:
        result.append((movie[0], movie[1], avg))

        result.sort(key=lambda x: x[2], reverse = True)

for i in range(len(result)):
    print(f"{i+1}. {result[i][0]} ({result[i][1]}) - Average rating: {result[i][2]:.2f} ★")
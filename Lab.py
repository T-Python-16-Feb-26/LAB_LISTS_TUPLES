movies =[
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
def Movies(movies: list)->list:
    Top_movies = []
    for movie in movies:
        title , year , ratings = movie
        average_rating = round(sum(ratings)/len(ratings),2)
        if average_rating > 6.0:
            Top_movies.append((title,year,average_rating))
    # we use the sort because we want to display the movies with the highest average rating first
    Top_movies.sort(reverse=True)
        
    for index, movie in enumerate(Top_movies):
        title, year, average_rating = movie
        print(f"{index+1}. {title} ({year}) - Average rating: {average_rating} ★")
    return Top_movies

Movies(movies)


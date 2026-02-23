def movie_rating(movies:list):
    for movie in movies:
        
        title=movie[0]
        year=movie[1]
        ratings=movie[2]

        total=0
        count=0


        for rating in ratings:
            total+=rating
            count+=1


        avg=total/count

        if avg >=6.0:
             print(f"{title} ({year}) - avg rate {round(avg,2)}")


movies = [
    ("The Shawshank Redemption", 1994, [10, 9, 10, 9, 8]),
    ("The Godfather", 1972, [10, 9, 9, 8, 8]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 9]),
    ("The Dark Knight", 2008, [9, 9, 8, 10, 8]),
    ("Schindler's List", 1993, [10, 9, 9, 8, 9]),
    ("The Room", 2003, [1, 2, 3, 2, 1])
]

movie_rating(movies)

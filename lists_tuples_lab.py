
def movie_rating():
    
    movies = [ 

    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
    

    for score in movies:
        movie_name = score[0]
        realese_date = score[1]
        rating_of_movie = score[2]

        calculate_avrage = sum(rating_of_movie)/ len(rating_of_movie)

        
        print(f"Movie name:{ movie_name}, Release date:{ realese_date}, Movie rating: { calculate_avrage: .2}")

movie_rating()    


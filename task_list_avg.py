
def filter_movies(movies: tuple) -> float:
    for movie in movies:
        #print(movie[-1][::])
        (*sum,) = movie[-1][::]
        #print(f"this is the sum {sum}")
        total = 0
        for i in sum:
            total += i
        avg = total / len(sum)
        #avg = avg * 10
        avg = round(avg, 2)
        #print(avg)
        
        #return section:
        if avg >= 6.0:
            print(f"{movie[0]} ({movie[1]}) - Average rating: {avg} ★")
            
        


movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

filter_movies(movies)
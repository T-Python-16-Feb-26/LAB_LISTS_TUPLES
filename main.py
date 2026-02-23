movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def user_rate():
    for i, movie_name in enumerate(movies, start=1):
        print(f"{i}-{movie_name[0]}")
    pick_movie = int(input("pick you movie to rate: "))
    pick_movie -= 1
    if 0 <= pick_movie < len(movies):
        select_movie = movies[pick_movie]
        movie_rates = select_movie[2]
        user_rate = int(input("Enter Your rate: "))
        if user_rate > 10:
            print("rate should be only from 1 to 10")
        else:
            movie_rates.append(user_rate)
            print("Your rate has been add it ")
    else:
        print("Not found")

def movies_lists():
    for i, movie_name in enumerate(movies, start=1):
        avg_rate = sum(movie_name[2]) / len(movie_name[2])
        if avg_rate >= 6.0:
            print(f"{i}-{movie_name[0]} ({movie_name[1]}) - Average rating: {round(avg_rate,2)}")

user_pick = None
while user_pick != 3:
    print("1- movies list")
    print("2- rate a movie")
    print("3- exit")
    user_pick = int(input("Pick: "))
    if user_pick == 1:
        movies_lists()
    elif user_pick == 2:
        user_rate()
    else:
        print("Thank You :)")

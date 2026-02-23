movie_list= [
    ("Training Day", 2001, [9, 10, 8, 9, 10, 9]),
    ("Man on Fire", 2004, [8, 9, 7, 8, 9, 8]),
    ("The Equalizer", 2014, [7, 8, 8, 7, 8, 7]),
    ("Remember the Titans", 2000, [9, 8, 9, 10, 9, 8])
]
for index ,movie in enumerate(movie_list,start=1):
    Movie_Name = movie[0]
    Year = movie[1]
    rating_number = movie[2]

    average = sum(rating_number) / len(rating_number)

    if average >= 6:
        print(f"{Movie_Name} ({Year}) - Average rating: {average:.2f} ★")


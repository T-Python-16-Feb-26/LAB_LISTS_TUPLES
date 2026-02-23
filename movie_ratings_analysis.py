"""
movies_database: a list that stores each movie as a tuple
Each tuple contains:
  - movie title (str)
  - release year (int)
  - a list of user ratings (list of ints/floats)
Note: The tuple itself is immutable (cannot add/remove elements),
but the list containing all movie tuples is mutable (you can add/remove movies).

"""
movies_database = [  
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


def get_high_rated_movies(movies_database):   
    """
    Calculates and returns movies with average rating >= 6

    This function takes a list of movies (each movie is a tuple containing
    the movie title, release year, and a list of user ratings), computes
    the average rating for each movie, and filters out movies with an
    average rating less than 6

    Args:
        movies_database (list of tuples): Each tuple contains
            - title (str): The movie title
            - year (int): The release year
            - ratings (list of int/float): List of user ratings

    Returns:
        list of tuples: Each tuple contains
            - title (str): The movie title
            - year (int): The release year
            - avg (float): The average rating of the movie
    """
    results = []  
    for title, year, ratings in movies_database:  
        count = len(ratings)        
        total = sum(ratings)       
        avg = total / count         
        
        if avg >= 6:               
            results.append((title, year, avg))  
    
    return results

sort_results = get_high_rated_movies(movies_database) 

# Sort the movies from highest to lowest average rating 
sort_results.sort(key=lambda x: x[2], reverse=True)

# Print each movie's title, release year, and average rating,
# using enumerate to automatically add the rank number
for rank, (title, year, avg) in enumerate(sort_results, start=1):
    print(f"{rank}. {title} ({year}) - Average rating: {avg:.2f} ✰")
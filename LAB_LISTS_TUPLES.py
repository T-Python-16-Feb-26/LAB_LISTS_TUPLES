'''Scenario:
You have just been hired as a data analyst at a movie streaming platform. Your manager has given you a list of movies, each with a tuple containing the movie title, release year, and user ratings. The platform allows users to rate movies on a scale of 1 to 10. Your manager wants you to create a Python program that:

1. Accepts a list of movies, with each movie represented as a tuple containing the movie title, release year, and a list of user ratings.
2. Calculates the average rating for each movie.
3. Filters out movies with an average rating lower than 6.0.
5. Displays the  movies, along with their title, release year, and average rating.

Example input:
```
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
```

Expected output:
```
1. The Shawshank Redemption (1994) - Avergae rating: 9.17 ★
2. The Godfather (1972) - Avergae rating: 8.83 ★
3. The Dark Knight (2008) - Avergae rating: 8.83 ★
4. Schindler's List (1993) - Avergae rating: 7.83 ★
5. Pulp Fiction (1994) - Avergae rating: 7.17 ★'''

movies = [
     ("The Room", 2003, [1, 2, 3, 4, 5, 1]),
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    
]
x = []
cunter = 1
for movie in ( movies ):
     title , years , ratings = movie 
     average = sum(ratings)/len(ratings)
     if average >= 6:
        sort = [title , years,average]
        x.append(sort)
        #print (str( cunter) + ".", title , '('+str(years)+')' , '-',format(average,'.3'), '★')
        #cunter +=1
          

x =sorted (x , key=lambda f : f[2] , reverse=True) 
q = 1
for k in x :
    print (str( q) + ".", k[0] , '('+str (k[1])+')' , '-',format(k [2],'.3'), '★')
    q +=1


          


   
        

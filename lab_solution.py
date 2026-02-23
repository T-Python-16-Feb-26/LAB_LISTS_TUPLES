movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

for i,(title,year,rating) in enumerate(sorted(
        movies,
        key=lambda x: sum(x[2])/len(x[2]),
        reverse=True),1):
  average=round(sum(rating)/len(rating),2)
  if average< 6:
    continue
  
  print(f"{i}- {title} ({year}) - Avergae rating: {average} ★")
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
# مصفوفه فاضيه عشان اضيف فيها العناصر الجديدة
results = []

# حساب المتوسط + الفلترة
for title, release_year, user_ratings in movies:
    average = sum(user_ratings) / len(user_ratings)
    if average >= 6.0:
        results.append((title, release_year, average))

# عرض النتائج بالشكل المطلوب
for i, (title, release_year, average) in enumerate(results, start=1):
    print(f"{i}. {title} ({release_year}) - Average rating: {average:.2f} ★")

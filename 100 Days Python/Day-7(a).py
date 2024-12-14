"""
This program manages a collection of movies using OOP principles.
It demonstrates:
- Creating a Movie class with attributes like title, director, and year
- Using methods to display details about a movie
- Managing a collection of movie objects with user interaction
"""

# Define a class to represent a Movie
class Movie:
    # Constructor to initialize movie attributes
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
        print(f"Movie '{self.title}' by {self.director} ({self.year}) has been added.")

    # Method to display movie details
    def display_details(self):
        print(f"Title: {self.title}\nDirector: {self.director}\nYear: {self.year}")

    # Destructor to clean up resources
    def __del__(self):
        print(f"Movie '{self.title}' is being removed from the collection.")

#######################################
# Main Program: Interact with the user
#######################################

print("Welcome to the Movie Manager!")
num_movies = int(input("How many movies would you like to add? "))
movie_collection = []

for i in range(num_movies):
    print(f"\nEnter details for Movie {i + 1}:")
    title = input("Title: ")
    director = input("Director: ")
    year = int(input("Year of Release: "))
    movie_collection.append(Movie(title, director, year))

# Display details of all movies
print("\nYour Movie Collection:")
for i, movie in enumerate(movie_collection, 1):
    print(f"\nMovie {i}:")
    movie.display_details()

# Cleanup: Deleting all movies
print("\nClearing the movie collection...")
while movie_collection:
    del movie_collection[0]

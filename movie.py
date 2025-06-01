class Movie:
    def __init__(self, movie_id, title, director, year, genre):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
    
    def __str__(self):
        return (f"ID: {self.movie_id}, Title: {self.title}, Director: {self.director}, "
                f"Year: {self.year}, Genre: {self.genre}")

class MovieCollection:
    def __init__(self):
        self.movies = {}
    
    def add_movie(self, movie):
        if movie.movie_id in self.movies:
            return False
        self.movies[movie.movie_id] = movie
        return True
    
    def get_all_movies(self):
        return list(self.movies.values())
    
    def search_by_title(self, title):
        return [movie for movie in self.movies.values() if title.lower() in movie.title.lower()]
    
    def update_movie(self, movie_id, **kwargs):
        if movie_id not in self.movies:
            return False
        
        movie = self.movies[movie_id]
        for key, value in kwargs.items():
            if hasattr(movie, key):
                setattr(movie, key, value)
        return True
    
    def delete_movie(self, movie_id):
        if movie_id not in self.movies:
            return False
        del self.movies[movie_id]
        return True

def display_menu():
    print("\nMovie Collection Manager")
    print("1. Add a new movie")
    print("2. View all movies")
    print("3. Search movies by title")
    print("4. Update a movie")
    print("5. Delete a movie")
    print("6. Exit")

def get_valid_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            if input_type == int:
                return int(user_input)
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def add_movie_ui(collection):
    print("\nAdd a New Movie")
    movie_id = get_valid_input("Enter movie ID: ")
    
    # Check if movie ID already exists
    if movie_id in collection.movies:
        print("Error: A movie with this ID already exists.")
        return
    
    title = get_valid_input("Enter movie title: ")
    director = get_valid_input("Enter director name: ")
    year = get_valid_input("Enter release year: ", int)
    genre = get_valid_input("Enter genre: ")
    
    new_movie = Movie(movie_id, title, director, year, genre)
    if collection.add_movie(new_movie):
        print("Movie added successfully!")
    else:
        print("Error adding movie.")

def view_movies_ui(collection):
    print("\nAll Movies in Collection")
    movies = collection.get_all_movies()
    if not movies:
        print("No movies in the collection.")
    else:
        for movie in movies:
            print(movie)

def search_movies_ui(collection):
    print("\nSearch Movies by Title")
    search_term = get_valid_input("Enter title to search: ")
    results = collection.search_by_title(search_term)
    
    if not results:
        print("No movies found matching your search.")
    else:
        print(f"Found {len(results)} matching movies:")
        for movie in results:
            print(movie)

def update_movie_ui(collection):
    print("\nUpdate Movie Information")
    movie_id = get_valid_input("Enter movie ID to update: ")
    
    if movie_id not in collection.movies:
        print("Error: No movie found with this ID.")
        return
    
    print("Current movie information:")
    print(collection.movies[movie_id])
    
    print("\nEnter new information (leave blank to keep current value):")
    title = input(f"New title [{collection.movies[movie_id].title}]: ") or collection.movies[movie_id].title
    director = input(f"New director [{collection.movies[movie_id].director}]: ") or collection.movies[movie_id].director
    
    while True:
        year_input = input(f"New year [{collection.movies[movie_id].year}]: ")
        if not year_input:
            year = collection.movies[movie_id].year
            break
        try:
            year = int(year_input)
            break
        except ValueError:
            print("Please enter a valid year.")
    
    genre = input(f"New genre [{collection.movies[movie_id].genre}]: ") or collection.movies[movie_id].genre
    
    if collection.update_movie(movie_id, title=title, director=director, year=year, genre=genre):
        print("Movie updated successfully!")
    else:
        print("Error updating movie.")

def delete_movie_ui(collection):
    print("\nDelete a Movie")
    movie_id = get_valid_input("Enter movie ID to delete: ")
    
    if collection.delete_movie(movie_id):
        print("Movie deleted successfully!")
    else:
        print("Error: No movie found with this ID.")

def main():
    collection = MovieCollection()
    
    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-6): ", int)
        
        if choice == 1:
            add_movie_ui(collection)
        elif choice == 2:
            view_movies_ui(collection)
        elif choice == 3:
            search_movies_ui(collection)
        elif choice == 4:
            update_movie_ui(collection)
        elif choice == 5:
            delete_movie_ui(collection)
        elif choice == 6:
            print("Exiting the Movie Collection Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
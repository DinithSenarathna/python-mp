# Movie Collection Manager - README

## Overview

A Python command-line application for managing a collection of movies. This program allows users to add, view, search, update, and delete movie entries with proper validation and error handling.

## Features

- **Add Movies**: Store movie details including title, director, release year, genre, and unique ID
- **View All**: Display all movies in the collection
- **Search**: Find movies by title (case-insensitive partial matching)
- **Update**: Modify existing movie information
- **Delete**: Remove movies from the collection
- **Validation**: Ensures unique IDs, correct data types, and existence checks

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DinithSenarathna/movie-collection-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-collection-manager
   ```

## Usage

Run the program with Python:
```bash
python movie_manager.py
```

Follow the on-screen menu to perform operations:

1. **Add a new movie**: Enter movie details with unique ID
2. **View all movies**: Display all movies in the collection
3. **Search movies by title**: Find movies containing your search term
4. **Update a movie**: Modify existing movie information
5. **Delete a movie**: Remove a movie by its ID
6. **Exit**: Quit the program

## File Structure

```
movie-collection-manager/
├── movie_manager.py      # Main program file
├── README.md             # This documentation
└── LICENSE               # License file (optional)
```

## Notes

- All data is stored in memory and will be lost when the program exits
- No external database or file storage is used (as per project requirements)

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## License

[MIT License](LICENSE) (or specify your preferred license)

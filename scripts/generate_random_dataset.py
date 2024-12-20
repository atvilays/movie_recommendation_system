import pandas as pd
import random

# Generate a random movie dataset
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Sci-Fi', 'Adventure', 'Animation', 'Fantasy']
movies = []

for i in range(1, 101):  # 100 movies
    movie = {
        'title': f'Movie {i}',
        'genre': random.choice(genres),
        'vote_average': round(random.uniform(1.0, 10.0), 1),
        'vote_count': random.randint(50, 2000),
        'release_year': random.randint(2000, 2023)
    }
    movies.append(movie)

# Convert to a DataFrame
movies_df = pd.DataFrame(movies)

# Save to the data folder
movies_df.to_csv("data/random_movies_dataset.csv", index=False)
print("Random movie dataset saved to data/random_movies_dataset.csv!")

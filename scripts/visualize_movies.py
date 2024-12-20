import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv("data/cleaned_movies_dataset.csv")

# Visualization 1: Number of Movies by Genre
genre_counts = data["genre"].value_counts()
plt.figure(figsize=(10, 6))
genre_counts.plot(kind="bar", color="skyblue")
plt.title("Number of Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/movies_by_genre.png")
plt.show()

# Visualization 2: Average Ratings by Genre
avg_ratings = data.groupby("genre")["vote_average"].mean()
plt.figure(figsize=(10, 6))
avg_ratings.plot(kind="bar", color="orange")
plt.title("Average Ratings by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/average_ratings_by_genre.png")
plt.show()

# Visualization 3: Movies Released Over Time
movies_per_year = data["release_year"].value_counts().sort_index()
plt.figure(figsize=(12, 6))
movies_per_year.plot(kind="line", marker="o", color="green")
plt.title("Number of Movies Released Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/movies_over_time.png")
plt.show()

print("Visualizations saved in the outputs folder!")

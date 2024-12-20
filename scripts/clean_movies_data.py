import pandas as pd

# Load the dataset
data = pd.read_csv("data/random_movies_dataset.csv")

# Drop duplicates
data.drop_duplicates(inplace=True)

# Ensure vote_average is between 1.0 and 10.0
data = data[(data["vote_average"] >= 1.0) & (data["vote_average"] <= 10.0)]

# Fill missing genres with "Unknown"
data["genre"] = data["genre"].fillna("Unknown")

# Save the cleaned data
data.to_csv("data/cleaned_movies_dataset.csv", index=False)

print("Data cleaning complete! Cleaned data saved to data/cleaned_movies_dataset.csv.")

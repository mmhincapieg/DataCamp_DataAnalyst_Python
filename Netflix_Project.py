import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# print(netflix_df.sample(10))

# Selecting Movies from the Netflix Record ----------------------

movies_df = netflix_df.loc[netflix_df["type"] == "Movie", ["title","type",
                                                           "duration", "release_year", "genre"]]
# print(movies_df)

# Ensure 'release_year' is integer type
movies_df["release_year"] = pd.to_numeric(movies_df["release_year"], errors='coerce')

# Filter for movies released in the 1990s (1990-1999)
movies1990_df = movies_df.loc[
    (movies_df["release_year"] >= 1990) & (movies_df["release_year"] < 2000),
    ["title", "duration", "genre", "release_year"]]

print(movies1990_df)

duration = int(movies1990_df["duration"].mode()[0])

duration_values = movies1990_df["duration"]

# Compute histogram data
counts, bins, patches = plt.hist(duration_values, bins=30, edgecolor='black')

# Normalize counts for colormap
norm = plt.Normalize(counts.min(), counts.max())
cmap = plt.cm.viridis

# Color each bar according to its height (darker in the middle where counts are higher)
for count, patch in zip(counts, patches):
    color = cmap(norm(count))
    patch.set_facecolor(color)

plt.title("Movie Duration Distribution")
plt.xlabel("Movie Duration")
plt.ylabel("Number of Movies (1990s)")
plt.show()

action_movies = movies1990_df[(movies1990_df["genre"] == "Action")]

#print(action_movies)

short_movie_count = (action_movies["duration"] < 90).sum()


print(short_movie_count)
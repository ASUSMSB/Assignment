import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Step 1: Importing the dataset
# Assume the dataset is in CSV format with two files: "movies.csv" and "ratings.csv"
movies_df = pd.read_csv('movies.csv')  # Movies dataset with columns like 'movieId', 'title', 'genre'
ratings_df = pd.read_csv('ratings.csv')  # User ratings dataset with columns like 'userId', 'movieId', 'rating'

# Display the first few rows to understand the data
print(movies_df.head())
print(ratings_df.head())

# Step 2: Exploratory Data Analysis (EDA)
## Check for missing values
print("\nMissing values in movies dataset:")
print(movies_df.isnull().sum())
print("\nMissing values in ratings dataset:")
print(ratings_df.isnull().sum())

# Handle missing data
# In this case, we'll drop any rows with missing values for simplicity
movies_df = movies_df.dropna()
ratings_df = ratings_df.dropna()

# Alternatively, you could use imputation for missing values
# movies_df['genre'].fillna('Unknown', inplace=True)

# Clean the movie titles: remove special characters (if any)
movies_df['title'] = movies_df['title'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

# Normalize genres by splitting them into individual genres
# This can help with content-based filtering later
movies_df['genres'] = movies_df['genre'].apply(lambda x: x.split('|'))

# Step 3: Create User-Item Rating Matrix for Collaborative Filtering
# Pivot the ratings data to create a user-item matrix
user_item_matrix = ratings_df.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Display the user-item matrix
print("\nUser-Item Rating Matrix:")
print(user_item_matrix.head())

# Visualize the user-item matrix using a heatmap
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.heatmap(user_item_matrix, cmap='Blues', cbar=True, linewidths=0.1)
plt.title("User-Item Rating Matrix Heatmap")
plt.show()

# OPTIONAL: Label Encoding for User and Movie IDs
# If needed, we can encode movie and user IDs for collaborative filtering models
movie_encoder = LabelEncoder()
ratings_df['movieId_encoded'] = movie_encoder.fit_transform(ratings_df['movieId'])

user_encoder = LabelEncoder()
ratings_df['userId_encoded'] = user_encoder.fit_transform(ratings_df['userId'])

# Display the transformed ratings dataset
print("\nEncoded ratings data:")
print(ratings_df.head())

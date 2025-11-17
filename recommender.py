import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from quantum_model import quantum_similarity

# Real-world dataset auto-download
URL_RATINGS = "https://files.grouplens.org/datasets/movielens/ml-latest-small/ratings.csv"
URL_MOVIES = "https://files.grouplens.org/datasets/movielens/ml-latest-small/movies.csv"

ratings = pd.read_csv(URL_RATINGS)
movies = pd.read_csv(URL_MOVIES)
df = ratings.merge(movies, on="movieId")

# Genre embedding
genre_dummies = df['genres'].str.get_dummies(sep='|')
df = pd.concat([df, genre_dummies], axis=1)

def recommend_movies(user_id, top_k=10):
    user_data = df[df['userId'] == user_id]
    if user_data.empty:
        return pd.DataFrame()

    # User preference profile based on liked movies
    user_profile = user_data[genre_dummies.columns].mean().values.reshape(1, -1)
    movie_features = df[genre_dummies.columns].values

    # Classical cosine similarity
    df["classical_score"] = cosine_similarity(user_profile, movie_features)[0]

    # Quantum similarity based on top 2 genres: Action, Romance
    q_scores = []
    for _, row in df.iterrows():
        user_vec = user_profile[0][:2]  # Action, Romance
        movie_vec = row[genre_dummies.columns[:2]].values
        q_scores.append(quantum_similarity(user_vec, movie_vec))

    df["quantum_score"] = q_scores

    # Hybrid score
    df["final_score"] = 0.7 * df["classical_score"] + 0.3 * df["quantum_score"]

    return df.sort_values("final_score", ascending=False).head(top_k)[["title", "final_score"]]

import numpy as np
import pandas as pd
from surprise import Dataset, SVD
from surprise.model_selection import train_test_split

from quantum_model import quantum_similarity

# Load dataset
data = Dataset.load_builtin('ml-100k')
trainset, testset = train_test_split(data, test_size=0.2)

# Train classical recommender (Matrix Factorization)
algo = SVD()
algo.fit(trainset)


def get_user_preferences(user_id):
    """Returns top-rated movies for baseline similarity"""
    user_ratings = pd.DataFrame(trainset.ur[user_id], columns=["movie_id", "rating"])
    user_ratings["rating"] = user_ratings["rating"].astype(float)
    return user_ratings.sort_values("rating", ascending=False).head(5)


def recommend_movies(user_id, top_k=10):
    all_items = list(set([i for i in trainset.all_items()]))
    movie_scores = []

    # Try predicting each movie for the user (cold start handled later)
    for movie_inner_id in all_items:
        movie_raw_id = trainset.to_raw_iid(movie_inner_id)
        est_rating = algo.predict(trainset.to_raw_uid(user_id), movie_raw_id).est

        # Latent factors as features for quantum similarity
        try:
            user_vec = algo.pu[user_id][:2]   # 2D latent features
            movie_vec = algo.qi[movie_inner_id][:2]
        except:
            continue  # skip if missing

        q_score = quantum_similarity(user_vec, movie_vec)
        hybrid_score = 0.7 * est_rating + 0.3 * q_score

        movie_scores.append((movie_raw_id, est_rating, q_score, hybrid_score))

    # Sort by hybrid score
    sorted_list = sorted(movie_scores, key=lambda x: x[3], reverse=True)
    return sorted_list[:top_k]

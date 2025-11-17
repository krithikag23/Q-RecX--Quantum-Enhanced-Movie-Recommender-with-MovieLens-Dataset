import streamlit as st
from recommender import recommend_movies

st.title("🎬 Q-RecX — Quantum Movie Recommender")

user_id = st.number_input("Enter User ID (0–943)", min_value=0, max_value=943, value=50)

if st.button("Recommend"):
    recs = recommend_movies(user_id)
    st.subheader("Top Picks For You")

    for movie_id, est, qscore, final in recs:
        st.markdown(f"**Movie ID: {movie_id}** ⭐Pred:{est:.2f} ⚛️Q:{qscore:.2f} 🔥Hybrid:{final:.2f}")

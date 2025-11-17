import streamlit as st
from recommender import recommend_movies

st.title("🎬 Quantum Movie Recommender ⚛️")

Action = st.slider("Action Preference", 0, 10, 6)
Romance = st.slider("Romance Preference", 0, 10, 5)

if st.button("Recommend"):
    prefs = {"Action": Action, "Romance": Romance}
    st.write("### 🔥 Top Recommendations")
    st.dataframe(recommend_movies(prefs))
else:
    st.info("Adjust sliders and click Recommend!")

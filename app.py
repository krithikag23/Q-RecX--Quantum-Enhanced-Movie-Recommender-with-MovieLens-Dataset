import streamlit as st
from recommender import recommend_movies

st.set_page_config(page_title="Quantum Movie Recommender", page_icon="🎬")

st.title("🎬 Quantum Movie Recommender")
st.caption("Hybrid classical + quantum similarity for smarter movie suggestions ⚛️")

user_id = st.number_input("Enter User ID (1–600)", min_value=1, max_value=600, value=10)

if st.button("🔍 Recommend Movies"):
    recs = recommend_movies(user_id)
    if recs.empty:
        st.error("No data found for this user. Try another!")
    else:
        st.dataframe(recs.style.format({"final_score": "{:.3f}"}))
else:
    st.info("Enter a User ID and click Recommend!")

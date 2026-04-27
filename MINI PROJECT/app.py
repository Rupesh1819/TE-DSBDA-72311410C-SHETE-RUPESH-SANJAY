import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

# ── Config ────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_resource
def load_data():
    with open(BASE_DIR / "movie_dict.pkl", "rb") as f:
        movies = pd.DataFrame(pickle.load(f))
    with open(BASE_DIR / "similarity.pkl", "rb") as f:
        similarity = pickle.load(f)
    return movies, similarity

movies, similarity = load_data()

# ── Recommend function ────────────────────────────────────────────────────────
def recommend(movie):
    idx = movies[movies["title"] == movie].index[0]
    distances = sorted(enumerate(similarity[idx]), key=lambda x: x[1], reverse=True)
    return [movies.iloc[i[0]].title for i, _ in zip(distances[1:6], range(5))]

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("🎬 Movie Recommender System")
st.write("Select a movie and get 5 similar movie recommendations.")

st.divider()

selected = st.selectbox(
    "Choose a Movie",
    sorted(movies["title"].dropna().unique().tolist()),
)

if st.button("Get Recommendations", type="primary"):
    recommendations = recommend(selected)

    st.divider()
    st.subheader(f"Movies similar to **{selected}**:")

    for i, name in enumerate(recommendations, start=1):
        st.write(f"**{i}.** {name}")

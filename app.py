import streamlit as st
import pandas as pd
import pickle
import requests
import gdown
import time

API_KEY = "e0f75588cfc093e37d64ad3851a696ad"

# ---------------- Safe TMDB request ----------------
def safe_request(url, retries=2, delay=1):
    for _ in range(retries):
        try:
            return requests.get(url, timeout=5).json()
        except:
            time.sleep(delay)
    return {}

# ---------------- Poster fetch with caching ----------------
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id, title):
    # Try by movie_id first
    if movie_id:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = safe_request(url)
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

    # Fallback: search by title
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    data = safe_request(search_url)
    if data.get("results") and data["results"][0].get("poster_path"):
        return "https://image.tmdb.org/t/p/w500/" + data["results"][0]["poster_path"]

    # Final fallback: placeholder
    return "https://via.placeholder.com/500x750?text=No+Poster"

# ---------------- Load similarity.pkl from Google Drive ----------------
SIMILARITY_URL = "https://drive.google.com/uc?id=14tlswXt4BiGHE7RhhRvpfRIGxDVRt4OE"

@st.cache_data
def load_similarity(url):
    output = "similarity.pkl"
    gdown.download(url, output, quiet=True)
    with open(output, "rb") as f:
        similarity = pickle.load(f)
    return similarity

similarity = load_similarity(SIMILARITY_URL)

# ---------------- Load local movie_dict.pkl ----------------
movies = pd.DataFrame(pickle.load(open('movie_dict.pkl','rb')))

# ---------------- Recommendation function ----------------
def recommend(movie):
    try:
        idx = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.warning("Movie not found!")
        return [], []

    distances = similarity[idx]
    top_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended = [(movies.iloc[i[0]]['title'], movies.iloc[i[0]].get('movie_id')) for i in top_indices]
    recommended_titles = [t[0] for t in recommended]
    recommended_posters = [fetch_poster(t[1], t[0]) for t in recommended]

    return recommended_titles, recommended_posters

# ---------------- Streamlit App ------------------
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    if names:
        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            col.text(name[:30])  # truncate long titles
            col.image(poster)

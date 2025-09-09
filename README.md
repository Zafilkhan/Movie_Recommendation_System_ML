# 🎬 Movie Recommendation System

This is a **Movie Recommendation System** built with **Machine Learning** and deployed using **Streamlit Cloud**.  
It suggests similar movies based on the movie you select.

---

## 🚀 Features
- Search and select your favorite movie.
- Get **top 5 recommended movies** instantly.
- Fetches **movie posters** using TMDB API.
- Simple and clean **Streamlit UI**.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Requests**

---

## 📂 Project Structure
- ├── app.py # Main Streamlit app
- ├── movies.pkl # Movies data (pickle file)
- ├── similarity.pkl # Similarity matrix
- ├── requirements.txt # Dependencies
- └── README.md # Project documentatio



---

## ▶️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
### 2.Install dependencies:   
  - pip install -r requirements.txt
### 3.Run the Streamlit app:
 - streamlit run app.py



 ### API Key
This project uses the TMDB API for fetching posters.
Add your TMDB API key in Streamlit secrets:
- Streamlit Cloud Secrets (Settings → Secrets)
- API_KEY = "e0f75588cfc093e37d64ad3851a696ad"

### Author
- Zafil Khan
  - Feel free to contribute or raise issues! ⭐





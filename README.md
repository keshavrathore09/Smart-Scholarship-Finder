# Smart-Scholarship-Finder
An intelligent, real-time scholarship matching engine powered by Python, Flask, and Machine Learning.

# 🎓 Smart Scholarship Finder System

An AI-powered web application designed to automatically match students with relevant financial aid opportunities using Natural Language Processing (NLP). 

## 🚀 Features
* **Automated Matching Engine:** Uses TF-IDF vectorization and Cosine Similarity to compare user profiles against scholarship descriptions.
* **Database Management:** Efficiently manages 500+ mock scholarship records using SQLite.
* **Responsive UI:** Clean, intuitive web interface for real-time filtering and deadline tracking.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn (NLP)
* **Database:** SQLite, SQL
* **Frontend:** HTML, CSS

## ⚙️ How to Run Locally

1. **Clone the repository:**
   `git clone <your-repo-link>`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Generate the mock database:**
   `python database.py`
4. **Run the application:**
   `python app.py`
5. Open `http://127.0.0.1:5000` in your browser.

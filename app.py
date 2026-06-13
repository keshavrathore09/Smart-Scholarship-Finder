from flask import Flask, render_template, request
import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# --- 1. Database Function ---
def get_scholarships():
    """Fetches all scholarships from the SQLite database."""
    conn = sqlite3.connect('scholarships.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, description, amount, deadline FROM scholarships')
    rows = cursor.fetchall()
    conn.close()
    
    # Convert database rows into a list of dictionaries for easier use
    scholarships = []
    for row in rows:
        scholarships.append({
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'amount': row[3],
            'deadline': row[4]
        })
    return scholarships

# --- 2. The "AI" Matching Engine ---
def get_top_matches(student_profile, scholarships, top_n=10):
    """Compares student text to scholarship text using NLP and scores them."""
    # Put the student profile first in our list of text documents
    documents = [student_profile]
    
    # Add every scholarship description to the list
    for sch in scholarships:
        combined_text = f"{sch['title']} {sch['description']}"
        documents.append(combined_text)
        
    # Convert all this text into mathematical numbers (TF-IDF mapping)
    # stop_words='english' removes useless words like 'and', 'the', 'is'
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Calculate how similar the student profile (index 0) is to all scholarships
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Attach the percentage score to each scholarship
    for i, sch in enumerate(scholarships):
        sch['match_score'] = round(cosine_similarities[i] * 100)
        
    # Sort them from highest score to lowest score
    scholarships.sort(key=lambda x: x['match_score'], reverse=True)
    
    # Return the top N results that have at least some match
    return [sch for sch in scholarships if sch['match_score'] > 0][:top_n]

# --- 3. The Web Routing ---
@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        # Grab what the user typed into the web form
        major = request.form.get('major')
        skills = request.form.get('skills')
        category = request.form.get('category')
        
        # Build the student's text profile
        student_profile = f"Majoring in {major}. Skills include {skills}. Looking for {category}."
        
        # Fetch data and run the AI match
        all_scholarships = get_scholarships()
        results = get_top_matches(student_profile, all_scholarships)
        
    # Send the data to our HTML page to be displayed
    return render_template('index.html', results=results)

if __name__ == '__main__':
    # debug=True means the server will auto-update if we change code
    app.run(debug=True)
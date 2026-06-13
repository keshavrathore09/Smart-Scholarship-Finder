import sqlite3
import random
from datetime import datetime, timedelta

def create_database():
    # 1. Connect to SQLite database (this creates the file automatically)
    conn = sqlite3.connect('scholarships.db')
    cursor = conn.cursor()

    # 2. Create the table for our scholarships
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scholarships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            amount TEXT,
            deadline DATE
        )
    ''')

    # Clear existing data just in case you run this script multiple times
    cursor.execute('DELETE FROM scholarships')

    # 3. Ingredients to generate realistic mock data
    majors = ['Computer Science', 'Data Science', 'Electrical Engineering', 'Mechanical Engineering', 'General B.Tech', 'Information Technology']
    keywords = ['Merit-based', 'Financial Need', 'Women in Tech', 'Minority', 'Leadership', 'Innovation', 'Research', 'First-Generation']
    skills = ['Python', 'SQL', 'Web Development', 'Machine Learning', 'Cybersecurity', 'Cloud Computing', 'Java', 'C++']
    
    print("Generating 500+ mock scholarship records...")
    
    # 4. Loop to create 525 unique scholarships
    for i in range(1, 526):
        major = random.choice(majors)
        keyword = random.choice(keywords)
        skill = random.choice(skills)
        
        # Build the mock data strings
        title = f"{keyword} Grant for {major}"
        description = f"This scholarship supports students pursuing {major}. Ideal candidates demonstrate excellence in {keyword.lower()} and have strong foundational skills in {skill}. We are looking for passionate individuals ready to impact the tech industry."
        amount = f"${random.randint(10, 150) * 100}" # Random amount between $1,000 and $15,000
        
        # Generate a random deadline between 5 and 180 days from today
        days_ahead = random.randint(5, 180)
        deadline = (datetime.now() + timedelta(days=days_ahead)).strftime('%Y-%m-%d')

        # 5. Insert the record into the database
        cursor.execute('''
            INSERT INTO scholarships (title, description, amount, deadline)
            VALUES (?, ?, ?, ?)
        ''', (title, description, amount, deadline))

    # 6. Save changes and close the connection
    conn.commit()
    conn.close()
    print("Database 'scholarships.db' created successfully with 525 records!")

if __name__ == '__main__':
    create_database()
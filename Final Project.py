#00. Create a new project: "Personality Test".

#01. Identify based on the tastes of movies, music, books and habits.
import random
import time
import os
import csv

print("Welcome to the Personality Test!")
print("Answer the following questions to find out your personality type.\n")
points = 0

# Determine default and proyect CSV paths
script_dir = os.path.dirname(os.path.abspath(__file__))
default_csv = os.path.join(script_dir, 'recommendations.csv')
proyect_dir = os.path.join(script_dir, 'Proyect')
proyect_csv = os.path.join(proyect_dir, 'recommendations.csv')

# Ensure Proyect folder exists
if not os.path.exists(proyect_dir):
    os.makedirs(proyect_dir, exist_ok=True)

# Choose which CSV to use (prefer proyect_csv if present)
if os.path.exists(proyect_csv):
    rec_csv_path = proyect_csv
elif os.path.exists(default_csv):
    rec_csv_path = default_csv
else:
    # Neither CSV exists: create the Proyect CSV with defaults and use it
    with open(proyect_csv, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["personality", "movies", "books", "music"])
        writer.writerow(["adventurous", "Mad Max;Indiana Jones", "Into the Wild;The Alchemist", "AC/DC;The Rolling Stones"])
        writer.writerow(["balanced", "The Intouchables;Forrest Gump", "To Kill a Mockingbird;The Kite Runner", "The Beatles;Coldplay"])
        writer.writerow(["introspective", "Her;Eternal Sunshine of the Spotless Mind", "Norwegian Wood;The Goldfinch", "Radiohead;Sufjan Stevens"])
        writer.writerow(["analytical", "The Imitation Game;A Beautiful Mind", "Sapiens;Thinking, Fast and Slow", "Philip Glass;Ludovico Einaudi"])
    rec_csv_path = proyect_csv

#02. Start with the questions and answers.

#03. Question 1: Movie preferences
print("Question 1: What type of movies do you prefer?")
print ("\n1. Action\n2. Comedy\n3. Drama\n4. Horror")
question1= input("Your choice (1-4): ")

if question1 == "1":
    points += 4
elif question1 == "2":
    points += 3
elif question1 == "3":
    points += 2
elif question1 == "4":
    points += 1

#04. Question 2: Music preferences
print("\nQuestion 2: What type of music do you prefer?")
print("\n1. Rock\n2. Pop\n3. Classical\n4. Jazz")
question2 = input("Your choice (1-4): ")

if question2 == "1":
    points += 4
elif question2 == "2":
    points += 3
elif question2 == "3":
    points += 2
elif question2 == "4":
    points += 1

#05. Question 3: Book preferences
print("\nQuestion 3: What type of books do you prefer?")
print("\n1. Fiction\n2. Non-fiction\n3. Mystery\n4. Fantasy")
question3 = input("Your choice (1-4): ")

if question3 == "1":
    points += 4
elif question3 == "2":
    points += 3
elif question3 == "3":
    points += 2
elif question3 == "4":
    points += 1

#06. Question 4: Daily habits
print("\nQuestion 4: How do you prefer to spend your free time?")
print("\n1. Socializing with friends\n2. Reading a book\n3. Watching TV\n4. Outdoor activities")
question4 = input("Your choice (1-4): ")

if question4 == "1":
    points += 4
elif question4 == "2":
    points += 3
elif question4 == "3":
    points += 2
elif question4 == "4":
    points += 1

#07. Calculate the personality type based on the points.
print("\nCalculating your personality type...")
time.sleep(3)  # Wait for 3 seconds to simulate calculation
print()
# Determine personality key and message
if points >= 14:
    personality_key = "adventurous"
    message = "You are adventurous and spontaneous. You love fun and living to the fullest."
elif 10 <= points < 14:
    personality_key = "balanced"
    message = "You are balanced and thoughtful. You enjoy a mix of social activities and quiet time."
elif 6 <= points < 10:
    personality_key = "introspective"
    message = "You are introspective and creative. You value deep connections and meaningful experiences."
else:
    personality_key = "analytical"
    message = "You are analytical and detail-oriented. You prefer structure and order in your life."

# Print personality message
print(message)

# Load recommendations from CSV and display them
recs = None
try:
    with open(rec_csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('personality', '').strip().lower() == personality_key:
                recs = row
                break
except Exception:
    recs = None

# Fallback/default recommendations (used when CSV can't be read or entry missing)
default_recs = {
    'adventurous': {
        'movies': ['Mad Max', 'Indiana Jones'],
        'books': ['Into the Wild', 'The Alchemist'],
        'music': ['AC/DC', 'The Rolling Stones']
    },
    'balanced': {
        'movies': ['The Intouchables', 'Forrest Gump'],
        'books': ['To Kill a Mockingbird', 'The Kite Runner'],
        'music': ['The Beatles', 'Coldplay']
    },
    'introspective': {
        'movies': ['Her', 'Eternal Sunshine of the Spotless Mind'],
        'books': ['Norwegian Wood', 'The Goldfinch'],
        'music': ['Radiohead', 'Sufjan Stevens']
    },
    'analytical': {
        'movies': ['The Imitation Game', 'A Beautiful Mind'],
        'books': ['Sapiens', 'Thinking, Fast and Slow'],
        'music': ['Philip Glass', 'Ludovico Einaudi']
    }
}

movies = []
books = []
music = []

if recs:
    movies = [m.strip() for m in recs.get('movies', '').split(';') if m.strip()]
    books = [b.strip() for b in recs.get('books', '').split(';') if b.strip()]
    music = [mu.strip() for mu in recs.get('music', '').split(';') if mu.strip()]
else:
    # Use fallback for the determined personality if available
    fallback = default_recs.get(personality_key)
    if fallback:
        movies = fallback.get('movies', [])
        books = fallback.get('books', [])
        music = fallback.get('music', [])

if movies or books or music:
    print("\nRecommended movies:")
    for m in movies:
        print("- ", m)
    print("\nRecommended books:")
    for b in books:
        print("- ", b)
    print("\nRecommended music/artists:")
    for mu in music:
        print("- ", mu)
else:
    print("\nNo recommendations available.")

#08. End of the test.
print("\nThank you for taking the Personality Test!")

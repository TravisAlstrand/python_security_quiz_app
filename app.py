from db import init_db, seed_from_json
from menu import prompt_quiz_options
from models.quiz import Quiz
import os

if __name__ == "__main__":
    print("Initializing database...")
    Session = init_db("quiz.db")
    print("Database initialized 👍")

    json_path = "data/data.json"
    if os.path.exists(json_path):
        print("Seeding database from JSON...")
        seed_from_json(Session, json_path)
        print("Database seeded 👍")
    else:
        print(f"Oops! '{json_path}' not found...")
        print("🚫 Database not seeded")

    quiz_type_selection = prompt_quiz_options()
    print(quiz_type_selection)
    quiz = Quiz(quiz_type_selection, Session)

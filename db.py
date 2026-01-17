from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.quiz_item import QuizItem, Base
import json


def init_db(db_path: str = "quiz.db") -> sessionmaker:
    """Initialize database and return session maker"""
    engine = create_engine(f"sqlite:///{db_path}")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


def seed_from_json(session_maker: sessionmaker, json_path: str) -> None:
    """Seed database from JSON file, clearing existing data"""
    with open(json_path, "r") as json_file:
        data = json.load(json_file)

    session = session_maker()

    # Clear existing data
    session.query(QuizItem).delete()

    # Add acronyms
    for item in data.get("acronyms", []):
        quiz_item = QuizItem({
            "question": item["question"],
            "correct_answer": item["correct_answer"],
            "incorrect_answers": [],
            "quiz_type": "acronym"
        })
        session.add(quiz_item)

    # Add terms
    for item in data.get("terms", []):
        quiz_item = QuizItem({
            "question": item["question"],
            "correct_answer": item["correct_answer"],
            "incorrect_answers": item.get("incorrect_answers", []),
            "quiz_type": "term"
        })
        session.add(quiz_item)

    session.commit()
    session.close()

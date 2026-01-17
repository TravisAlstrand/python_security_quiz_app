from typing import Any
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class QuizItem(Base):
    """SQLAlchemy model for quiz questions"""
    __tablename__ = "quiz_items"

    # Database columns
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    incorrect_answers = Column(JSON)
    quiz_type = Column(String)

    def __init__(self, quiz_item: dict) -> None:
        """Initialize from dictionary"""
        self.question = quiz_item.get("question", "")
        self.correct_answer = quiz_item.get("correct_answer", "")
        self.incorrect_answers = quiz_item.get("incorrect_answers", [])
        self.quiz_type = quiz_item.get("quiz_type", "")

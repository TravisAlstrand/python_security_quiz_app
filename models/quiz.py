from sqlalchemy.orm import Session
from .quiz_item import QuizItem
import random


class Quiz():
    def __init__(self, quiz_options: dict, session: Session) -> None:
        self.quiz_type: str = quiz_options["type"]
        self.quiz_length: int = quiz_options["amount"]
        self.session = session
        self.items: list[QuizItem] = []
        self.current_index: int = 0
        self.correct_count: int = 0
        self.incorrectly_answered: list[QuizItem] = []

    def start_quiz(self) -> None:
        self.initialize_quiz_items()

    def initialize_quiz_items(self) -> None:
        """Query database for needed items and set up questions / answers"""
        all_items = []
        if self.quiz_type == "acronyms":
            all_items = self.session.query(
                QuizItem).filter_by(quiz_type="acronym").all()
        else:
            all_items = self.session.query(
                QuizItem).filter_by(quiz_type="term").all()

        if self.quiz_length == 0:
            self.items = all_items
        else:
            counter = self.quiz_length
            while counter != 0:
                self.items.append(random.choice(all_items))
                counter -= 1

        random.shuffle(self.items)

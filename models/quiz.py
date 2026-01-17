from sqlalchemy.orm import sessionmaker


class Quiz():
    def __init__(self, quiz_options: dict, session: sessionmaker) -> None:
        self.quiz_type = quiz_options["type"]
        self.quiz_amount = quiz_options["amount"]
        self.session = session

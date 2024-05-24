from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.repository.base import Base


class SQLiteEngine:
    def __init__(self):
        self._engine = create_engine('sqlite:///chatbot.db')
        Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)

    def get_session(self):
        return self._session

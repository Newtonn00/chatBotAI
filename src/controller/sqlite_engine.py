from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.repository.base import Base


class SQLiteEngine:
    def __init__(self, config):
        db_directory = f'{config.work_dir}/{config.app_db_directory}'
        self._engine = create_engine(f'sqlite:///{db_directory}/chatbot.db')
        Base.metadata.create_all(self._engine)
        self._session = sessionmaker(bind=self._engine)

    def get_session(self):
        return self._session()

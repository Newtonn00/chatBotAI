from src.repository.user_model import UserModel
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db_engine):
        self._session: Session = db_engine.get_session()

    def read(self, username: str) -> dict:
        curr_session = self._session

        user_data = curr_session.query(UserModel).filter_by(username=username).first()
        curr_session.close()
        return user_data

    def create(self, username) -> dict:
        curr_session = self._session
        user = UserModel(username=username)
        curr_session.add(user)
        curr_session.commit()
        return user


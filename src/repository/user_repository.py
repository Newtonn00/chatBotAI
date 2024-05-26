from src.repository.user_model import UserModel
from sqlalchemy.orm import Session
from src.entity.user_entity import UserEntity


class UserRepository:
    def __init__(self, db_engine):
        self._session: Session = db_engine.get_session()

    def _map_rep_dataclass(self, rep_data: UserModel) -> UserEntity:
        user_dataclass = None
        if rep_data:
            user_dataclass = UserEntity(
                id=rep_data.id,
                username=rep_data.username
            )
        return user_dataclass

    def read(self, username: str) -> UserEntity:
        curr_session = self._session

        user_data = curr_session.query(UserModel).filter_by(username=username).first()
        user_entity = self._map_rep_dataclass(user_data)
        curr_session.close()

        return user_entity

    def create(self, username) -> UserEntity:
        curr_session = self._session
        user_data = UserModel(username=username)
        curr_session.add(user_data)
        curr_session.commit()
        user_entity = self._map_rep_dataclass(user_data)
        curr_session.close()

        return user_entity


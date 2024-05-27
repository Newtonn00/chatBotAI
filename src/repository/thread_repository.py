from src.repository.thread_model import ThreadModel
from sqlalchemy.orm import Session
from src.entity.thread_entity import ThreadEntity
import logging
from sqlalchemy.exc import SQLAlchemyError


class ThreadRepository:
    def __init__(self, db_engine):
        self._session: Session = db_engine.get_session()
        self._logger = logging.getLogger("")

    def _map_rep_dataclass(self, rep_data: ThreadModel) -> ThreadEntity:
        thread_dataclass = None
        if rep_data:
            thread_dataclass = ThreadEntity(
                id=rep_data.id,
                user_id=rep_data.user_id,
                thread_id=rep_data.thread_id,
                content=rep_data.content,
                created_on_timestamp=rep_data.created_on_timestamp,
                active=rep_data.active
            )
        return thread_dataclass

    def read(self, user_id: int) -> ThreadEntity:
        thread_dataclass = None
        try:
            curr_session = self._session

            thread_data = curr_session.query(ThreadModel).filter_by(user_id=user_id, active=True).first()
            thread_dataclass = self._map_rep_dataclass(thread_data)
            curr_session.close()
        except SQLAlchemyError as err:
            self._logger.error(f'Users thread ({user_id}) reading error: {err}')

        return thread_dataclass

    def create(self, user_id, thread_id, active, content="No summary provided") -> ThreadEntity:
        thread_dataclass = None
        try:
            curr_session = self._session
            thread = ThreadModel(thread_id=thread_id, user_id=user_id, active=active, content=content)
            curr_session.add(thread)
            curr_session.commit()
            thread_dataclass = self._map_rep_dataclass(thread)
            curr_session.close()
            self._logger.info(f'Users thread {thread_id} created')
        except SQLAlchemyError as err:
            self._logger.error(f'Users thread ({user_id}) creating error: {err}')
        return thread_dataclass

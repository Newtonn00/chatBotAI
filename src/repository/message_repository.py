from typing import List

from src.repository.message_model import MessageModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging
from src.entity.message_entity import MessageEntity


class MessageRepository:
    def __init__(self, db_engine):
        self._session: Session = db_engine.get_session()
        self._logger = logging.getLogger("")

    def _map_rep_dataclass(self, rep_data: MessageModel) -> MessageEntity:
        message_dataclass = None
        if rep_data:
            message_dataclass = MessageEntity(
                id=rep_data.id,
                user_id=rep_data.user_id,
                thread_id=rep_data.thread_id,
                role=rep_data.role,
                message_timestamp=rep_data.message_timestamp,
                message_text=rep_data.message_text
            )
        return message_dataclass

    def read(self, thread_id: int) -> List[MessageEntity]:
        message_dataclass = None
        try:
            curr_session = self._session
            message_data = curr_session.query(MessageModel).filter_by(thread_id=thread_id).all()
            message_dataclass = [self._map_rep_dataclass(message) for message in message_data]
            curr_session.close()
        except SQLAlchemyError as err:
            self._logger.error(f'Messages in thread ({thread_id}) reading error: {err}')

        return message_dataclass

    def create(self, user_id, thread_id, role, message_text) -> MessageEntity:
        message_dataclass = None
        try:
            curr_session = self._session
            message = MessageModel(user_id=user_id, thread_id=thread_id, role=role,
                                   message_text=message_text)
            curr_session.add(message)
            curr_session.commit()
            message_dataclass = self._map_rep_dataclass(message)
            curr_session.close()
            self._logger.info(f'Message in thread {thread_id} created')
        except SQLAlchemyError as err:
            self._logger.error(f'Message in thread ({thread_id}) creating error: {err}')

        return message_dataclass

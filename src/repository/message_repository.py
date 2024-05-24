from typing import List

from src.repository.message_model import MessageModel
from sqlalchemy.orm import Session
from src.entity.message_entity import MessageEntity


class MessageRepository:
    def __init__(self, db_engine):
        self._session: Session = db_engine.get_session()

    def _map_rep_dataclass(self, rep_data: MessageModel) -> MessageEntity:
        thread_dataclass = MessageEntity(
            id=rep_data.id,
            user_id=rep_data.user_id,
            thread_id=rep_data.thread_id,
            role=rep_data.role,
            message_timestamp=rep_data.message_timestamp,
            message_text=rep_data.message_text
        )
        return thread_dataclass

    def read(self, thread_id: int) -> List[MessageEntity]:
        curr_session = self._session

        message_data = curr_session.query(MessageModel).filter_by(thread_id=thread_id).all()
        curr_session.close()
        message_dataclass = [self._map_rep_dataclass(message) for message in message_data]
        return message_dataclass

    def create(self, user_id, thread_id, role, message_timestamp, message_text) -> MessageEntity:
        curr_session = self._session
        message = MessageModel(user_id=user_id, thread_id=thread_id, role=role, message_timestamp=message_timestamp,
                               message_text=message_text)
        curr_session.add(message)
        curr_session.commit()
        message_dataclass = self._map_rep_dataclass(message)
        return message_dataclass


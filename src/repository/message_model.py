import time

from sqlalchemy import Column, Integer, Text, ForeignKey, String
from src.repository.base import Base


class MessageModel(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    thread_id = Column(String)
    role = Column(String)
    message_timestamp = Column(Integer, default=lambda: int(time.time()))
    message_text = Column(Text)

    def __init__(self, user_id, thread_id, role, message_text):
        self.user_id = user_id
        self.thread_id = thread_id
        self.role = role
        self.message_text = message_text

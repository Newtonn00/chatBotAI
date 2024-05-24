from sqlalchemy import Column, Integer, Text, ForeignKey, String
from base import Base
from sqlalchemy.orm import relationship


class MessageModel(Base):
    __tablename__ = 'threads'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    thread_id = Column(Integer)
    role = Column(String)
    message_timestamp = Column(Integer)
    message_text = Column(Text)

    def __init__(self, user_id, thread_id, role, message_timestamp, message_text):
        self.user_id = user_id
        self.thread_id = thread_id
        self.role = role
        self.message_timestamp = message_timestamp
        self.message_text = message_text

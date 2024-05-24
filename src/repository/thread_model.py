from sqlalchemy import Column, Integer, Text, Boolean
from src.repository.base import Base


class ThreadModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer)
    user_id = Column(Integer, unique=True)
    created_on_timestamp = Column(Integer)
    content = Column(Text)
    active = Column(Boolean)

    def __init__(self, user_id: int, thread_id: int, created_on_timestamp: int, content:Text,
                 active: bool):
        self.thread_id = thread_id
        self.user_id = user_id
        self.created_on_timestamp = created_on_timestamp
        self.content = content
        self.active = active

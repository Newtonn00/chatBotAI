import time
from sqlalchemy import Column, Integer, Text, Boolean, String
from src.repository.base import Base


class ThreadModel(Base):
    __tablename__ = 'thread'
    id = Column(Integer, primary_key=True)
    thread_id = Column(String)
    user_id = Column(Integer, unique=True)
    created_on_timestamp = Column(Integer, default=lambda: int(time.time()))
    content = Column(String)
    active = Column(Boolean)

    def __init__(self, user_id: int, thread_id: str, active: bool,
                 content="No summary provided"):
        self.thread_id = thread_id
        self.user_id = user_id
        self.content = content
        self.active = active

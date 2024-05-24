from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.repository.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

    def __init__(self, username: str):
        self.name = username

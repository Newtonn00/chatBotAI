from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

class Thread(Base):
    __tablename__ = 'threads'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='threads')
    thread_id = Column(String, unique=True)
    summary = Column(Text)  # поле для хранения суммаризации

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer, ForeignKey('threads.id'))
    content = Column(Text)
    thread = relationship('Thread', back_populates='messages')

User.threads = relationship('Thread', order_by=Thread.id, back_populates='user')
Thread.messages = relationship('Message', order_by=Message.id, back_populates='thread')

engine = create_engine('sqlite:///chatbot.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

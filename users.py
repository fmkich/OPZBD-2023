from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from base import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    reviews = relationship('Review', back_populates='user')
    recipes = relationship('Recipe', back_populates='author')

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password



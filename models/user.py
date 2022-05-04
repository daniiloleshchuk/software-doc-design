from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models import AbstractModel


class User(AbstractModel):
    __tablename__ = 'users'
    pk = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=True)
    email = Column(String(50), nullable=False)
    stories = relationship("Story", back_populates="author")

    def __init__(self, username, name, email, surname=None):
        self.username = username
        self.name = name
        self.email = email
        self.surname = surname

    def json(self):
        return {
            'username': self.username,
            'name': self.name,
            'surname': self.surname,
            'email': self.email
        }

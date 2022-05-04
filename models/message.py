from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from models import AbstractModel


class Message(AbstractModel):
    __tablename__ = 'messages'

    pk = Column(Integer, primary_key=True)
    author_pk = Column(Integer, ForeignKey('users.pk'), nullable=False)
    author = relationship('User', backref='author', foreign_keys=author_pk)
    addressee_pk = Column(Integer, ForeignKey('users.pk'), nullable=False)
    addressee = relationship('User', backref='addressee', foreign_keys=addressee_pk)
    text = Column(String(512), nullable=False)

    def __init__(self, author_pk, addressee_pk, text):
        self.author_pk = author_pk
        self.addressee_pk = addressee_pk
        self.text = text

    def json(self):
        return {
            'author_pk': self.author_pk,
            'addressee_pk': self.addressee_pk,
            'text': self.text
        }

from sqlalchemy import Column, Integer, ForeignKey, func, TIMESTAMP, String
from sqlalchemy.orm import relationship

from models import AbstractModel


class Story(AbstractModel):
    __tablename__ = 'stories'
    pk = Column(Integer, primary_key=True, autoincrement=True)
    author_pk = Column(Integer, ForeignKey('users.pk'))
    author = relationship("User", back_populates="stories", cascade="all, delete")
    created_at = Column(TIMESTAMP(timezone=False), server_default=func.now())
    media_path = Column(String(256))

    def __init__(self, media_path, author_pk, *args, **kwargs):
        self.media_path = media_path
        self.author_pk = author_pk

    def json(self):
        return {
            'author_pk': self.author_pk,
            'created_at': str(self.created_at),
            'media_path': self.media_path
        }

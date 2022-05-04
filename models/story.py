from sqlalchemy import Column, Integer, ForeignKey, func, TIMESTAMP, String
from sqlalchemy.orm import relationship

from models import AbstractModel


class Story(AbstractModel):
    __tablename__ = 'stories'
    pk = Column(Integer, primary_key=True)
    author_pk = Column(Integer, ForeignKey('users.pk'), nullable=False)
    author = relationship("User", back_populates="stories")
    created_at = Column(TIMESTAMP(timezone=False), server_default=func.now())
    media_path = Column(String(256))

    def __init__(self, media_path):
        self.media_path = media_path

    def json(self):
        return {
            'author_pk': self.author_pk,
            'created_at': self.created_at,
            'media_path': self.media_path
        }

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models import Message, Story


class StoryReaction(Message):
    __tablename__ = 'story_reactions'

    pk = Column(Integer, ForeignKey('messages.pk'), primary_key=True)
    story_pk = Column(Integer, ForeignKey('stories.pk'))
    story = relationship('Story', backref='story')

    def __init__(self, author_pk, story_pk, text, session=None):
        self.story_pk = story_pk
        self.story = Story.get_by_pk(story_pk, session=session)
        super().__init__(author_pk, self.story.author_pk, text)

    def json(self):
        return {**super().json(), **{'story_pk': self.story_pk}}

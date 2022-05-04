from flask_restful import reqparse

from models import StoryReaction
from resources.abstract_resource import AbstractResource, AbstractResourceList


class StoryReactionResource(AbstractResource):
    model = StoryReaction
    parser = reqparse.RequestParser()
    parser.add_argument('author_pk', type=int, required=True)
    parser.add_argument('story_pk', type=int, required=True)
    parser.add_argument('text', type=str, required=True)


class StoryReactionListResource(AbstractResourceList):
    model = StoryReaction

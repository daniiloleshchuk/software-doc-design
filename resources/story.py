from datetime import datetime

from flask_restful import reqparse

from models import Story
from resources.abstract_resource import AbstractResource, AbstractResourceList


class StoryResource(AbstractResource):
    model = Story
    parser = reqparse.RequestParser()
    parser.add_argument('author_pk', type=int, required=False)
    parser.add_argument('created_at', type=datetime, required=False)
    parser.add_argument('media_path', type=str, required=False)


class StoryListResource(AbstractResourceList):
    model = Story

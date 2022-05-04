from flask_restful import reqparse

from models import Message
from resources.abstract_resource import AbstractResource, AbstractResourceList


class MessageResource(AbstractResource):
    model = Message
    parser = reqparse.RequestParser()
    parser.add_argument('author_pk', type=int, required=True)
    parser.add_argument('addressee_pk', type=int, required=True)
    parser.add_argument('text', type=str, required=True)


class MessageListResource(AbstractResourceList):
    model = Message

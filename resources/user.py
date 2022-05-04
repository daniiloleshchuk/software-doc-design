from flask_restful import reqparse

from models import User
from resources.abstract_resource import AbstractResource, AbstractResourceList


class UserResource(AbstractResource):
    model = User
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=False)
    parser.add_argument('name', type=str, required=False)
    parser.add_argument('surname', type=str, required=False)
    parser.add_argument('email', type=str, required=False)


class UsersListResource(AbstractResourceList):
    model = User

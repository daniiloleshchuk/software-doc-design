from flask import Flask, render_template
from flask_restful import Api

from db import init_db, session
from models import Story, User, Message, StoryReaction
from resources import (UserResource, UsersListResource, StoryResource, StoryListResource,
                       StoryReactionResource, StoryReactionListResource)
from resources.message import MessageResource, MessageListResource
from utils import write_from_csv_to_db, generate_csv

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/user', '/user/<int:pk>')
api.add_resource(UsersListResource, '/users')
api.add_resource(MessageResource, '/message', '/message/<int:pk>')
api.add_resource(MessageListResource, '/messages')
api.add_resource(StoryResource, '/story', '/story/<int:pk>')
api.add_resource(StoryListResource, '/stories')
api.add_resource(StoryReactionResource, '/story_reaction', '/story_reaction/<int:pk>')
api.add_resource(StoryReactionListResource, '/story_reactions')


@app.route("/", methods=["GET"])
def index():
    stories = [x.json() for x in Story.get_all()]
    users = [x.json() for x in User.get_all()]
    messages = [x.json() for x in Message.get_all()]
    reactions = [x.json() for x in StoryReaction.get_all()]
    return render_template("index.html", stories=stories, users=users, messages=messages, reactions=reactions)


if __name__ == '__main__':
    # init_db()
    # generate_csv('input_data.csv')
    # write_from_csv_to_db('input_data.csv', ['User', 'Story', 'Message', 'StoryReaction'], session=session)
    app.run()

import re
import sys
from random import randint

from db import Session
from models import User


def write_from_csv_to_db(csv_filename, sections_to_search, session=None):
    session = Session() if not session else session
    with open(csv_filename, 'r+') as file:
        for part in re.split(r'\n\n+', file.read()):
            rows = part.split('\n')
            for row in rows:
                for section_name in sections_to_search:
                    if section_name == row.strip():
                        cls = getattr(sys.modules['models'], section_name)
                        for row in rows[1:]:
                            args = row.split(',')
                            obj = cls(*args, session=session) if section_name == 'StoryReaction' else cls(*args)
                            if section_name == 'Story':
                                user = User.get_by_pk(randint(1, len(rows) - 1), session=session)
                                user.stories.append(obj)
                                user.save(session=session)
                            else:
                                obj.save(session=session)

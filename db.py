import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get('SDDLab_DB_URI'))
metadata = MetaData()
Session = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)

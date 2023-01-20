import environ
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session
from db.model import *

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()
DB_URL = env('DB_URL')
engine = create_engine(DB_URL, echo=True)

engine.connect()
metadata = MetaData()
session = Session(engine)

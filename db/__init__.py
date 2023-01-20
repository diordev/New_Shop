import sqlalchemy as db
from sqlalchemy.orm import Session

engine = db.create_engine('postgresql://postgres:1@localhost/news_db')
connection = engine.connect()
metadata = db.MetaData()
session = Session(engine)


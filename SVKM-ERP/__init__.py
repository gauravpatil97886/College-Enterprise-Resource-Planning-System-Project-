import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(bind=engine)

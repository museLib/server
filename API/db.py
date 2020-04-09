from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
RDB_PATH = f'postgresql://muse:{os.environ.get("DB_PASSWORD")}@db:5432/muse'

engine = create_engine(RDB_PATH, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

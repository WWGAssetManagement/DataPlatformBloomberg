from tkinter.tix import IMMEDIATE
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.log import Logging

load_dotenv()

DATABASE = os.environ.get("DATABASE")

ENGINE = create_engine(DATABASE, echo=False)
SESSION = sessionmaker(bind=ENGINE)

BASE = declarative_base()
META = MetaData()


LOG = Logging()


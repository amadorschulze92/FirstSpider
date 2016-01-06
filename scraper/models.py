from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """performs database connection using settings.py"""
    return create_engine(URL(**settings.DATABASE))

def create_deal_table(engine):
    DeclarativeBase.metadata.create_all(engine)
    
class People(DeclarativeBase):
    """Sqlalchemy people model"""
    __tablename__ = "people"
    
    id = Column(Integer, primary_key=True)
    url = Column('url', String, nullable=True)
    title = Column('title', String, nullable=True)
    name = Column('name', String, nullable=True)
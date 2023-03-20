from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase


DATABASE_NAME = 'computer_firm.db'

engine = create_engine(f'sqlite:///{DATABASE_NAME}')


class Base(DeclarativeBase):
    pass


def create_database():
    Base.metadata.create_all(engine)

from sqlalchemy import creat_engine
form sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase


DATABASE_NAME = 'computer.firm.db'

engine = creat_engine(f'ssqlite:///{DATABASE_NAME}')

class Base(DeclarativeBase)
    pass


def create_database():
    Base.metadata.create_all(engine)

from sqlalchemy import Column, Integer, String, ForeignKey

from modules.database import Base

class Car (Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True)
    model_name = Column(String)
    year_of_release = Column(Integer)
    price = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self)
    



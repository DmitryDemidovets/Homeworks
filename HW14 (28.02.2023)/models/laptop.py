from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base


class Laptop(Base):
    __tablename__ = 'laptops'

    id = Column(Integer, primary_key=True, index = True)
    model_id = Column(Integer, ForeignKey('products_id'))
    speed = Column (Integer)
    ram = Column (Integer)
    cd = Column (String)
    hd = Column(Integer)
    price = Column(Integer)
    screen = Column(Integer)


    def __init__(self, model_id: int, sped: int, ram: int, cd: str, hd: int, price: int, screen: int):
        self.model_id = model_id
        self.speed = speed
        self.ram = ram
        self.cd = cd
        self.hd = hd
        self.price = price
        self.screen = screen
#

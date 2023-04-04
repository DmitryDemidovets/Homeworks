from sqlalchemy import Column, Integer, String
from models.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    manufacturer = Column(String)
    model = Column(String, unique=True)
    
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
#Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12х или 24х CD и цену менее 600 долларов.


from models.database import engine
from sqlalchemy.orm import Session
from models.pc import PC
from models.product import Product
from sqlalchemy import or_

def get_query3(speed_cd1, speed_cd2, value):
    with Session(autoflush=False, bind=engine) as db:
        result = db.query(
            PC.speed, 
            PC.hd, 
            Product.manufacturer,
            Product.model
            ).join(
            Product,
            Product.id == PC.model_id,
            isouter = True
            ).filter(
            or_(PC.cd == speed_cd1, PC.cd == speed_cd2), 
            PC.price < value).all()
            
        for u in result:
            print(f'Manufacturer: {u.manufacturer} Model: {u.model} Speed: {u.speed} HDD: {u.hd}')
#

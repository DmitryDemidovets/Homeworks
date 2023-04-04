from models.database import engine
from models.laptop import Laptop
from models.pc import PC
from models.product import Product
from sqlalchemy.orm import Session
from faker import Faker


def create_db_comp_firm():
    
    with Session(autoflush=False, bind=engine) as db:
        
        fake = Faker('ru_RU')

        # Fake_data Products
        products_list = ['Samsung', 'LG', 'Acer', 'Lenovo', 'Xiaomi', 'Dell', 'MSI', 'Razer']
               
        for _ in range(30):
            manufacturer = fake.random.choice(products_list)
            model = fake.bothify('????-########')
            product1 = Product(manufacturer, model)
            db.add_all([product1])

        ram_list = [4, 8, 16, 32]
        hd_list = [265, 512, 1024, 2056] 
        cd_list = ['12x', '8x', '16x', '32x', '24x']

        # Fake_data Laptops
        model_id= 1
       
        for _ in range(15):

            speed = fake.random.randint(500, 1000)
            ram = fake.random.choice(ram_list)
            hd = fake.random.choice(hd_list)
            cd = fake.random.choice(cd_list)
            price = fake.random.randint(400, 1500)
            screen = fake.random.randint(13, 17)
            laptop1 = Laptop(model_id, speed, ram, hd, cd, price, screen)
            db.add_all([laptop1])
            model_id += 1

        # Fake_data PCs
        model_id = 16    

        for _ in range(15):
            
            speed = fake.random.randint(500, 1000)
            ram = fake.random.choice(ram_list)
            hd = fake.random.choice(hd_list)
            cd = fake.random.choice(cd_list)
            price = fake.random.randint(200, 1000)
            pc1 = Pc(model_id, speed, ram, hd, cd, price)
            db.add_all([pc1])
            model_id += 1
        
        db.commit()
    
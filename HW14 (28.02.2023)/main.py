from script_fake_data import create_db_comp_firm
from models.database import create_database
from test1 import get_query1
from test2 import get_query2
from test3 import get_query3

# create_db_comp_firm
def main():
    create_database()
    print('''\nНомер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 долларов:''')
    get_query1(500)
    print('''\nНомер модели, объем памяти и размеры экранов ноутбуков, цена которых превышает 1000 долларов''')
    get_query2(1000)
    print('''\nНомер модели, скорость и размер жесткого диска ПК, имеющих 12х или 24х CD и цену менее 600 долларов.''')
    get_query3('12x', '24x', 600)

if __name__ == '__main__':
    main()
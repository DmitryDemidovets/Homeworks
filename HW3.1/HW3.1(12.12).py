'''В итоговый файл coctails.txt должны записаться коктейли в виде структурированного списка
состоящего из полей (название, описание, картинка)
'''
#C:/Users/DDemidovec/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/DDemidovec/HW Step/HW3.1/HW3.1(12.12).py"
import os
print(os.getcwd())
import requests

def response():
    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = r.json()
    str = ''
    for item in data['drinks']:
        str += (f"Cocktail: {item['strDrink']}; How to prepare: {item['strInstructions']}; Link to photo: {item['strDrinkThumb']} \n")
    return str
        
def record(x):
    with open('cocktails.txt', 'w+') as f:
        f.write(x)       

record(response())
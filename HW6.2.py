'''
Задача 2

Напишите функцию, которая будет примет список нечетных чисел, выводит их и остановится,
если встретит число 200. Типизировать ее. При запуске mypy не должно быть никаких ошибок
типов
'''
import random
from typing import Union

x: list = [x for x in range(random.randint(50, 100)) if x%2]
x[random.randint(0, len(x))] = 200

print(x)

def list_output(list: list) -> Union[str, None]:
    for i in list:
        if i != 200:
            print(i)
        else:
            return "Number 200 was found."
    return None
            
print(list_output(x))



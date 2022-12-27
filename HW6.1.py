'''
Задача 1 

Создать функцию calc(a, b, operation). Описание входных параметров: 1. Первое число 2.
Второе число 3. Действие над ними: 1) + Сложить 2) - Вычесть 3) * Умножить 4) / Разделить 5) В
остальных случаях функция должна возвращать "Операция не поддерживается". Типизировать
ее. При запуске mypy не должно быть никаких ошибок типов
'''
from typing import Callable
a: float = float(input('Input first number ... '))
operator: str = input('Input operator ... ')
while operator not in ('+', '-', '*', '/'):
    operator = input('Operation is not supported ! Input correct operator as + , - , * , / ... ') 
    # print error message 
b: float = float(input('Input second number ... '))

def calc(a:float, b: float, operator: str) -> float: 
    # converts arguments to string and calculates the result
    answer: float = float(eval(str(a)+operator+str(b)))
    return answer

def title(func: Callable):
    def wrapper(func: float):
        global a, b, operator
        print(f"{a:g} {operator} {b:g} = {func:g}".center(102), end= '\n\n\n') 
    return wrapper


@title
def print_result(func: float):
    print(func)

print(print_result(calc(a, b, operator)))
###

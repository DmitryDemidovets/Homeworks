'''
Задача 3

Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и
возвращает название сезона, к которому относится этот месяц. Например, передаем 2, на
выходе получаем 'Зима'.
'''
import calendar
from typing import Callable

month = int(input('Input the number of the month... '))

def month_to_season(month: int) -> str:
    seasons = {'winter':(12,1,2),
               'spring':(3,4,5),
               'summer':(6,7,8),
               'fall':(9,10,11)}
    for key in seasons.keys():
        if month in seasons[key]:
            return key

def title(func: Callable):
    def wrapper(func: str):
        global month
        print("START".center(25), end= '\n\n\n')
        if func is not None:
            print(f"{calendar.month_name[month]} is the {func} month".center(25), end= '\n\n\n')
        else:
            print(f"Such month does not exist !".center(25), end= '\n\n\n')
    return wrapper


@title
def print_result(func: str):
    print(func)


print(print_result(month_to_season(month)))
# Задача 3- Реализуйте функцию min2time(mm), которая минуты с начала суток переводит в часы и минуты
#(для показа на электронных часах).

import datetime

def hours_minutes(): 
    current = datetime.datetime.now()
    return current.hour, current.minute

def time2min(x): 
    min = x[0]*60+x[1]
    return min

def title(func):
    def wrapper(func):
        print("*"*60)
        print("START".center(60, '-'), end= '\n\n\n')
        print(f'{func} minutes have passed since the beginning of the day ⧗'.center(60), end= '\n\n\n')
        print("FINISH".center(60, '-'))
        print("*"*60)
    return wrapper

@title
def print_minutes(func):
    print(func)

print(print_minutes(time2min(hours_minutes())))
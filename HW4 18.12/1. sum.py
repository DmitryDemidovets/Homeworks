#Задача 1- Напишите функцию sum(start, end), которая суммирует все целые числа от значения «start» до
#величины «end» включительно. Если пользователь задаст первое число большее чем второе,
#просто поменяйте их местами.
def sum(start, end):
    sum = 0
    if end < start: 
        start, end = end, start
    for i in range(start, end+1): 
        sum = sum + i
    return sum

start, end = int(input('Input firts value fo the range ...')), int(input('Input second value fo the range ...'))

print(f"Sum of all values in range is {sum(start, end)}.")
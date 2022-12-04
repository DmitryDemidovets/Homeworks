# Задача 1- Напишите функцию, которая принимает аргумент в виде списка и возвращает словарь,
#в котором каждый элемент списка является и ключом и значением. Предполагается,
#что элементы списка будут соответствовать правилам задания ключей в словарях.
def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([1, 2, 3, 4]))
print(to_dict(['hi', (1, 10), 5, 25]))

# Задача 2- Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый
#и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ
#«new_key» со значением «new_value». Выведите на печать итоговый словарь.
from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
# Меняем местами первый и последний элементы
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
# Удаляем второй элемент
second = list(dct.items())[1]
del dct[second[0]]
# Вставляем новый элемент
dct['new_key'] = 'new_value'
my_dict = {5: 5, 3: 3, 4: 4, 1: 1, 'new_key': 'new_value'}

# Задача 3- Дан произвольный список. Представьте его в обратном порядке. (двумя вариантами)
#1
films = ['Knockin On Heavens Door', 'invisible guest', 'Eyes Wide Shut', 'Nocturnal Animals'] 
films.reverse()
print(films)
#2
films = ['Knockin On Heavens Door', 'invisible guest', 'Eyes Wide Shut', 'Nocturnal Animals'] 
print(films[::-1])

# Задача 4- Необходимо удалить пустые строки из списка строк.
if __name__ == '__main__':
    films = ['Knockin On Heavens Door','','invisible guest','', 'Eyes Wide Shut', 'Nocturnal Animals'] 
    try:
        while True:
            films.remove('')
    except ValueError:
        pass
    print(films) 

# Задача 5- Даны списки:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in range(len(a)):
   for j in range(len(b)):
       if a[i] == b[j]:
           c.append(a[i])
print(list(c))


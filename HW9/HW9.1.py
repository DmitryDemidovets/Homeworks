#Разработайте GUI-программу используя Tkinter «Найти сумму двух чисел» с
#использованием класса.
from tkinter import *
root = Tk()
root.title('Сумма двух чисел')
def Summa():
    # берем данные из первого поля
    a = EntryA.get() 
    # преобразуем в число
    a = int(a) 
    # берем данные из второго поля
    b = EntryB.get() 
    # преобразуем в число
    b = int(b) 
    # результат суммы переводим в строку для вывода
    result = str(a + b) 
    # очищаем текстовое поле 
    EntryC.delete(0, END) 
    # вставляем результат в начало
    EntryC.insert(0, result)  
# первая метка в строке, выравниваем
Label(root, text='Первое число').grid(row=0, sticky=W)
# вторая метка в строке 1
Label(root, text='Второе число').grid(row=1, sticky=W)

# создаем виджеты текстовых полей
EntryA = Entry(root, width=10, font='Arial 16')
EntryB = Entry(root, width=10, font='Arial 16')
EntryC = Entry(root, width=20, font='Arial 16')

# размещаем первые два поля справа от меток
EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)

# третье текстовое поле ввода на всю ширину строки 2
EntryC.grid(row=2, columnspan=2)

# размещаем кнопку в строке 3 во втором столбце 
but = Button(root, text='Сумма')
but = Button(root, text='Сумма', command=Summa)
but.grid(row=3, column=1, sticky=E)

root.mainloop()


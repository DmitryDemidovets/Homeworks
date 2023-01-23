#Разработайте GUI-программу используя Tkinter «Найти сумму двух чисел» с
#использованием класса.
from tkinter import *
root = Tk()
root.title('Сумма двух чисел')
def Summa():
    a = EntryA.get() # берем данные из первого поля
    a = int(a) # преобразуем в число
    b = EntryB.get() # берем данные из второго поля
    b = int(b) # преобразуем в число
    result = str(a + b) # результат суммы переводим в строку для вывода
    EntryC.delete(0, END) # очищаем текстовое поле полностью
    EntryC.insert(0, result) # вставляем результат в начало 
# первая метка в строке 0, столбце 0 (0 по умолчанию)
# парамет sticky  означает выравнивание, W — запад
Label(root, text='Первое число').grid(row=0, sticky=W)
# вторая метка в строке 1
Label(root, text='Второе число').grid(row=1, sticky=W)

# создаем виджеты текстовых полей
EntryA = Entry(root, width=10, font='Arial 16')
EntryB = Entry(root, width=10, font='Arial 16')
EntryC = Entry(root, width=20, font='Arial 16')

# размещаем первые два поля справа от меток, второй столбец (отсчет от нуля)
EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)

# третье текстовое поле ввода занимает всю ширину строки 2
# columnspan — объединение ячеек по столбцам; rowspan — по строкам
EntryC.grid(row=2, columnspan=2)

# размещаем кнопку в строке 3 во втором столбце 
but = Button(root, text='Сумма')
but = Button(root, text='Сумма', command=Summa)
but.grid(row=3, column=1, sticky=E)

root.mainloop()


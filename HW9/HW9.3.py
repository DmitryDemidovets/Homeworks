#Разработайте GUI-программу "Телефонная книга” используя Tkinter, в которой можно
#вводить имя и номер телефона. Снизу в поле вывода отображаются номера и имена.
from tkinter import *
root = Tk()
root.title('Телефонная книга')
def numbers_and_names():
    # берем данные имени из первого поля
    a = EntryA.get() 
    # преобразуем в строку
    a = str(a) 
    # берем данные номера телефона из второго поля
    b = EntryB.get() 
    # преобразуем в строку
    b = str(b) 
    # результат ввода переводим в строку для вывода
    result = str(b + "-" + a) 
    # очищаем текстовое поле 
    EntryC.delete(0, END) 
    # вставляем результат в начало
    EntryC.insert(0, result)  

# первая метка в строке, выравниваем
Label(root, text='Введите имя:').grid(row=0, sticky=W)
# вторая метка в строке 1
Label(root, text='Введите номер телефона:').grid(row=1, sticky=W)

# создаем виджеты текстовых полей
EntryA = Entry(root, width=25, font='Arial 10')
EntryB = Entry(root, width=25, font='Arial 10')
EntryC = Entry(root, width=50, font='Arial 10')

# размещаем первые два поля справа от меток
EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)

# третье текстовое поле ввода на всю ширину строки 2
EntryC.grid(row=2, columnspan=2)

# размещаем кнопку в строке 3 во втором столбце 
but = Button(root, text='Вывести данные')
but = Button(root, text='Вывести данные', command=numbers_and_names)
but.grid(row=3, column=1, sticky=E)
root.mainloop()
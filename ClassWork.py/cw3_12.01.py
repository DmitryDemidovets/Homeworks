# Импортируем все из библиотеки TKinter
from tkinter import *
from tkinter import messagebox
root = Tk()
def btn_click():
    login = loginInput.get()
    password = passField.get()
    info_str = f'Данные: {str(login)}, {str(password)}'
    messagebox.showinfo(title = 'название', message = '') 
# окно с ошибкой
messagebox.showerror(title ='', message = 'Error always!!!' )
    
root['bg'] = '#31ce87'
# Указываем размеры окна
root.geometry('300x250')
#название программы
root.title('Название программы')
# Делаем невозможным менять размеры окна
root.resizable(width=False, height=False)
#запуск постоянного цикла
canvas = Canvas(root, width=250, height=300)
canvas.pack()
frame = Frame(root, bg="red")
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight=0.7)
title = Label (frame, text = 'Текст подсказка', bg = 'gray', font = 40)
title.pack()
btn = Button(frame, text = 'Кнопка', bg = 'yellow', command = btn_click)
btn.pack()

passField = Entry(frame, bg = 'white', show = '*')
passField.pack()


root.mainloop()
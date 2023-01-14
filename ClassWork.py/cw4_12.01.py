# размещение виджетов при помощи метода grid
import tkinter as tk
win = tk.Tk()
win.geometry(f'400x500+100+200')
win.title('Графическое приложение')

btn1 = tk.Button(win, text = 'Кнопка 1')
btn2 = tk.Button(win, text = 'Кнопка 2')
btn3 = tk.Button(win, text = 'Кнопка 3')
btn4 = tk.Button(win, text = 'Кнопка 4')
btn5 = tk.Button(win, text = 'Кнопка 5')
btn6 = tk.Button(win, text = 'Кнопка 6')
btn7 = tk.Button(win, text = 'Кнопка 7')
#метод pack

btn1.pack()
# метод grid-это метод, котрый позвояет распологать виджеты в виде таблицы
# метод stick- растягивает кнопку, передать методу первые буквы сторон света
btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row = 1, column = 0)
btn4.grid(row = 1, column = 1)
btn5.grid(row = 2, column = 0)
btn6.grid(row = 2, column = 1)
btn7.grid(row = 3, column = 0, columnspan = 2, stick = 'we')
win.mainloop()


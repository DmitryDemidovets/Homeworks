from tkinter import *
 
 
class Frame(Tk):
    def __init__(self):
        super().__init__()
        super().title('color game')
        self.geometry('100x200')
        self.label = Label(text="", width=230)
        self.entry = Entry(width=230, justify="center")
 
        colors = {'#ff0000':'Красный',
        '#ffff00': 'Желтый',
        '#00ff00': 'Зеленый',
        '#007dff': 'Голубой',
        '#0000ff': 'Синий',
        '#7d00ff': 'Фиолетовый',}
 
        for color in colors.keys():
            func = lambda c = color, ruc=colors[color] : self.onclick(c, ruc)
            btn = Button(text="", command=func, bg=color, width=50, height=3)
            self.label.pack()
            self.entry.pack()
            btn.pack()
            
          
 
    def onclick(self, color, ru_color):
        self.entry.delete(0, END)
        self.entry.insert(0, color)
        
        self.label['text'] = ru_color
 
 
if __name__ == '__main__':
    app = Frame()     
    app.mainloop()
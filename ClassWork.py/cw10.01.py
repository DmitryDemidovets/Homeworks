from tkinter import *
 
 
def changeFont(font):
    l['font'] = font
 
 
root = Tk()
l = Label(text="Hello World")
l.pack()
Button(command=
       lambda f="Verdana": changeFont(f))\
    .pack()
Button(command=
       lambda f="Times": changeFont(f))\
    .pack()
root.mainloop()
class Block():
    def __init__(self, master, func):
        self.label1 = Label(master,width=20, bg='white', fg='black')
        self.label2 = Label(master,width=20, bg='white', fg='black')
        self.button1 = Button(master, width=20, bg='#ff0000')
        self.button2 = Button(master, width=20, bg='#ff7d00')
        self.button3 = Button(master, width=20, bg='#00ff00')
        self.button4 = Button(master, width=20, bg='#007dff')    
        self.button5 = Button(master, width=20, bg='#7d00ff')   
        
        self.button1['command'] = getattr(self, func)
        self.button2['command'] = getattr(self, func)
        self.button3['command'] = getattr(self, func)
        self.button4['command'] = getattr(self, func)
        self.button5['command'] = getattr(self, func)
 
        self.label1.pack()
        self.label2.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        
 
    def click_but(self):
        if self.button1:
            self.label1['text'] = 'красный'
            self.label2['text'] = '#ff0000'
        elif self.button2:
            self.label1['text'] = 'оранжевый'
            self.label2['text'] = '#ff7d00'
        elif self.button3:
            self.label1['text'] = 'зеленый'
            self.label2['text'] = '#00ff00'
        elif self.button4:
            self.label1['text'] = 'голубой'
            self.label2['text'] = '#007dff'
        elif self.button5:
            self.label1['text'] = 'фиолетовый'
            self.label2['text'] = '#7d00ff'
    
     
    
 
root = Tk()
 
first_block = Block(root, command = 'click_but')
 
 
root.mainloop()

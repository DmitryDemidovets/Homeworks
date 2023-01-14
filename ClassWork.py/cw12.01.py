'''
from tkinter import *
root = Tk()
'''
#1) Кнопка
#2) Поле ввода
#3) Текст Label
#4) Окно с программой

#Алгоритм
#1) Создать главное окно
#2) Создаем виджеты и опции
#3) Описываем и обрабатываем события
#4) Располагаем виджеты в главном окне
#5) Запуск цикла обработки
'''

#поле ввода
entry = Entry(root, width=20)
#поле вывода
label = Label(root, width=20, bg='black', fg = 'white')
#кнопка
button = Button (root, text = 'click!')
entry.pack()
button.pack()
label.pack()

root.mainloop()
'''
from tkinter import *
import pygame
import os
 
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()
 
        trackframe = LabelFrame(self.root, text="Current track", font=("times new roman", 15, "bold"),
         bg="gray", fg="white", bd=5, relief=GROOVE)
        
        trackframe.place(x=0, y=0, width=600, height=100)
 
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 15, "bold"),
        bg="silver", fg="white").grid(row=0, column=0, padx=10, pady=10)
 
        trackstatus = Label(trackframe, textvariable=self.status, width=20, font=("times new roman", 15, "bold"),
        bg="silver", fg="white").grid(row=0, column=1, padx=10, pady=5)
 
 
        buttonframe = LabelFrame(self.root, text="Buttons pannel", font=("times new roman", 15, "bold"),
        bg="gray", fg="white", bd=5, relief=GROOVE)
 
        buttonframe.place(x=0, y=100, width=600, height=100)
 
        playbtn = Button(buttonframe, text="PLAYSONG", command=self.playsong, width=10, height=1,
         font=("times new roman", 15, "bold"), fg="navyblue", bg="silver").grid(row=0, column=0,padx=10, pady=5)
        
        playbtn = Button(buttonframe, text="STOPSONG", command=self.stopsong, width=10, height=1,
         font=("times new roman", 15, "bold"), fg="navyblue", bg="silver").grid(row=0, column=3,padx=10, pady=5)
 
        # TODO: добавить кнопку паузы и снять паузу
 
        songframe = LabelFrame(self.root, text="Playlist", font=("times new roman", 15, "bold"),
         bg="gray", fg="white", bd=5, relief=GROOVE)
 
        songframe.place(x=600, y=0, width=400, height=200)
 
        scroll_y = Scrollbar(songframe, orient=VERTICAL)
 
        self.playlist = Listbox(songframe, yscrollcommand=scroll_y.set,selectbackground="gray",
         selectmode=SINGLE, font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE )
 
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
 
        os.chdir("songs")
        songtracks = os.listdir()
 
        for track in songtracks:
            self.playlist.insert(END, track)
        
    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-PLAYING")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()
    
    def stopsong(self):
        self.status.set("-STOPPED")
        pygame.mixer.music.stop()
 
    # дописать методы для паузы и pause off


    
 
root = Tk()
MusicPlayer(root)
root.mainloop()

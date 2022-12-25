from tkinter import *
from tkinter import ttk
from generator import key
from pygame import mixer

def show_message():
    label["text"] = key(entry.get())

root = Tk()
root.title("Приложение на Tkinter")
root.geometry("1920x1080") # задаю окно

bg = PhotoImage(file='301012014.png')  # загружаю фон
label_bg = Label( root, image = bg)
label_bg.place(x = -10, y = -10)  # указываю место

entry = ttk.Entry()
entry.pack(anchor=CENTER, padx=16, pady=16)  # окошко ввода

btn = Button(text="Сгенерировать ключ", command=show_message) # кнопка
btn.pack(anchor=CENTER)

label = ttk.Label()
label.pack(anchor=CENTER, padx=0, pady=0)

mixer.init()
mixer.music.load('Рингтон - Классный вызов.mp3')
mixer.music.play()  # загружаю и запускаю музыку

c = Canvas( width=200, height=200, bg='green')  # параметры поля под анимацию
c.pack()
oval = c.create_oval(0, 0, 25, 25, fill='red')   # параметры кружка

def moveBall():
    c.move(oval, 1, 1)
    c.after(200, moveBall)
    c.move(oval, 1, 1) # направление и скорость

c.after(1000, moveBall) #запуск с задержкой


root.mainloop()
from tkinter import *
import numpy
import sys
import os

def resource_path(relative_path): # Чтобы exe сжал и картинки
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

is_cross = True

def matrix(n): # Команда для матрицы выборов
    return numpy.matrix(f"{n} {n} {n}; {n} {n} {n}; {n} {n} {n}")
field = matrix(0) #Словарь матриц выборов
def choice(r,c): # Команды выборов
    global is_cross,buttons
    button = buttons[(r,c)]
    if is_cross:
        play.configure(text="Нолики")
        button.configure(image = cross, state="disabled")
        field[r,c] = 1
    else:
        play.configure(text="Крестики")
        button.configure(image = zero, state="disabled")
        field[r,c] = -1
    is_cross = not is_cross
    check()
def check(): # Команда проверки
    global buttons
    ch = 3
    ch1 = -3
    if numpy.sum(field[0]) == ch or numpy.sum(field[1]) == ch or numpy.sum(field[2]) == ch or numpy.sum(field[:,0]) == ch or numpy.sum(field[:,1]) == ch or numpy.sum(field[:,2]) == ch or (field[0,0]+field[1,1]+field[2,2]) == ch or (field[0,2]+field[1,1]+field[2,0]) == ch:
        title.configure(text="Победили крестики!")
        for button in list(buttons.values()):
            button.configure(state = "disabled")
        play.configure(state="active", text= "Поехали!")
    elif numpy.sum(field[0]) == ch1 or numpy.sum(field[1]) == ch1 or numpy.sum(field[2]) == ch1 or numpy.sum(field[:,0]) == ch1 or numpy.sum(field[:,1]) == ch1 or numpy.sum(field[:,2]) == ch1 or (field[0,0]+field[1,1]+field[2,2]) == ch1 or (field[0,2]+field[1,1]+field[2,0]) == ch1:
        title.configure(text="Победили нолики!")
        for button in list(buttons.values()):
            button.configure(state = "disabled")
        play.configure(state="active", text= "Поехали!")
    else:
        if 0 in field[:,:]:
            pass
        else:
            title.configure(text="Ничья!")
            play.configure(state="active", text= "Поехали!")
def new_game(): # Команда начала по новой
    global field
    title.configure(text="Крестики нолики")
    field = matrix(0)
    for button in list(buttons.values()):
        button.configure(state = "active", image = na)
    play.configure(state="disabled")
# Конфиг окна
main = Tk()
main.title("Tic-Tac-Toe")
main.resizable(0,0)
# Конфиг текста
title = Label(text="Крестики нолики", font= ("Arial", 20))
title.grid(row=0, column=0, columnspan=3)
# Грузим картинки
cross = PhotoImage(file=resource_path("Pics/cross1.png"))
na = PhotoImage(file=resource_path("Pics/na1.png"))
zero = PhotoImage(file = resource_path("Pics/zero1.png"))
# Делаем кнопки
b00 = Button(image=na, command=lambda:choice(0,0))
b00.grid(row=1, column=0)
b01 = Button(image=na, command=lambda:choice(0,1))
b01.grid(row=1, column=1)
b02 = Button(image=na, command=lambda:choice(0,2))
b02.grid(row=1, column=2)
b10 = Button(image=na, command=lambda:choice(1,0))
b10.grid(row=2, column=0)
b11 = Button(image=na, command=lambda:choice(1,1))
b11.grid(row=2, column=1)
b12 = Button(image=na, command=lambda:choice(1,2))
b12.grid(row=2, column=2)
b20 = Button(image=na, command=lambda:choice(2,0))
b20.grid(row=3, column=0)
b21 = Button(image=na, command=lambda:choice(2,1))
b21.grid(row=3, column=1)
b22 = Button(image=na, command=lambda:choice(2,2))
b22.grid(row=3, column=2)
buttons = {(0,0):b00,(0,1):b01,(0,2):b02,(1,0):b10,(1,1):b11,(1,2):b12,(2,0):b20,(2,1):b21,(2,2):b22}
for button in list(buttons.values()):
    button.configure(state = "disabled", image = na)
play = Button(text="Поехали!",command = new_game, state="active", font=("Arial", 20))
play.grid(row=4,column=0, columnspan = 3)
# Работаем
main.mainloop()


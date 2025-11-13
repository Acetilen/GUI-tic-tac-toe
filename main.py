from tkinter import *
import numpy

# Команда для матрицы выборов
def matrix(n):
    return numpy.matrix(f"{n} {n} {n}; {n} {n} {n}; {n} {n} {n}")
#Словарь матриц выборов
field = matrix(0)

cross = False
playing = True

# Команды выборов
def choice(r,c):
    global cross
    print(f"{r}, {c}")
    pass


# Команда проверки
def check():
    pass

# Команда начала по новой
def new_game():
    pass

# Кнопки передают крест и нолик и позицию + меняется картинка на кнопке и она становиться не активной
# После каждого нажатия на кнопку нужна проверка победы и сброс поля через пару секунд с промтом кто победил


# Конфиг окна
main = Tk()
main.title("Tic-Tac-Toe")

# Конфиг текста
title = Label(text="Крестики нолики", font= ("Arial", 20))
title.grid(row=0, column=0, columnspan=3)

# Грузим картинки
cross = PhotoImage(file=r"Pics\cross1.png")
zero = PhotoImage(file=r"Pics\zero1.png")
na = PhotoImage(file = r"Pics\na1.png")

# Делаем кнопки
b00 = Button(image=na, command=lambda:choice(0,0)).grid(row=1, column=0)
b01 = Button(image=na, command=lambda:choice(0,1)).grid(row=1, column=1)
b02 = Button(image=na, command=lambda:choice(0,2)).grid(row=1, column=2)
b10 = Button(image=na, command=lambda:choice(1,0)).grid(row=2, column=0)
b11 = Button(image=na, command=lambda:choice(1,1)).grid(row=2, column=1)
b12 = Button(image=na, command=lambda:choice(1,2)).grid(row=2, column=2)
b20 = Button(image=na, command=lambda:choice(2,0)).grid(row=3, column=0)
b21 = Button(image=na, command=lambda:choice(2,1)).grid(row=3, column=1)
b22 = Button(image=na, command=lambda:choice(2,2)).grid(row=3, column=2)
    

main.mainloop()


from tkinter import *
import numpy

field = {
    "choices":numpy.matrix("0 0 0; 0 0 0; 0 0 0"), 
    "active":numpy.matrix("1 1 1; 1 2 1; 1 1 1")
         }

turns = {
    1:"cross",
    2:"circle"
        }


# Кнопки передают крест и нолик и позицию + меняется картинка на кнопке и она становиться не активной
# После каждого нажатия на кнопку нужна проверка победы и сброс поля через пару секунд с промтом кто победил

main = Tk()
main.title("Tic-Tac-Toe")
main.minsize(300,300)

title = Label(text="Крестики нолики")
title.grid(row=1, column=1)


# main.mainloop()


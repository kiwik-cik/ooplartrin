from tkinter import *#Импорт всех классов из библиотеки Tkinter.
from math import exp, sqrt, log#Импорт функций exp, sqrt, log из модуля math

def calculate_formula():#Определение функции calculate_formula(), которая будет вызываться при нажатии на кнопку "Вычислить"
    x = float(entry.get())#Получение значения x из текстового поля entry и преобразование его в тип float
    result = (exp(1/3 - x))**(1/5)) / sqrt(x**2 + x**4 + abs(log(abs(x - 3.4))))#Расчет значения выражения с использованием математических функций sqrt, exp, log и операторов
    result_label.config(text="Выражение = " + str(result))#Обновление текста в надписи result_label с результатом вычисления и добавлением префикса "Выражение ="
#Создание главного окна приложения с заголовком "Формула" и размером 300x100 пикселей
window = Tk()
window.title("Формула")
window.geometry('500x100')
#Создание надписи "Подсчет по формуле" с синим цветом текста и размещение в 2-м столбце и 0-й строке сетки окна
label1 = Label(window, text="Подсчет по формуле", fg = 'blue')
label1.grid(column=2, row=0)
#Создание надписи "x = " и размещение в 1-м столбце и 1-й строке сетки окна
label = Label(window, text="x = ")
label.grid(column=1, row=1)
#Создание текстового поля entry для ввода значения x и размещение в 2-м столбце и 1-й строке сетки окна
entry = Entry(window)
entry.grid(column=2, row=1)
#Создание кнопки "Вычислить" с командой calculate_formula для обработки нажатия на кнопку и размещение в 2-м столбце и 2-й строке сетки окна
calculate_button = Button(window, text="Вычислить", command=calculate_formula)
calculate_button.grid(column=2, row=2)
#Создание надписи result_label для отображения результата вычислений и размещение в 1-м столбце и 3-й строке сетки окна
result_label = Label(window, text="Выражение = ")
result_label.grid(column=1, row=3)
#Запуск главного цикла приложения с помощью метода mainloop(). Цикл обрабатывает события пользовательского интерфейса и отображает окно до тех пор, пока пользователь не закроет его
window.mainloop()

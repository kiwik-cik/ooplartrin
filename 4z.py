from tkinter import *#Импортируем библиотеку tkinter
from math import exp, sqrt, log#Импортируем функции exp, sqrt, log из модуля math
#Определяем функцию calculate_formula()
def calculate_formula():
    x = float(entry.get())#Получаем значение из поля ввода и преобразуем его в число типа float
    result =  (sqrt(exp(1/3 - x)**5)) / sqrt(x ** 2 + x ** 4 + abs(log(abs(x - 3.4))))#Вычисляем значение формулы
    result_label.config(text="Выражение =  " + str(result))#Устанавливаем текст для метки с результатом
#Создаем окно приложения
window = Tk()
window.title("Формула")#Устанавливаем заголовок окна
window.geometry('400x200')
#Создаем метку с текстом "x = "
label = Label(window, text="x = ")
label.grid(column = 1, row = 0)#Устанавливаем позицию метки на окне

entry = Entry(window)#Создаем поле ввода
entry.grid(column = 150, row = 20)#Устанавливаем позицию поля ввода на окне

calculate_button = Button(window, text="Вычислить", command=calculate_formula)#Создаем кнопку "Вычислить" с командой calculate_formula()
calculate_button.place(column = 50, row =50)#Устанавливаем позицию кнопки "Вычислить" на окне

result_label = Label(window, text="Выражение =  ")#Создаем метку с текстом "Выражение = "
result_label.place(column = 20, row =80)#Устанавливаем позицию метки с результатом на окне

window.mainloop()#Запускаем главный цикл обработки событий

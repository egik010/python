# Поработайте с переменными, создайте несколько, выведите на экран, запросите
# у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

first_variable = 12
second_variable = '12'

print(F'first_variable = {first_variable} second_variable = {second_variable}')
print(F'Тип переменной first_variable = {type(first_variable)}'
      F'.  Тип переменной second_variable = {type(second_variable)}')

number_variable1 = int(input("Введите 1 число: "))
number_variable2 = int(input("Введите 2 число: "))
print(F'Вы ввели 1 число: {number_variable1}. 2 число: {number_variable2}')

str_variable = input('Введите строку: ')
print(F'Вы ввели строку: {str_variable}')

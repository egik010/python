# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(value1, value2, value3):
    # print(value1, value2, value3)
    my_list = [value1, value2, value3]
    my_list.sort()
    return my_list[-1] + my_list[-2]


print(my_func(int(input('Введите 1 число: ')), int(input('Введите 2 число: ')), int(input('Введите 3 число: '))))

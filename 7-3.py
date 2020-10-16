# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __str__(self):  # хочется переопределить для print
        return str(self.number_cells)

    def __add__(self, other):  # +
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):  # -
        my_sub = self.number_cells - other.number_cells
        if my_sub > 0:
            return Cell(my_sub)
        else:
            print('Ошибка, результат вычитания клеток меньше 0')
            return -1

    def __mul__(self, other):  # *
        return Cell(self.number_cells * other.number_cells)

    def __truediv__(self, other):  # / не понял почему в лекции было floordiv
        return Cell(self.number_cells // other.number_cells)

    def make_order(self, number):
        my_str = '*' * self.number_cells
        i = 1
        while i <= self.number_cells // number:
            k = number * i + (i-1)
            my_str = my_str[:k] + '\n' + my_str[k:]
            i += 1
        print(my_str)


c1 = Cell(11)
c2 = Cell(5)
c3 = c1 + c2
print(c3)
c3 = c1 - c2
print(c3)
c3 = c1 / c2
print(c3)
c3 = c1 * c2
print(c3)

c1.make_order(3)

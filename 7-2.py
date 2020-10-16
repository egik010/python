# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def fabric_cons(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.v = size

    @property
    def fabric_cons(self):
        print(F'Расход ткани на пальто "{self.name}" составит {(self.v / 6.5 + 0.5):.2f} ')


class Suit(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.h = size

    @property
    def fabric_cons(self):
        print(F'Расход ткани на костюм "{self.name}" составит {(2 * self.h + 0.3):.2f} ')


c = Coat('Осеннее', 48)
s = Suit('Смокинг', 50)

c.fabric_cons
s.fabric_cons

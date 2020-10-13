# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police  # Булево

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(F'машина повернула {direction}')

    def show_speed(self):
        print(F'Скорость астомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(F'Скорость городского астомобиля {self.speed}')
        if self.speed > 60:
            print(F'Внимание вы первысили скорость на {self.speed - 60} км/ч')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        print(F'Скорость рабочего астомобиля {self.speed}')

class PoliceCar(Car):
    pass

t_car = TownCar(65, 'Зеленый', 'Еда', 0)
t_car.show_speed()

p_car = PoliceCar(90, 'Голубой', 'Джип', 1)
if p_car.is_police:
    print(F'Машина {p_car.color}, {p_car.name} является полчицейской машиной')
else:
    print(F'Машина {p_car.color} цвет, {p_car.name} Не является полчицейской машиной')

s_car = SportCar (110, 'Красный', 'бензин', 0)
print(F'У нас машина {s_car.color} цвет, {s_car.name}:')
s_car.go()
s_car.turn('Налево')
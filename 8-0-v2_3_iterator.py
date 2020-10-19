import random


class Rnd3:
    def rnd(self):
        self.rnd_15 = random.sample(range(1, 91), 15)

    def del_3(self):
        self.s1 = self.rnd_15[0:5]
        self.s2 = self.rnd_15[5:10]
        self.s3 = self.rnd_15[10:15]
        self.s1.sort()
        self.s2.sort()
        self.s3.sort()

    def add_space(self):
        for i in range(1, 5):
            self.s1.insert(random.randint(1, 5), ' ')
            self.s2.insert(random.randint(1, 5), ' ')
            self.s3.insert(random.randint(1, 5), ' ')

    def create_card(self):
        self.card = self.s1 + self.s2 + self.s3

    def v_str(self):
        for i, j in enumerate(self.card, 0):
            self.card[i] = str(self.card[i])

    def prn(self):
        print('-' * 5, self.name, '-' * (29 - len(self.name)))
        print('%4s' * 9 % tuple(self.card[0:9]))
        print('%4s' * 9 % tuple(self.card[9:18]))
        print('%4s' * 9 % tuple(self.card[18:27]))
        print('-' * 36)


class Gamer(Rnd3):
    def __init__(self, name):
        self.name = name
        self.kol_minus = 0
        self.flag = 0
        self._i = -1
        self.rnd()
        self.del_3()
        self.add_space()
        self.create_card()
        self.v_str()

    def __iter__(self):
        if self._i == len(self.card):  # !!!! обнуляем итератор!
            return self.__class__(self.card)  # !!!!!!!
        return self

    def __next__(self):
        self._i += 1
        if self._i < len(self.card):
            return self._i
        else:
            raise StopIteration


class Game():
    def __init__(self):
        self.g1 = Gamer('Ваша карточка')
        self.g2 = Gamer('Карточка компьютера')
        self.run()

    def find_karta(self, bar, obj):
        flag = False
        for x in obj:
            if obj.card[x] == str(bar):
                obj.card[x] = '-'
                flag = True
        return flag

    def run(self):
        self.barrel = random.sample(range(1, 91), 90)
        i = True
        while i:
            print('\n\n выпал БОЧЕНОК -', self.barrel[0], '  Осталось -', len(self.barrel) - 1)
            self.g1.prn()
            self.g2.prn()
            vvod = 't'
            while vvod != 'y' and vvod != 'n':
                vvod = input('Зачеркнуть цифру? (y/n): ')

            self.g1.flag = self.find_karta(self.barrel[0], self.g1)

            if self.find_karta(self.barrel[0], self.g2):
                self.g2.kol_minus += 1

            if vvod == 'y' and self.g1.flag == False:
                print('Игрок проиграл!!!! нет такой цифры')
                i = False

            if vvod == 'y' and self.g1.flag == True:
                self.g1.kol_minus += 1

            if vvod == 'n' and self.g1.flag:
                print('Игрок проиграл!!!! есть такая цифра')
                i = False

            del self.barrel[0]  # удаляем из списка выпавший боченок

            if (self.g1.kol_minus == 15):
                print('Выиграл ИГРОК')
                i = False

            if (self.g2.kol_minus == 15):
                print('Выиграл КОМПЬЮТЕР')
                i = False


go = Game()

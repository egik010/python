# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

listing = list(input('Введите строку из нескольких слов через пробел ').split())
number = 1
for i in listing:
    if len(i) >= 10:
        print(number, i[:10])
    else:
        print(number, i)
    number += 1

# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

listing = list(input('Введите список через пробел: ').split())
listing2 = []
i = 0
while i < (len(listing) - 1):
    listing2.append(listing[i + 1])
    listing2.append(listing[i])
    i += 2

if len(listing) % 2 != 0:
    listing2.append(listing[-1])

print(listing2)

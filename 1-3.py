# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input('Введите число n: '))
i = 0
result = 0
string = ''

while i < n:
    i += 1
    string += str(n)
    result += int(string)

print(result)

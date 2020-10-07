# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

my_str = ''
for i in range(1, 4):
    a = random.randint(1, 10)
    my_str += str(a) + ' '

print('записали: ', my_str)

with open('5-5-out.txt', 'w', encoding="utf-8") as f:  # записали в файл
    f.write(my_str)

my_str = ''
with open("5-5-out.txt", encoding="utf-8") as f_obj:  # считали из файла
    for i in f_obj:
        my_str += i

my_sum = 0
for i in list(my_str):
    if i != ' ':
        my_sum += int(i)
print('сумма чисел: ', my_sum)

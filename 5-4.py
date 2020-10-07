# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
# ************************************
# 5-4.txt - как в задании (Ctrl-C - Ctrl-V)

my_str = ''
with open("5-4.txt", encoding="utf-8") as f_obj:  # под винду7
    for i in f_obj:
        if i.split()[0] == 'One':
            my_str += 'Один' + ' ' + i.split()[1] + ' ' + i.split()[2] + '\n'
        elif i.split()[0] == 'Two':
            my_str += 'Два' + ' ' + i.split()[1] + ' ' + i.split()[2] + '\n'
        elif i.split()[0] == 'Three':
            my_str += 'Три' + ' ' + i.split()[1] + ' ' + i.split()[2] + '\n'
        elif i.split()[0] == 'Four':
            my_str += 'Четыре' + ' ' + i.split()[1] + ' ' + i.split()[2] + '\n'

with open('5-4-out.txt', 'w', encoding="utf-8") as f:
    f.write(my_str)

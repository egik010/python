# Создать текстовый файл(не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.
# ****************
# 5-2.txt
# str1 str1_2
# str2
# str3
# str4
# str5

with open("5-2.txt", encoding="utf-8") as f_obj:
    i = 0
    for line in f_obj:
        i += 1
        print(len([x for x in line.split()]))

print(i)

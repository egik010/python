# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
my_sum = 0
print('Введите числа через пробел, для завершения работы введите через пробел"q"')
while True:
    my_list = list(map(str, input().split()))
    if 'q' in my_list:  # как говорилось проверка на неправильный ввод не прводилась. все разделено пробелами
        print('Выход!')
        my_list = my_list[:my_list.index('q')]
        my_sum += sum([int(x) for x in my_list])
        print(my_sum)
        break
    my_sum += sum([int(x) for x in my_list])
    print(my_sum)

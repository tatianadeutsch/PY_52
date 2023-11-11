""""
Часть 4. Списки
"""

def elem_list(list_1):
    """
    1. Используя операции индексирования и среза
    выведите на экран первый и третий элементы списка
    [1, 2, 3 ,4 ,5], а также срез списка из первых
    трех элементов.
    """
    return (f'Первый и третий элементы списка {list_1} - '
      f' {list_1[0]}, {list_1[2]} \n'
      f'Срез списка {list_1} из первых трех элементов - '
      f'{list_1[:3]}')


def replace_elem_of_list(list_1):
    """
    2. Дан список [«Ростов», «+», «на», «-», «Дону»].
    Исправьте плюс на дефис и выведите название
    города на экран использовав доступ к элементам
    списка по индексам
    """
    search_elem = list_1.index('+')
    list_1[search_elem] = '-'
    list_join = "".join(list_1)

    return list_join


def digit_or_alpha_of_list(list_1):
    """
    3. Дан список [«a», «s», «1», «a», «32», «23»].
    Разбейте его на два списка:
    только с буквами и только с числами.
    """
    alpha_list = []
    digit_list = []

    for elem in list_1:
        if elem.isalpha():
            alpha_list.append(elem)
        if elem.isdigit():
            digit_list.append(int(elem))

    return alpha_list, digit_list


def pop_and_revers_in_alpha_list_of_prev_func(list_2):
    """
    4. В предыдущей задаче должен был получиться список
    из букв. Используя методы списков: удалите из него
    последний элемент, сделайте реверсию списка.
    """
    list_2[0].pop()
    list_2[0].reverse()

    return list_2[0]

def result_list_to_set(list_1):
    """
    5. Преобразуйте список [«a», «s», «1», «a», «32», «23»]
    в set и выведите на экран. Что изменилось?
    """
    list_to_set = set(list_1)

    return list_to_set


# 1
print(elem_list([1, 1, 3, 4, 5]))

# 2
print(replace_elem_of_list(['Ростов', '+', 'на', '-', 'Дону']))

# 3
print(digit_or_alpha_of_list(['a', 's', '1', 'a', '32', '23']))

# 4
ref_func = digit_or_alpha_of_list(['a', 's', '1', 'a', '32', '23'])
print(pop_and_revers_in_alpha_list_of_prev_func(ref_func))

# 5
list_1 = ['a', 's', '1', 'a', '32', '23']
print(f'После преобразования списка {result_list_to_set(list_1)} '
      f'в множество {result_list_to_set(list_1)} из списка "выпал" повторяющийся элемент "а",- '
      f'поскольку Set может содержать только уникальные значения.')
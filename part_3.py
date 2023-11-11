"""
Часть 3. Во всех заданиях данной группы требуется
вывести логическое значение True, если приведенное
высказывание для предложенных исходных данных является истинным,
и значение False в противном случае.
Все числа, для которых указано количество цифр
(двузначное число, трехзначное число и т. д.),
считаются целыми положительными.
"""


def int_number_is_positiv(a):
    """
    1. Дано целое число A.
    Проверить истинность высказывания: «Число A
    является положительным»
    """
    return a >= 0


def int_number_is_odd(a):
    """
    2. Дано целое число A.
    Проверить истинность высказывания:
    «Число A является нечетным».
    """
    return a % 2 != 0


def int_number_is_even(a):
    """
    3. Дано целое число A.
    Проверить истинность высказывания:
    «Число A является четным».
    """
    return a % 2 == 0


def inequality_and_true(a, b):
    """
    4. Даны два целых числа: A, B.
    Проверить истинность высказывания:
    «Справедливы неравенства A > 2 и B ≤ 3».
    """
    return a > 2 and b <= 3

def inequality_or_true(a, b):
    """
    5. Даны два целых числа: A, B.
    Проверить истинность высказывания:
    «Справедливы неравенства A ≥ 0 или B < −2».
    """
    return a >= 0 or b < -2


def double_inequality(a, b, c):
    """
    6. Даны три целых числа: A, B, C.
    Проверить истинность высказывания:
    «Справедливо двойное неравенство A < B < _C_».
    """
    return a < b < c


def number_between_number(a, b, c):
    """
    7. Даны три целых числа: A, B, C.
    Проверить истинность высказывания:
    «Число B находится между числами A и _C_».
    """
    return a < b < c


def numbers_are_odd(a, b):
    """
    8. Даны два целых числа: A, B.
    Проверить истинность высказывания:
    «Каждое из чисел A и B нечетное».
    """
    return a % 2 != 0 and b % 2 != 0


def number_or_number_is_odd(a, b):
    """
    9. Даны два целых числа: A, B.
    Проверить истинность высказывания:
    «Хотя бы одно из чисел A и B нечетное».
    """
    return a % 2 != 0 or b % 2 != 0

def only_number_or_number_is_odd(a, b):
    """
    10. Даны два целых числа: A, B.
    Проверить истинность высказывания:
    «Ровно одно из чисел A и B нечетное»
    """
    return (a % 2 != 0 ^ b % 2 != 0) or (b % 2 != 0 ^ a % 2 != 0)


# 1
int_number_a = int(input('Целое число A: \n'))
print(f'«Число {int_number_a} является положительным»: '
      f'{int_number_is_positiv(int_number_a)} \n')


# 2
int_number_a = int(input('Целое число A: \n'))
print(f'«Число {int_number_a} является нечетным»: '
      f'{int_number_is_odd(int_number_a)} \n')


# 3
int_number_a = int(input('Целое число A: \n'))
print(f'«Число {int_number_a} является четным»: '
      f'{int_number_is_even(int_number_a)} \n')

#  4
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
print(f'Справедливы неравенства {int_number_a} > 2 и '
      f'{int_number_b} ≤ 3»: {inequality_and_true(int_number_a, int_number_b)} \n')


# 5
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
print(f'Справедливы неравенства {int_number_a} > 2 и '
      f'{int_number_b} ≤ 3: {inequality_or_true(int_number_a, int_number_b)} \n')


# 6
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
int_number_c = int(input('Целое число C: \n'))

print(f'Справедливо двойное неравенство '
      f'{int_number_a} < {int_number_b} < {int_number_c}: '
      f'{double_inequality(int_number_a, int_number_b, int_number_c)} \n')


# 7
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
int_number_c = int(input('Целое число C: \n'))

print(f'Число {int_number_b} находится '
      f'между {int_number_a} и {int_number_c}: '
      f'{number_between_number(int_number_a, int_number_b, int_number_c)} \n')


# 8
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
print(f'Каждое из чисел {int_number_a} и {int_number_b} '
      f'нечетное: {numbers_are_odd(int_number_a, int_number_b)} \n')


# 9
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
print(f'Хотя бы одно из чисел {int_number_a} и {int_number_b} '
      f'нечетное: {number_or_number_is_odd(int_number_a, int_number_b)} \n')


# 10
int_number_a = int(input('Целое число A: \n'))
int_number_b = int(input('Целое число B: \n'))
print(f'Ровно одно из чисел {int_number_a} и {int_number_b} '
      f'нечетное: {only_number_or_number_is_odd(int_number_a, int_number_b)} \n')
"""
Часть 2. Все входные и выходные данные в заданиях этой группы
являются целыми числами.
Все числа, для которых указано количество цифр
(двузначное число, трехзначное число и т. д.), считаются положительными.
"""


def cm_in_m(l):
    """
    1. Дано расстояние L в сантиметрах.
    Используя операцию деления нацело,
    найти количество полных метров в нем (1 метр = 100 см
    """
    m = l // 100

    return m


def kg_in_t(m):
    """
    2. Дана масса M в килограммах.
    Используя операцию деления нацело,
    найти количество полных тонн в ней
    (1 тонна = 1000 кг).
    """
    t = m // 1000

    return t


def byte_in_kilobyte(byte):
    """
    3. Дан размер файла в байтах.
    Используя операцию деления нацело,
    найти количество полных килобайтов,
    которые занимает данный файл (1 килобайт = 1024 байта).
    """
    kb = byte // 1024

    return kb


def count_segments(a, b):
    """
    4. Даны целые положительные числа A и B (A > B).
    На отрезке длины A размещено максимально
    возможное количество отрезков длины B (без наложений).
    Используя операцию деления нацело,
    найти количество отрезков B, размещенных на отрезке A.
    """
    count_segments = a // b

    return count_segments


def count_segments_plus_rest_length(a, b):
    """
    5. Даны целые положительные числа A и B (A > B).
    На отрезке длины A размещено максимально возможное
    количество отрезков длины B (без наложений).
    Используя операцию взятия остатка от деления нацело,
    найти длину незанятой части отрезка A.
    """
    rest_length = a % b

    return rest_length


def part_two_digit_number(a):
    """
    6. Дано двузначное число. Вывести вначале его левую цифру
    (десятки), а затем — его правую цифру (единицы).
    Для нахождения десятков использовать операцию
    деления нацело, для нахождения единиц —
    операцию взятия остатка от деления.
    """
    left_part_numper = a // 10
    right_part_number = a % 10

    return left_part_numper, right_part_number


def sum_and_mult_of_two_digit_number(a):
    """
    7. Дано двузначное число. Найти сумму и произведение его цифр.
    """
    left_part_numper = a // 10
    right_part_number = a % 10
    sum_digit = left_part_numper + right_part_number
    mult_digit = left_part_numper * right_part_number

    return sum_digit, mult_digit


def change_site_of_two_digit_number(a):
    """
    8. Дано двузначное число. Вывести число, полученное
    при перестановке цифр исходного числа.
    """
    left_part_numper = a // 10
    right_part_number = a % 10
    change_number = int(str(right_part_number) + str(left_part_numper))

    return change_number


def hundred_of_three_digit_number(a):
    """
       9. Дано трехзначное число.
    Используя одну операцию деления нацело,
    вывести первую цифру данного числа (сотни).
    """
    hundred_part_numper = a // 100

    return hundred_part_numper


def tens_and_units_of_three_digit_number(a):
    """
        10. Дано трехзначное число.
    Вывести вначале его последнюю цифру (единицы),
    а затем — его среднюю цифру (десятки).
    """
    units = a % 10
    tens = a // 10 % 10

    return units, tens


not_null = "Укажите значение больше 0. "


# 1
l = abs(int(input("Расстояние L: \n")))

if l != 0:
    print(f'В {l} см - полных {cm_in_m(l)} м')
else:
    print(not_null)


# 2
m = abs(int(input("Масса m: \n")))

if m != 0:
    print(f'В {m} кг полных {kg_in_t(m)} т \n')
else:
    print(not_null)


# 3
file_size = abs(int(input("Размер файла в байтах: \n")))

if file_size != 0:
    print(f'В файле размером {file_size} байт - {byte_in_kilobyte(file_size)} '
          f'полных килобайтов(-а). \n')
else:
    print()


# 4
length_a = abs(int(input("Число А: \n")))
length_b = abs(int(input("Число B: \n")))

if ((length_a != 0 and length_b != 0)
        and (length_a > length_b)):
    print(f'На отрезке А длиной {length_a} '
          f'размещены {count_segments(length_a, length_b)} '
          f'отрезков В длиной {length_b}. \n')
else:
    print(not_null, "Значение А > B")


# 5
length_a = abs(int(input("Число А: \n")))
length_b = abs(int(input("Число B: \n")))

if ((length_a != 0 and length_b != 0)
        and (length_a > length_b)):
    print(f'Длина незанятой части на отрезке А '
          f'составляет {count_segments_plus_rest_length(length_a, length_b)} \n')
else:
    print(not_null, "Значение А > B")


# 6
two_digit_number = int(input('Двухзначное число: \n'))

if two_digit_number > 0 and len(str(two_digit_number)) == 2:
    print(f'В числе {two_digit_number}: %d десятков '
          f'и %d единиц. \n'
          %(part_two_digit_number(two_digit_number)))
else:
    print(not_null, "Число должно быть двухзначным.")


# 7
two_digit_number = int(input('Двухзначное число: \n'))

if two_digit_number > 0 and len(str(two_digit_number)) == 2:
    print(f'В числе {two_digit_number} сумма его цифр = %d, '
          f'произведение его цифр = %d. \n'
          %(sum_and_mult_of_two_digit_number(two_digit_number)))
else:
    print(not_null, "Число должно быть двухзначным.")


# 8
two_digit_number = int(input('Двухзначное число: \n'))

if two_digit_number > 0 and len(str(two_digit_number)) == 2:
    print(f'При перестановке цифр в числе {two_digit_number} '
          f'получается {change_site_of_two_digit_number(two_digit_number)}. \n')
else:
    print(not_null, "Число должно быть двухзначным.")


# 9
three_digit_number = int(input('Трехзначное число: \n'))

if three_digit_number > 0 and len(str(three_digit_number)) == 3:
    print(f'Число {three_digit_number} содержит '
          f'{hundred_of_three_digit_number(three_digit_number)} сотню(-и, -ен). \n')
else:
    print(not_null, "Число должно быть трехзначным.")


# 10
three_digit_number = int(input('Трехзначное число: \n'))

if three_digit_number > 0 and len(str(three_digit_number)) == 3:
    print(f'Число {three_digit_number} содержит '
          f'%d единицы(-иц) и %d десятка(-ов). '
          %(tens_and_units_of_three_digit_number(three_digit_number)))
else:
    print(not_null, "Число должно быть трехзначным.")


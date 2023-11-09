"""
Часть 1. Все входные и выходные данные в заданиях этой группы
являются вещественными числами.
"""

import math


def perimeter_squere(a):
    """
    1. Дана сторона квадрата a. Найти его периметр P = 4·a
    """
    p = 4 * a

    return p


def area_squere(a):
    """
    2. Дана сторона квадрата a. Найти его площадь{{ S = a2}}
    """
    s = a ** 2

    return s


def area_and_perimetr_restangle(a, b):
    """
    3. Даны стороны прямоугольника a и b.
    Найти его площадь S = a·b и периметр P = 2·(a + b)
    """
    s = a * b
    p = 2 * (a + b)

    return s, p

def length_circum(d):
    """
    4. Дан диаметр окружности d.
    Найти ее длину{{ L = π·d, π = 3.14}}
    """
    pi = 3.14
    l = pi * d

    return l

def volume_and_area_cube(a):
    """
    5. Дана длина ребра куба a.
    Найти объем куба V = a3 и площадь его поверхности S = 6·a2
    """
    v = a**3
    s = 6 * a**2

    return v, s


def volume_and_area_parallelepiped(a, b, c):
    """
    6. Даны длины ребер a, b, c прямоугольного параллелепипеда.
    Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)
    """
    v = a * b * c
    s = 2 * (a * b + b * c + a * c)

    return v, s


def length_and_area_circum(r):
    """
    7. Найти длину окружности L и площадь круга S заданного радиуса R:
    L = 2·π·R, S = π·R2, π = 3.14
    """
    pi = 3.14
    l = 2 * pi * r
    s = pi * r**2

    return l, s


def average(a, b):
    """
    8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
    """
    average = (a + b) / 2

    return average


def geometric_average(a, b):
    """
    9. Даны два неотрицательных числа a и b.
    Найти их среднее геометрическое,
    т. е. квадратный корень из их произведения: (a·b)1/2
    """
    geometric_average = math.sqrt(a * b)

    return geometric_average


def sum_diff_multip_quot_numbers_squere(a, b):
    """
    10. Даны два ненулевых числа.
    Найти сумму, разность, произведение и частное их квадратов.
    """
    sum_squere = a**2 + b**2
    diff_squere = a**2 - b**2
    mult_squere = a**2 * b**2
    quot_squere = a**2 / b**2

    return sum_squere, diff_squere, mult_squere, quot_squere



not_null = "Введите положительное число"


side_squere_a = float(input("Сторона квадрата: \n"))

if side_squere_a > 0:
    print(f'Периметр квадрата со стороной {side_squere_a} '
      f'равен {format(perimeter_squere(side_squere_a), ".2f")}\n')
else:
    print(not_null)


side_squere_a = float(input("Сторона квадрата: \n"))

if side_squere_a > 0:
    print(f'Площадь квадрата со стороной {side_squere_a} '
      f'равна {format(area_squere(side_squere_a), ".2f")}\n')
else:
    print(not_null)


side_restangle_a = float(input("Сторона прямоугольника a: \n"))
side_restangle_b = float(input("Сторона прямоугольника b: \n"))

if side_restangle_a > 0 and side_restangle_b > 0:
    print(f'Площадь прямоугольника со сторонами {side_restangle_a} и {side_restangle_b} '
      f'равна %.2f. \n'
      f'Периметр прямоугольника со сторонами {side_restangle_a} и {side_restangle_b} '
      f'равен %.2f.' %(area_and_perimetr_restangle(side_restangle_a, side_restangle_b)), "\n")
else:
    print(not_null)


diameter_circum_d = float(input("Диаметр окружности d: \n"))

if diameter_circum_d > 0:
    print(f'Длина окружности с диаметром {diameter_circum_d} '
      f'равна {format(length_circum(diameter_circum_d), ".2f")}. \n')
else:
    print(not_null)


length_edge_cube_a = float(input("Длина ребра куба: \n"))

if length_edge_cube_a > 0:
    print(f'Объем куба с ребром {length_edge_cube_a} '
      f'равен %.2f. \n'
      f'Площадь поверхности куба с ребром {length_edge_cube_a} '
      f'равна %.2f.' %(volume_and_area_cube(length_edge_cube_a)), "\n")
else:
    print(not_null)


length_edge_parallelepiped_a = float(input("Длина ребра параллелепипеда a: \n"))
length_edge_parallelepiped_b = float(input("Длина ребра параллелепипеда b: \n"))
length_edge_parallelepiped_c = float(input("Длина ребра параллелепипеда c: \n"))

if (length_edge_parallelepiped_a > 0 and length_edge_parallelepiped_b > 0 and
        length_edge_parallelepiped_c > 0):
    print(f'Объем прямоугольного параллелепипеда с ребрами длиной '
      f'{length_edge_parallelepiped_a}, {length_edge_parallelepiped_b}, '
      f'{length_edge_parallelepiped_c} '
      f'равен %.2f \n'
      f'Площадь поверхности прямоугольного параллелепипеда с ребрами длиной '
      f'{length_edge_parallelepiped_a}, {length_edge_parallelepiped_b}, '
      f'{length_edge_parallelepiped_c} '
      f'равна %.2f.' %(volume_and_area_parallelepiped(
    length_edge_parallelepiped_a,
    length_edge_parallelepiped_b,
    length_edge_parallelepiped_c)), "\n")
else:
    print(not_null)


radius_circum_r = float(input("Радиус окружности r: \n"))

if radius_circum_r > 0:
    print(f'Длина окружности с радиусом {radius_circum_r} '
      f'равна %.2f \n'
      f'Площадь круга с радиусом {radius_circum_r} '
      f'равна %.2f'
      %(length_and_area_circum(radius_circum_r)), "\n")
else:
    print(not_null)


number_a = float(input("Число a: \n"))
number_b = float(input("Число b: \n"))
print(f'Среднее арифметическое чисел {number_a} и {number_b} '
      f'равно {format(average(number_a, number_b), ".2f")} \n')

positv_number_a = float(input("Число a: \n"))
positv_number_b = float(input("Число b: \n"))

if positv_number_a > 0 and positv_number_b > 0:
    print(f'Среднее геометрическое чисел '
      f'{positv_number_a} и {positv_number_b} '
      f'равно {format(geometric_average(positv_number_a, positv_number_b), ".2f")}')
else:
    print(not_null)


a = float(input("Число a: \n"))
b = float(input("Число b: \n"))

if a != 0 and b != 0:
    print(f'Сумма квадратов чисел {a} и {b} равна '
          f'%.2f. \n'
          f'Разность квадратов чисел {a} и {b} равна '
          f'%.2f. \n'
          f'Произведение квадратов чисел {a} и {b} равно '
          f'%.2f. \n'
          f'Частное квадратов чисел {a} и {b} равно '
          f'%.2f. \n'
          %(sum_diff_multip_quot_numbers_squere(a, b)))
else:
    print("Введите ненулевое число.")


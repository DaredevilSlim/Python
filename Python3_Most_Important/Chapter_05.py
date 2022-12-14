#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal
from fractions import Fraction
import math
import random

# Глава 5
# Числа
print('Числа:')
# Язык Python 3 поддерживает следующие числовые типы:
# int - целые числа. Размер числа ограничен лишь объемом оперативной памяти;
# float - вещественные числа;
# complex - комплексные числа.
# Операции над числами разных типов возвращают число, имеющее более сложный тип из типов, участвующих в операции. Целые
# числа имеют самый простой тип, далее идут вещественные числа и самый сложный тип - комплексные числа. Таким образом,
# если в операции участвуют целое число и вещественное, то целое число будет автоматически преобразовано в вещественное
# число, а затем произведена операция над вещественными числами. Результатом этой операции будет вещественное число.
# Создать объект целочисленного типа можно обычным способом:
x = 0
y = 10
z = -80
print(x, y, z)
# Также можно указать число в двоичной, восьмеричной или шестнадцатеричной форме. Такие числа будут автоматически
# преобразованы в десятичные целые числа.
# Двоичные числа начинаются с комбинации символов 0b (или 0B) и содержит цифры 0 или 1:
print('Двоичные числа:')
print(0b11111111, 0b101101)
# Восьмеричные числа начинаются с нуля и следующей за ним латинской буквой o (регистр не имеет значения) и содержит
# цифры от 0 до 7:
print('Восьмеричные числа:')
print(0o7, 0o12, 0o777, 0O7, 0O12, 0O777)
# Шестнадцатеричные числа начинаются с комбинации символов 0x (или 0X) и могут содержать цифры от 0 до 9 и буквы от A
# до F (регистр букв не имеет значения):
print('Шестнадцатеричные числа:')
print(0X9, 0XA, 0x10, 0xFFF, 0xfff)
# Вещественное число может содержать точку и (или) быть представлено в экспоненциальной форме с буквой E (регистр букв
# не имеет значения). При выполнении операций над вещественными числами следует учитывать ограничения точности
# вычислений:
print('Вещественное число:')
print(0.3 - 0.1 - 0.1 - 0.1)
# Ожидаемым был бы результат 0.0, но, как видно из примера, было получено совсем другое значение. Если необходимо
# производить операции с фиксированной точностью, то следует использовать модуль decimal:
# Подключение модуля decimal:
# from decimal import Decimal
print('Использование метода Decimal:')
print(Decimal('0.3') - Decimal('0.1') - Decimal('0.1') - Decimal('0.1'))
# Кроме того, можно использовать дроби, поддержка которых содержится в модуле fractions. При создании дроби можно как
# указать два числа: числитель и знаменатель, так и одно число или строку, содержащую число, которое будет преобразовано
# в дробь.
# Подключение модуля Fraction:
# from fractions import Fraction
print('Использование метода Fraction:')
print(Fraction(4, 5))
print(Fraction(1, 2))
print(Fraction('0.5'))
print(Fraction(0.5))
# Над дробями можно производить арифметические операции, как и над обычными числами:
print(Fraction(9, 5) - Fraction(2, 3))
print(Fraction('0.3') - Fraction('0.1') - Fraction('0.1') - Fraction('0.1'))
print(float(Fraction(0, 1)))
# Комплексные числа записываются в формате:
# <Вещественная часть> + <Мнимая часть>J
# Здесь буква J может стоять в любом регистре.
print('Комплексные числа:')
print(2 + 5J, 8j)


# 5.1 Встроенные функции и методы для работы с числами
print('Встроенные функции и методы для работы с числами:')
# Для работы с числами предназначены следующие встроенные функции:
print('Для работы с числами предназначены следующие встроенные функции:')
# int([<Объект>[, <Система счисления>]]) - преобразует объект в целое число. Во втором параметре можно указать систему
# счисления преобразуемого числа (значение по умолчанию 10).
print('int([<Объект>[, <Система счисления>]]) - преобразует объект в целое число:')
print(int(7.5), int('71', 10), int('0o71', 8), int('0xA', 16))
print(int(), int('0b11111111', 2))
# float([<Число или строка>]) - преобразует целое число или строку в вещественное число:
print('float([<Число или строка>]) - преобразует целое число или строку в вещественное число:')
print(float(7), float('7.1'), float('12.'))
print(float('inf'), float('-Infinity'), float('nan'))
print(float())
# bin(<Число>) - преобразует десятичное число в двоичное. Возвращает строковое представление числа.
print('bin(<Число>) - преобразует десятичное число в двоичное:')
print(bin(255), bin(1), bin(-45))
# oct(<Число>) - преобразует десятичное число в восьмеричное. Возвращает строковое представление числа.
print('oct(<Число>) - преобразует десятичное число в восьмеричное:')
print(oct(7), oct(8), oct(64))
# hex(<Число>) - преобразует десятичное число в шестнадцатеричное. Возвращает строковое представление числа.
print('hex(<Число>) - преобразует десятичное число в шестнадцатеричное:')
print(hex(10), hex(16), hex(255))
# round(<Число>[, <Количество знаков после точки>]) - для чисел с дробной частью меньше 0.5 возвращает число,
# округленное до ближайшего меньшего целого, а для чисел с дробной частью больше 0.5 возвращает число, округленное до
# ближайшего большего целого. Если дробная часть равна 0.5, то округление производится до ближайшего четного числа.
print('round(<Число>[, <Количество знаков после точки>]) - округление вещественных чисел:')
print(round(0.49), round(0.50), round(0.51))
print(round(1.49), round(1.50), round(1.51))
print(round(2.49), round(2.50), round(2.51))
print(round(3.49), round(3.50), round(3.51))
# Во втором параметре можно указать желаемое количество знаков после запятой. Если оно не указано, используется
# значение 0 (т.е. число будет округлено до целого):
print(round(1.524, 2), round(1.525, 2), round(1.5555, 3))
# abs(<Число>) - возвращает абсолютное значение:
print('abs(<Число>) - возвращает абсолютное значение:')
print(abs(-10), abs(10), abs(-12.5))
# роw(<Число>, <Степень>[, <Делитель>]) - возводит <Число> в <Степень>:
print('роw(<Число>, <Степень>[, <Делитель>]) - возводит <Число> в <Степень>:')
print(pow(10, 2), 10 ** 2, pow(3, 3), 3 ** 3)
# Если указан третий параметр, то возвращается остаток от деления полученного результата на значение этого параметра:
print(pow(10, 2, 2), (10 ** 2) % 2, pow(3, 3, 2), (3 ** 3) % 2)
# max(<Список чисел через запятую>) - максимальное значение из списка:
print('max(<Список чисел через запятую>) - максимальное значение из списка:')
print(max(1, 2, 3), max(3, 2, 3, 1), max(1, 1.0), max(1.0, 1))
# min(<Список чисел через запятую>) - минимальное значение из списка:
print('min(<Список чисел через запятую>) - минимальное значение из списка:')
print(min(1, 2, 3), min(3, 2, 3, 1), min(1, 1.0), min(1.0, 1))
# sum(<Последовательность>[, <Начальное значение>]) - возвращает сумму значений элементов последовательности (например:
# списка, кортежа) плюс <Начальное значение>. Если второй параметр не указан, начальное значение принимается равным 0.
# Если последовательность пустая, то возвращается значение второго параметра.
print('sum(<Последовательность>[, <Начальное значение>]) - возвращает сумму значений элементов последовательности:')
print(sum((10, 20, 30, 40)), sum([10, 20, 30, 40]))
print(sum([10, 20, 30, 40], 2), sum([], 2))
# divmod(x, у) - возвращает кортеж из двух значений (x // y, x % y):
print('divmod(x, у) - возвращает кортеж из двух значений (x // y, x % y):')
print(divmod(13, 2))  # 13 == 6 * 2 + 1
print(13 // 2, 13 % 2)
print(divmod(13.5, 2.0))  # 13.0 == 6.0 * 2.0 + 1.5
print(13.5 // 2.0, 13.5 % 2.0)
# Следует понимать, что все типы данных, поддерживаемые Python, представляют собой классы. Класс float, представляющий
# вещественные числа, поддерживает следующие полезные методы:
# is_integer() - возвращает True, если заданное вещественное число не содержит дробной части, т.е. фактически
# представляет собой целое число:
print('is_integer() - возвращает True, если заданное вещественное число не содержит дробной части:')
print(2.0.is_integer())
print(2.3.is_integer())
# as_integer_ratio() - возвращает кортеж из двух целых чисел, представляющих собой числитель и знаменатель дроби,
# которая соответствует заданному числу:
print('as_integer_ratio() - возвращает кортеж из двух целых чисел:')
print(0.5.as_integer_ratio())
print(2.3.as_integer_ratio())


# 5.2 Модуль math. Математические функции
print('Модуль math. Математические функции:')
# Модуль math предоставляет дополнительные функции для работы с числами, а также стандартные константы. Прежде чем
# использовать модуль, необходимо подключить его с помощью инструкции:
# Примечание - Для работы с комплексными числами необходимо использовать модуль cmath.
# Модуль math предоставляет следующие стандартные константы:
print('Модуль math предоставляет следующие стандартные константы:')
# pi - возвращает число pi:
print('pi - возвращает число pi:')
print(math.pi)
# е - возвращает значение константы е:
print('е - возвращает значение константы е:')
print(math.e)
# Основные функции для работы с числами:
print('Основные функции для работы с числами:')
# sin(), cos(), tan() - стандартные тригонометрические функции (синус, косинус, тангенс). Значение указывается в
# радианах;
print('sin(), cos(), tan() - стандартные тригонометрические функции:')
# asin(), acos(), atan() - обратные тригонометрические функции (арксинус, арккосинус, арктангенс). Значение возвращается
# в радианах;
print('asin(), acos(), atan() - обратные тригонометрические функции:')
# degrees() - преобразует радианы в градусы:
print('degrees() - преобразует радианы в градусы:')
print(math.degrees(math.pi))
# radians() - преобразует градусы в радианы:
print('radians() - преобразует градусы в радианы:')
print(math.radians(180.0))
# ехр() - экспонента:
print('ехр() - экспонента:')
# log(<Число>[, <База>]) - логарифм по заданной базе. Если база не указана, вычисляется натуральный логарифм
# (по базе е):
print('log(<Число>[, <База>]) - логарифм по заданной базе:')
# log1O() - десятичный логарифм:
print('log1O() - десятичный логарифм:')
# log2() - логарифм по базе 2:
print('log2() - логарифм по базе 2:')
# sqrt() - квадратный корень:
print('sqrt() - квадратный корень:')
print(math.sqrt(100), math.sqrt(25))
# ceil() - значение, округленное до ближайшего большего целого:
print('ceil() - значение, округленное до ближайшего большего целого:')
print(math.ceil(5.49), math.ceil(5.50), math.ceil(5.51))
# floor() - значение, округленное до ближайшего меньшего целого:
print('floor() - значение, округленное до ближайшего меньшего целого:')
print(math.floor(5.49), math.floor(5.50), math.floor(5.51))
# pow(<Число>, <Степень>) - возводит <Число> в <Степень>:
print('pow(<Число>, <Степень>) - возводит <Число> в <Степень>:')
print(math.pow(10, 2), 10 ** 2, math.pow(3, 3), 3 ** 3)
# fabs() - абсолютное значение:
print('fabs() - абсолютное значение:')
print(math.fabs(10), math.fabs(-10), math.fabs(-12.5))
# fmod() - остаток от деления:
print('fmod() - остаток от деления:')
print(math.fmod(10, 5), 10 % 5, math.fmod(10, 3), 10 % 3)
# factorial() - факториал числа:
print('factorial() - факториал числа:')
print(math.factorial(5), math.factorial(6))
# fsum(<Список чисел>) - возвращает точную сумму чисел из заданного списка:
print('fsum(<Список чисел>) - возвращает точную сумму чисел из заданного списка:')
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))


# 5.3. Модуль random. Генерация случайных чисел
print('Модуль random. Генерация случайных чисел:')
# Модуль random позволяет генерировать случайные числа. Прежде чем использовать модуль, необходимо подключить его с
# помощью инструкции:
# import random
# Основные функции модуля random():
print('Основные функции модуля random():')
# random() - возвращает псевдослучайное число от 0.0 до 1.0:
print('random() - возвращает псевдослучайное число от 0.0 до 1.0:')
print(random.random())
print(random.random())
print(random.random())
# seed([<Параметр>][, version = 2] ) - настраивает генератор случайных чисел на новую последовательность. Если первый
# параметр не указан, в качестве базы для случайных чисел будет использовано системное время. Если значение первого
# параметра будет одинаковым, то генерируется одинаковое число:
print(random.seed(10))
print(random.random())
print(random.seed(10))
print(random.random())
# uniform(<Начало>, <Конец>) - возвращает псевдослучайное вещественное число в диапазоне от <Начало> до <Конец>:
print('uniform(<Начало>, <Конец>) - возвращает псевдослучайное вещественное число в диапазоне от <Начало> до <Конец>:')
print(random.uniform(0, 10))
print(random.uniform(0, 10))
# randint(<Начало>, <Конец>) - возвращает псевдослучайное целое число в диапазоне от <Начало> до <Конец>:
print('randint(<Начало>, <Конец>) - возвращает псевдослучайное целое число в диапазоне от <Начало> до <Конец>:')
print(random.randint(0, 10))
print(random.randint(0, 10))
# randrange([<Начало>, ]<Конец>[, <Шаг>] ) - возвращает случайный элемент из числовой последовательности. Параметры
# аналогичны параметрам функции range(). Можно сказать, что функция randrange «за кадром» создает диапазон, из которого
# и будут выбираться возвращаемые случайные числа:
print('randrange([<Начало>, ]<Конец>[, <Шаг>] ) - возвращает случайный элемент из числовой последовательности.')
print(random.randrange(10))
print(random.randrange(0, 10))
print(random.randrange(0, 10, 2))
# choice(<Последовательность>) - возвращает случайный элемент из заданной последовательности (строки, списка, кортежа):
print('choice(<Последовательность>) - случайный элемент из заданной последовательности (строки, списка, кортежа):')
print(random.choice('string'))  # Строка
print(random.choice(['s', 't', 'r', 'i', 'n', 'g']))  # Список
print(random.choice(('s', 't', 'r', 'i', 'n', 'g')))  # Кортеж
# shuffle(<Список>[, <Число от 0.0 до 1.О>]) - перемешивает элементы списка случайным образом. Если второй параметр
# не указан, то используется значение, возвращаемое функцией random(). Никакого результата при этом не возвращается.
print('shuffle(<Список>[, <Число от 0.0 до 1.О>]) - перемешивает элементы списка случайным образом:')
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
print(random.shuffle(arr))
print(arr)
# sample(<Последовательность>, <Количество элементов>) - возвращает список из указанного количества элементов, которые
# будут выбраны случайным образом из заданной последовательности. В качестве таковой можно указать любые объекты,
# поддерживающие итерации.
print('sample(<Последовательность>, <Количество элементов>) - возвращает список из указанного количества элементов:')
print(random.sample("string", 2))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(arr, 2))
print(arr)  # Сам список не изменяется
print(random.sample((1, 2, 3, 4, 5, 6, 7), 3))
print(random.sample(range(300), 5))
# Для примера создадим генератор паролей произвольной длины (test_00029.py). Для этого добавляем в список arr все
# разрешенные символы, а далее в цикле получаем случайный элемент с помощью функции choice(). По умолчанию будет
# выдаваться пароль из 8 символов.

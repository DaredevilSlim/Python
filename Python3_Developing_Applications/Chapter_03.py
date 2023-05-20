#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from decimal import Decimal   # Подключаем из модуля decimal содержащийся в нем объект Decimal

# Глава 3
# Операторы
# Оператор - языковая конструкция, выполняющая над переданными ему значениями (операндами) какое-либо элементарное
# действие (например, математическое сложение). Набор операторов, поддерживаемых Python, определен разработчиками этого
# языка и не может быть расширен (в отличие от набора поддерживаемых функций).

# 3.1. Математические операторы
# Производить операции над числами позволяют математические операторы:
# + - сложение
print(10 + 5)      # Целые числа
print(12.4 + 5.2)  # Вещественные числа
print(10 + 12.4)   # Целые и вещественные числа

# - - вычитание
print(10 - 5)      # Целые числа
print(12.4 - 5.2)  # Вещественные числа
print(12 - 5.2)    # Целые и вещественные числа

# * - умножение:
print(10 * 5)      # Целые числа
print(12.4 * 5.2)  # Вещественные числа
print(12 * 5.2)    # Целые и вещественные числа

# / - деление. Результатом деления всегда является вещественное число, даже если производится деление целых чисел.
print(10 / 5)      # Деление целых чисел без остатка
print(10 / 5)      # Деление целых чисел с остатком
print(10.0 / 5.0)  # Деление вещественных чисел
print(10.0 / 3.0)  # Деление вещественных чисел
print(10 / 5.0)    # Деление целого числа на вещественное
print(10.0 / 5)    # Деление вещественного числа на целое

# // - деление с округлением вниз. Остаток всегда отбрасывается.
print(10 // 5)      # Деление целых чисел без остатка
print(10 // 3)      # Деление целых чисел с остатком
print(10.0 // 5.0)  # Деление вещественных чисел
print(10.0 // 3.0)  # Деление вещественных чисел
print(10 // 5.0)    # Деление целого числа на вещественное
print(10 // 3.0)    # Деление целого числа на вещественное
print(10.0 // 5)    # Деление вещественного числа на целое
print(10.0 // 3)    # Деление вещественного числа на целое

# % - остаток от деления:
print(10 % 5)      # Деление целых чисел без остатка
print(10 % 3)      # Деление целых чисел с остатком
print(10.0 % 5.0)  # Операция над вещественными числами
print(10.0 % 3.0)  # Операция над вещественными числами
print(10 % 5.0)    # Операция над целыми и вещественными числами
print(10 % 3.0)    # Операция над целыми и вещественными числами
print(10.0 % 5)    # Операция над целыми и вещественными числами
print(10.0 % 3)    # Операция над целыми и вещественными числами

# ** - возведение в степень. Основание указывается первым операндом, показатель - вторым.
print(10 ** 2, 10.0 ** 2)

# унарный минус ( - ) - изменяет знак числа на противоположный:
print(-10, -10.0, -(-10), -(-10.0))

# унарный плюс ( +) - ничего не делает с числом:
print(+10, +10.0)
# Как видно из приведенных примеров, операции над числами разных типов возвращают число, имеющее более сложный из типов,
# участвующих в операции. Целые числа имеют самый простой тип, далее идут вещественные числа и самый сложный тип -
# комплексные числа. Таким образом, если в операции участвуют целое число и вещественное, то целое число будет
# автоматически преобразовано в вещественное число, затем будет произведена операция над вещественными числами, а
# результатом станет вещественное число.
# При выполнении операций над вещественными числами следует учитывать ограничения точности вычислений. Например,
# результат следующей операции может показаться странным:
print(0.3 - 0.1 - 0.1 - 0.1)
# Ожидаемым бьш бы результат 0.0, но, как видно из примера, мы получили совсем другой результат. Если необходимо
# производить операции с фиксированной точностью, следует использовать модуль decimal.
print(Decimal('0.3') - Decimal('0.1') - Decimal('0.1') - Decimal('0.1'))


# 3.2. Двоичные операторы
# Двоичные операторы предназначены для манипуляции отдельными битами:
# ~ - двоичная инверсия. Значение каждого бита заменяется на противоположное:
# x = 100  # 01100100
# x = ~x   # 10011011

# & - двоичное И:
# x = 100    # 01100100
# у = 75     # 01001011
# z = х & у  # 01000000

# | - двоичное ИЛИ:
# x = 100    # 01100100
# у = 75     # 01001011
# z = х | у  # 01101111

# ^ - двоичное исключающее ИЛИ:
# х = 100    # 01100100
# y = 250    # 11111010
# z = х ^ у  # 10011110

# << - сдвиг влево - сдвигает двоичное представление числа, заданного первым операндом, влево на количество разрядов,
# указанное вторым операндом, и заполняет разряды справа нулями:
# х = 100     # 01100100
# у = х << 1  # 11001000
# z = у << 1  # 10010000
# k = z << 2  # 01000000
# >> - сдвиг вправо - сдвигает двоичное представление числа, заданного первым операндом, вправо на количество разрядов,
# указанное вторым операндом, и заполняет разряды слева нулями, если число положительное, и единицами, если число
# отрицательное:
# х = 100     # 01100100
# у = х >> 1  # 00110010
# z = у >> 1  # 00011001
# k = z >> 2  # 00000110
# х = -127    # 10000001
# у = х >> 1  # 11000000
# z = у >> 2  # 11110000
# k = z << 1  # 11100000
# m = k >> 1  # 11110000


# 3.3. Операторы для работы с последовательностями
# Для работы с последовательностями предназначены следующие операторы:
# + - конкатенация (объединение):
print('Строка1' + 'Строка2')  # Конкатенация строк
print([1, 2, 3] + [4, 5, 6])  # Списки
print((1, 2, 3) + (4, 5, 6))  # Кортежи

# * - повторение. Повторяет последовательность из первого операнда количество раз, указанное вторым операндом.
print('s' * 20)    # Строки
print([1, 2] * 3)  # Списки
print((1, 2) * 3)  # Кортежи

# in - проверка на вхождение. Если значение, заданное первым операндом, входит в последовательность, указанную вторым
# операндом, то возвращается логическое значение True, в противном случае - False.
print('Строка' in 'Строка для поиска')  # Строки
print('Буква' in 'Строка для поиска')   # Строки
print(2 in [1, 2, 3], 4 in [1, 2, 3])   # Списки
print(2 in (1, 2, 3), 4 in (1, 2, 3))   # Кортежи

# not in - проверка на невхождение. Если значение, заданное первым операндом, не входит в последовательность, указанную
# вторым операндом, то возвращается значение True, в противном случае - False.
print('Строка' not in 'Строка для поиска')     # Строки
print('Буква' not in 'Строка для поиска')      # Строки
print(2 not in [1, 2, 3], 4 not in [1, 2, 3])  # Списки
print(2 not in (1, 2, 3), 4 not in (1, 2, 3))  # Кортежи


# 3.4. Операторы присваивания
# Операторы присваивания предназначены для сохранения значения в переменной:
# = - простое присваивание:
x = 5
print(x)

# += - присваивание со сложением - увеличивает значение переменной на величину из второго операнда:
x = 5
x += 10  # Эквивалентно х = х + 10
print(x)

# -= - присваивание с вычитанием - уменьшает значение переменной на величину из второго операнда:
x = 10
x -= 5  # Эквивалентно х = х - 5
print(x)

# *= - присваивание с умножением - умножает значение переменной на величину из второго операнда:
x = 10
x *= 5  # Эквивалентно х = х * 5
print(x)
# Будучи примененным к последовательности, оператор *= производит повторение:
s = '*'
s *= 20
print(s)

# /= - присваивание с делением - делит значение переменной на величину из второго операнда:
x = 10
x /= 3    # Эквивалентно х = х / 3
print(x)
x = 10.0
x /= 3.0  # Эквивалентно х = х / 3.0
print(x)

# //= - присваивание с делением и округлением вниз - делит значение переменной на величину из второго операнда и
# округляет результат вниз:
x = 10
x //= 3    # Эквивалентно х = х // 3
print(x)
x = 10.0
x //= 3.0  # Эквивалентно х = х // 3.0
print(x)

# %= - присваивание с делением по модулю - делит по модулю значение переменной на величину из второго операнда:
x = 10
x %= 2    # Эквивалентно х = х % 2
print(x)
x = 10.0
x %= 3.0  # Эквивалентно х = х % 3.0
print(x)

# ** =- присваивание с возведением в степень - возводит значение переменной в степень, заданную вторым операндом:
x = 10
x **= 2  # Эквивалентно х = х * 2
print(x)

# := (начиная с Python 3.8) - присваивание в составе сложного выражения (рассмотрен в главе 4).


# 3.5. Пустой оператор
# Пустой оператор pass ничего не делает:
pass                     # Ничего не делаем
pass                     # Снова ничего не делаем
print('Что-то сделали')
# Обычно пустой оператор используется, чтобы временно определить «пустую», ничего не делающую функцию или «пустой» класс
def empty_function(): pass
class EmptyClass: pass
# Впоследствии такие «пустые» функции и классы наполняются необходимым содержимым.


# 3.6. Приоритет операторов
# Приоритет операторов - это очередность, в которой выполняются различные операторы Python. Например, оператор умножения
# будет выполнен раньше оператора сложения, поскольку приоритет первого выше, чем у второго.
# Рассмотрим следующее выражение:
# х = 5 + 10 * 3 / 2
# Последовательность его вычисления будет такой:
# 1. Число 10 будет умножено на 3, поскольку приоритет оператора умножения выше приоритета оператора сложения.
# 2. Полученное значение будет поделено на 2, поскольку приоритет оператора деления равен приоритету оператора умножения
# (а операторы с равными приоритетами выполняются слева направо), но выше, чем у оператора сложения.
# 3. К полученному значению будет прибавлено число 5.
# 4. Значение будет присвоено переменной х, поскольку оператор присваивания = имеет наименьший приоритет.
x = 5 + 10 * 3 / 2
print(x)
# С помощью скобок можно изменить последовательность вычисления выражения
# х = (5 + 10) * 3 / 2
# Теперь порядок вычислений станет иным:
# 1. К числу 5 будет прибавлено 10.
# 2. Полученное значение будет умножено на 3.
# 3. Полученное значение будет поделено на 2.
# 4. Значение будет присвоено переменной х.
x = (5 + 10) * 3 / 2
print(x)
# Перечислим операторы в порядке убывания приоритета:
# 1. -х, +х, ~х, ** - унарный минус, унарный плюс, двоичная инверсия, возведение в степень. Если унарные операторы
# расположены слева от оператора **, то возведение в степень имеет больший приоритет, а если справа - то меньший.
# Например, выражение
# -10 ** -2
# эквивалентно следующей расстановке скобок:
# -(10 ** (-2))
# 2. *, %, /, // - умножение (повторение), остаток от деления, деление, деление с округлением вниз.
# 3. +,--сложение (конкатенация), вычитание.
# 4. <<, >> - двоичные сдвиги.
# 5. & - двоичное И.
# 6. ^ - двоичное исключающее ИЛИ.
# 7. | - двоичное ИЛИ.
# 8. =, +=, -=, *=, /=, //=, %=, **= - присваивание.

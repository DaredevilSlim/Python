#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy    # Подключаем модуль сору
import math    # Подключаем модуль math
import random  # Подключаем модуль random

# ГЛАВА 8
# Списки, кортежи, множества и диапазоны
# Список, кортеж, множество и диапазон - это упорядоченные наборы значений, иначе говоря, последовательности. Значение,
# входящее в последовательность, называется элементом и может быть любого типа: числом, строкой, логической величиной и
# даже другой последовательностью. Количество элементов в последовательности называется размером.
# Большинство последовательностей (в частности, список, кортеж и диапазон) являются пронумерованными, поскольку в них за
# каждым элементом закреплен порядковый номер - индекс. Зная его, можно извлечь из списка или кортежа соответствующий
# этому индексу элемент. Нумерация элементов в пронумерованной последовательности начинается с О.
# Часть последовательностей (например, множество) относятся к группе непронумерованных, т. к. у их элементов нет


# 8.1. Создание списков
print('8.1. Создание списков')
# Список - это изменяемая пронумерованная последовательность.
# Создать список можно следующими способами:
# - с помощью функции list([<Последовательность>]). Функция возвращает список, созданный на основе указанной
# последовательности. Если последовательность не указана, выдается пустой список. Примеры:
print(list())                 # Создаем пустой список
print(list('String'))         # Преобразуем строку в список
print(list((1, 2, 3, 4, 5)))  # Преобразуем кортеж в список

# - приведя элементы списка внутри квадратных скобок через запятую:
arr = [1, 'str', 3, '4']
print(arr)

# - заполнив список поэлементно с помощью метода append() :
arr = list()       # Создаем пустой список
arr.append(1)      # Добавляем элемент1 (индекс О)
arr.append('str')  # Добавляем элемент2 (индекс 2)
print(arr)

# Не забываем, что при присваивании объекта (например, списка) какой-либо переменной в последнюю заносится не сам
# объект, а ссылка на него. В результате получатся две переменные, указывающие на один и тот же объект. Пример:
x = y = [1, 2]  # Якобы создали два списка
print(x, y)
y[1] = 100      # Изменяем второй элемент списка из второй переменной
print(x, y)     # Изменилось значение сразу в двух переменных
# Но что же делать, если необходимо создать копию списка? Первый способ заключается в применении операции извлечения
# среза, второй - в использовании функции list(), а третий - в вызове метода сору(). Примеры:
x = [1, 2, 3, 4, 5]  # Создали список
# Создаем копию списка
y = list(x)          # или с помощью среза: у = х[:] или вызовом метода сору(): у = х.сору()
print(y)
print(x is y)        # Оператор is показывает, что это разные объекты
y[1] = 100           # Изменяем второй элемент
print(x, y)          # Изменился только список в переменной у
# Однако, если в числе элементов копируемого списка имеются другие списки (вложенные), будут скопированы не сами эти
# списки, а ссылки на них. Как говорят в таких случаях программисты, будет создана поверхностная, копия. Рассмотрим
# пример:
x = [1, [2, 3, 4, 5]]  # Создали вложенный список
y = list(x)            # Якобы сделали копию списка
print(x is y)          # Разные объекты
y[1][1] = 100          # Изменяем элемент вложенного списка
print(x, y)            # Изменение затронуло переменную х!!!
# Чтобы получить полную копию списка вместе с вложенными списками, следует воспользоваться функцией deepcopy() из модуля
# сору:
# import copy # Подключаем модуль сору
x = [1, [2, 3, 4, 5]]
y = copy.deepcopy(x)  # Делаем полную копию списка
y[1][1] = 100         # Изменяем элемент вложенного списка
print(x, y)           # Изменился только список в переменной у
# Функция deepcopy() создает копию каждого объекта, при этом сохраняя внутреннюю структуру списка. Иными словами, если в
# списке существуют два элемента, ссылающиеся на один объект, то будет создана копия объекта и элементы будут ссылаться
# на этот новый объект, а не на разные объекты. Пример:
x = [1, 2]
y = [x, x]            # Два элемента ссылаются на один список
print(y)
z = copy.deepcopy(y)  # Сделали копию списка
print(z[0] is x, z[1] is x, z[0] is z[1])
z[0][0] = 300         # Изменили один элемент вложенного списка
print(z)              # Значение изменилось сразу в двух вложенных списках!
print(x)              # Начальный список не изменился


# 8.2. Операции над списками
print('8.2. Операции над списками')
# Чтобы получить элемент списка по его индексу, следует поставить после списка квадратные скобки и указать индекс в них:
arr = [1, 'str', 3.2, '4']
print(arr[0], arr[1], arr[2], arr[3])
# С помощью позиционного присваивания можно присвоить значения элементов списка каким-либо переменным. Количество
# элементов справа и слева от оператора = должно совпадать, иначе будет выведено сообщение об ошибке. Примеры:
x, y, z = [1, 2, 3]  # Позиционное присваивание
print(x, y, z)
# x, y = [1, 2, 3]   # Количество элементов должно совпадать
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 89, in <module>
#     x, y = [1, 2, 3]
#     ^^^^
# ValueError: too many values to unpack (expected 2)
# Перед одной из переменных слева от оператора = можно указать звездочку - и тогда в этой переменной будет сохранен
# список из «лишних» элементов. Если таких элементов нет, список будет пустым. Примеры:
x, y, *z = [1, 2, 3]
print(x, y, z)
x, y, *z = [1, 2, 3, 4, 5]
print(x, y, z)
x, y, *z = [1, 2]
print(x, y, z)
*x, y, z = [1, 2]
print(x, y, z)
x, *y, z = [1, 2, 3, 4, 5]
print(x, y, z)
*z, = [1, 2, 3, 4, 5]
print(z)
# В качестве индекса можно указать отрицательное значение. Такой индекс будет отсчитываться от конца списка. Пример:
arr = [1, 2, 3, 4, 5]
print(arr[-1], arr[-3])
# Так как списки относятся к изменяемым типам данных, мы можем изменить элемент по его индексу:
arr = [1, 2, 3, 4, 5]
arr[0] = 600           # Изменение элемента по индексу
print(arr)
# Если элемент с указанным индексом отсутствует в списке, возбуждается исключение IndexError:
# arr = [1, 2, 3, 4, 5]
# print(arr[5])          # Обращение к несуществующему элементу
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 118, in <module>
#     print(arr[5])      # Обращение к несуществующему элементу
#           ~~~^^^
# IndexError: list index out of range
# Получить размер списка (количество элементов в нем) позволяет функция len():
arr = [1, 2, 3, 4, 5]
print(len(arr))           # Получаем количество элементов
print(arr[len(arr) - 1])  # Получаем последний элемент
# Срез - это фрагмент списка, который сам является списком и содержит элементы, индексы которых располагаются между
# указанными начальным, конечным индексами и отстоят друг от друга на заданный шаг. Формат операции извлечения среза:
# [<Начало>:<Конец>:<Шаг>]
# Все параметры не являются обязательными. Если параметр <Начало> не указан, используется значение 0. Если параметр
# <Конец> не указан, возвращается фрагмент до конца списка. Элемент с индексом, указанным в параметре <Конец>, не входит
# в возвращаемый срез. Если параметр <Шаг> не указан, используется значение 1. В качестве значения параметров можно
# указать отрицательные значения. Рассмотрим несколько примеров:
# - получение поверхностной копии списка:
arr = [1, 2, 3, 4, 5]
m = arr[:]             # Создаем поверхностную копию и выводим значения
print(m)
print(m is arr)        # Оператор is показывает, что это разные объекты
# - вывод элементов списка в обратном порядке:
arr = [1, 2, 3, 4, 5]
print(arr[::-1])       # Шаг -1
# - вывод списка без первого и последнего элементов:
print(arr[1:])         # Без первого элемента
print(arr[:-1])        # Без последнего элемента
# - извлечение среза, содержащего первые два элемента списка:
print(arr[0:2])        # Символ с индексом 2 не входит в диапазон
# - получение среза, содержащего последний элемент списка:
print(arr[-1:])        # Последний элемент списка
# - получение среза с элементами от второго до четвертого включительно:
print(arr[1:4])        # Возвращаются элементы с индексами 1, 2 и 3
# С помощью среза можно изменить фрагмент списка. Если срезу присвоить пустой список, то элементы, попавшие в срез,
# будут удалены. Примеры:
arr = [1, 2, 3, 4, 5]
arr[1:3] = [6, 7]      # Изменяем значения элементов с индексами 1 и 2
print(arr)
arr[1:3] = []          # Удаляем элементы с индексами 1 и 2
print(arr)
# Объединить два списка в один список позволяет оператор +. Результатом объединения будет новый список. Пример:
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9]
arr3 = arr1 + arr2
print(arr3)
# Вместо оператора + можно использовать оператор +=. Следует учитывать, что в этом случае элементы добавляются в текущий
# список. Пример:
arr = [1, 2, 3, 4, 5]
arr += [6, 7, 8, 9]
print(arr)
# Еще списки поддерживают операции повторения (оператор *), проверки на вхождение (оператор in) и на невхождение
# (оператор not in):
print([1, 2, 3] * 3)                                 # Повторение
print(2 in [1, 2, 3, 4, 5], 6 in [1, 2, 3, 4, 5])    # Проверка на вхождение
print(2 not in [1, 2, 3, 4], 6 not in [1, 2, 3, 4])  # Проверка на невхождение


# 8.3. Многомерные списки
print('8.3. Многомерные списки')
# Многомерным называется список, содержащий в числе своих элементов вложенные списки (или иные последовательности).
# Создать многомерный список можно, например, так:
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
# Как вы уже знаете, выражение внутри скобок может располагаться на нескольких строках. Следовательно, предыдущий пример
# можно записать иначе:
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(arr)
# Чтобы получить значение элемента из вложенного списка, следует указать два индекса:
print(arr[1][1])
# Вложенные списки также могут содержать вложенные списки. В этом случае для доступа к элементам указывается несколько
# индексов подряд, например:
arr = [[1, ['a', 'b'], 3], [4, 5, 6], [7, 8, 9]]
print(arr[0][1][0])
arr = [[1, {'a': 10, 'b': ['s', 5]}]]
print(arr[0][1]['b'][0])


# 8.4. Перебор списков
print('8.4. Перебор списков')
# Последовательно перебрать все элементы списка можно с помощью цикла перебора последовательности:
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i, end=' ')
print()
# Значение очередного элемента списка заносится в переменную, указанную в цикле. Его можно изменить в теле цикла, но
# если оно относится к неизменяемому типу данных (например, числовому или строковому), это не отразится на исходном
# списке. Пример:
arr = [1, 2, 3, 4]      # Элементы имеют неизменяемый тип (число)
for i in arr:
    i += 10
print(arr)              # Список не изменился
arr = [[1, 2], [3, 4]]  # Элементы имеют изменяемый тип (список)
for i in arr:
    i[0] += 10
print(arr)              # Список изменился
# Однако изменить список в цикле все же можно, если для генерирования индексов его элементов воспользоваться функцией
# range(), возвращающей диапазон. Функция имеет следующий формат:
# range([<Начало>, ]<Конец>[, <Шаг>])
# Первый параметр задает начальное значение диапазона. Если он не указан, используется значение 0. Во втором параметре
# указывается конечное значение. Следует заметить, что это значение не входит в возвращаемый диапазон. Если параметр
# <Шаг> не указан, используется значение 1. Для примера умножим каждый элемент списка на 2:
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr[i] *= 2
print(arr)                 # Результат выполнения: [2, 4, 6, 8]
# Также можно воспользоваться функцией enumerate(<Список>[, start=0]), которая на каждой итерации цикла for возвращает
# кортеж из индекса и значения очередного элемента указанного списка. Параметр start задает индекс элемента, с которого
# начнется перебор списка. Умножим каждый элемент списка на 2:
arr = [1, 2, 3, 4]
for i, elem in enumerate(arr):
    arr[i] *= 2
print(arr)                 # Результат выполнения: [2, 4, 6, 8]
# Перебрать список можно и с помощью цикла с условием, но нужно помнить, что он выполняется медленнее цикла перебора
# последовательности. Для примера умножим каждый элемент списка на 2:
arr = [1, 2, 3, 4]
i, c = 0, len(arr)
while i < c:
    arr[i] *= 2
    i += 1
print(arr)                 # Результат выполнения: [2, 4, 6, 8]


# 8.5. Генераторы списков и выражения-генераторы
print('8.5. Генераторы списков и выражения-генераторы')
# Генератор списка заполняет создаваемый список элементами, полученными в результате каких-либо вычислений, которые
# выполняются над элементами другой последовательности. Формат записи генератора списка:
# [<Выражение> for <Переменная> in <Исходная последовательность>]
# Генератор списка перебирает заданную исходную последовательность, на каждой итерации занося значение ее очередного
# элемента в указанную переменную, и выполняет заданное выражение, проводящее необходимые вычисления над значением этого
# элемента (оно доступно из указанной переменной). Результаты вычислений, проведенных над всеми элементами исходной
# последовательности, сводятся во вновь созданный список, который и выдается в качестве результата.
# Генератор цикла можно рассматривать как более компактную и производительную разновидность цикла перебора
# последовательности.
# Для примера вернемся в разд. 8.4 и найдем код, изменяющий элементы списка:
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr[i] *= 2
print(arr)                  # Результат выполнения: [2, 4, 6, 8]
# Использовав генератор списка, можно заметно сократить объем этого кода (и ускорить его выполнение):
arr = [1, 2, 3, 4]
arr = [i * 2 for i in arr]
print(arr)                  # Результат выполнения: [2, 4, 6, 8]
# Генераторы списков могут быть вложены друг в друга и (или) содержать оператор ветвления. Для примера получим четные
# элементы списка и умножим их на 10:
arr = [1, 2, 3, 4]
arr = [i * 10 for i in arr if i % 2 == 0]
print(arr)                  # Результат выполнения: [20, 40]
# Этот код эквивалентен коду:
arr = []
for i in [1, 2, 3, 4]:
    if i % 2 == 0:          # Если число четное
        arr.append(i * 10)  # Добавляем элемент
print(arr)                  # Результат выполнения: [20, 40]
# Теперь получим четные элементы вложенного списка и умножим их на 10:
arr = [[1, 2], [3, 4], [5, 6]]
arr = [j * 10 for i in arr for j in i if j % 2 == 0]
print(arr)                      # Результат выполнения: [20, 40, 60]
# Этот код эквивалентен коду:
arr = []
for i in [[1, 2], [3, 4], [5, 6]]:
    for j in i:
        if j % 2 == 0:          # Если число четное
            arr.append(j * 10)  # Добавляем элемент
print(arr)                      # Результат выполнения: [20, 40, 60]
# Выражение-генератор аналогично генератору списка, только выдает не список, а итератор - особый объект, обладающий
# функциональностью последовательности. В частности, итератор можно перебрать, воспользовавшись циклом перебора
# последовательности. Формат записи выражения-генератора:
# (<Выражение> for <Переменная> in <Исходная последовательность>)
# Для примера вычислим посредством выражения-генератора квадратные корни чисел от 1 до 5 и выведем их на экран в цикле
# перебора:
exp_gen = (math.sqrt(n) for n in range(1, 6))
for p in exp_gen:
    print(p)


# 8.6. Функции map(), zip(), filter() и reduce()
print('8.6. Функции map(), zip(), filter() и reduce()')
# Функция map() применяет заданную функцию к каждому элементу указанной последовательности и сводит возвращенные ей
# результаты в новую последовательность, которую и возвращает в качестве результата. Она имеет такой формат:
# map(<Функция>, <Последовательность 1>[, . . ., <Последовательность N>])
# Задаваемая функция должна принимать единственный параметр - очередной элемент указанной последовательности. Еще она
# должна возвращать результат (обычно получаемый в результате каких-либо вычислений с применением полученного элемента).
# Функция map() в качестве результата возвращает итератор (объект с функциональностью последовательности, обычно
# ограниченной). Чтобы получить список, возвращенный итератор необходимо передать в функцию list().
# Для примера прибавим к каждому элементу списка число 10 test_00038.py.
# Функции map() можно передать несколько последовательностей. В этом случае. В заданной функции будут передаваться сразу
# несколько элементов, расположенных в последовательностях на одинаковом смещении. Просуммируем элементы трех списков
# test_00039.py.
# Если размеры заданных последовательностей различаются, за основу выбирается последовательность с минимальным
# количеством элементов test_00040.py.
# Функция zip() возвращает итератор, при переборе последовательно выдающий кортежи, содержащие элементы указанных
# последовательностей, расположенные на одинаковом смещении. Формат функции:
# ziр(<Последовательность 1>[, . . . , <Последовательность N>] [, strict=False])
# Пример:
print(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
# Если размеры заданных последовательностей различаются и параметру strict (поддерживается, начиная с Python 3.10) дано
# значение False, в результат попадут только элементы, которые существуют во всех последовательностях на одинаковом
# смещении:
print(list(zip([1, 2, 3], [4, 6], [7, 8, 9, 10])))
# Если же параметру strict дано значение True, при передаче функции zip() последовательностей разного размера будет
# сгенерировано исключение valueError:
# print(list(zip([1, 2, 3], [4, 6], [7, 8, 9, 10], strict=True)))
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 326, in <module>
#     print(list(zip([1, 2, 3], [4, 6], [7, 8, 9, 10], strict=True)))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: zip() argument 2 is shorter than argument 1
# Переделаем программу суммирования элементов трех списков из test_00040.py, использовав функцию zip() test_00041.py.
# Функция filter() выполняет проверку элементов последовательности на соответствие заданным критериям. Формат функции:
# filter(<Функция>, <Последовательность>)
# Указанная функция должна в качестве параметра принимать очередной элемент заданной последовательности и возвращать
# True или False. В результат будут добавлены только те элементы, для которых функция вернет True. Если вместо функции
# указать значение None, очередной элемент будет проверяться на соответствие значению True.
# Функция filter() возвращает итератор. Чтобы получить список, этот итератор необходимо передать в функцию list().
# Примеры:
print(filter(None, [1, 0, None, [], 2]))
print(list(filter(None, [1, 0, None, [], 2])))
# Аналогичный код с использованием генераторов списков выглядит так:
print([i for i in [1, 0, None, [], 2] if i])
# Для примера удалим все отрицательные значения из списка test_00042.py.
# Функция reduce() из модуля functools применяет указанную функцию к парам элементов заданной последовательности и
# накапливает результат. Функция имеет следующий формат:
# reduce(<Функция>, <Последовательность>[, <Начальное значение>])
# В заданную функцию передаются два параметра: результат предыдущих вычислений и значение очередного элемента указанной
# последовательности. При обработке первого элемента последовательности функции передаются:
# - если начальное значение задано - начальное значение и первый элемент последовательности;
# - если начальное значение не задано - первый и второй элементы последовательности;
# Получим сумму всех элементов списка test_00043.py.


# 8.7. Добавление и удаление элементов списка
print('8.7. Добавление и удаление элементов списка')
# Для добавления и удаления элементов списка используются следующие методы:
# - append(<Значение>) - добавляет значение в качестве элемента в конец текущего списка. Результата не возвращает.
# Примеры:
arr = [1, 2, 3]
arr.append(4)
print(arr)          # Добавляем число
arr.append([5, 6])
print(arr)          # Добавляем список
arr.append((7, 8))
print(arr)          # Добавляем кортеж

# - extend(<Последовательность>) - добавляет элементы заданной последовательности в конец текущего списка. Результата не
# возвращает. Примеры:
arr = [1, 2, 3]
arr.extend([4, 5, 6])  # Добавляем список
arr.extend([7, 8, 9])  # Добавляем кортеж
arr.extend('abc')      # Добавляем буквы из строки
print(arr)
# Добавить несколько элементов можно посредством конкатенации или оператора +=:
arr = [1, 2, 3]
print(arr + [4, 5, 6])  # Возвращает новый список
arr += [4, 5, 6]        # Изменяет текущий список
print(arr)
# Кроме того, можно воспользоваться операцией присваивания значения срезу:
arr = [1, 2, 3]
arr[len(arr):] = [4, 5, 6]  # Изменяет текущий список
print(arr)

# - insert(<Индекс>, <Значение>) - добавляет заданное значение в текущий список по указанному индексу. Остальные
# элементы смещаются. Результата не возвращает. Примеры:
arr = [1, 2, 3]
arr.insert(0, 0)
print(arr)              # Вставляем 0 в начало списка
arr.insert(-1, 20)
print(arr)              # Можно указать отрицательные числа
arr.insert(2, 100)
print(arr)              # Вставляем 100 в позицию 2
arr.insert(10, [4, 5])
print(arr)              # Добавляем список
# Метод insert() позволяет добавить только один элемент. Чтобы добавить несколько элементов, можно воспользоваться
# операцией присваивания значения срезу. Добавим несколько элементов в начало списка:
arr = [1, 2, 3]
arr[:0] = [-3, -2, -1, 0]
print(arr)

# - рор([<Индекс>]) - удаляет из текущего списка элемент, расположенный по указанному индексу, и возвращает его. Если
# индекс не указан, то удаляет и возвращает последний элемент списка. Если элемента с указанным индексом нет или список
# пустой, возбуждается исключение IndexError. Примеры:
arr = [1, 2, 3, 4, 5]
arr.pop()   # Удаляем последний элемент списка
print(arr)  # Список изменился
arr.pop(0)  # Удаляем первый элемент списка
print(arr)  # Список изменился
# Удалить элемент списка позволяет также оператор del:
arr = [1, 2, 3, 4, 5]
del arr[4]   # Удаляем последний элемент списка
print(arr)
del arr[:2]  # Удаляем первый и второй элементы
print(arr)

# - remove(<Значение>) - удаляет из текущего списка первый элемент, содержащий указанное значение. Если элемент не
# найден, возбуждается исключение ValueError. Метод ничего не возвращает. Примеры:
arr = [1, 2, 3, 1, 1]
arr.remove(1)  # Удаляет только первый элемент
print(arr)
# arr.remove(5)  # Такого элемента нет
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 422, in <module>
#     arr.remove(5)  # Такого элемента нет
#     ^^^^^^^^^^^^^
# ValueError: list.remove(x): x not in list

# - clear() - удаляет все элементы текущего списка, очищая его. Результата не возвращает. Пример:
arr = [1, 2, 3, 1, 1]
arr.clear()
print(arr)
# Если необходимо удалить все повторяющиеся элементы списка, то можно преобразовать список во множество, а затем
# множество обратно преобразовать в список. Обратите внимание на то, что список должен содержать только неизменяемые
# объекты (например, числа, строки или кортежи). В противном случае возбуждается исключение TypeError. Пример:
arr = [1, 2, 3, 1, 1, 2, 2, 3, 3]
s = set(arr)   # Преобразуем список во множество
arr = list(s)  # Преобразуем множество в список
print(arr)


# 8.8. Поиск элемента в списке и получение сведений об элементах списка
print('8.8. Поиск элемента в списке и получение сведений об элементах списка')
# Выполнить проверку на вхождение элемента в список позволяет оператор in: если элемент входит в список, то возвращается
# значение True, в противном случае - False. Аналогичный оператор not in выполняет проверку на невхождение элемента в
# список: если элемент отсутствует в списке, возвращается True, в противном случае - False. Примеры:
print(2 in [1, 2, 3, 4, 5], 6 in [1, 2, 3, 4, 5])    # Проверка на вхождение
print(2 not in [1, 2, 3, 4], 6 not in [1, 2, 3, 4])  # Проверка на невхождение
# Чтобы узнать индекс элемента с заданным значением в текущем списке, следует воспользоваться методом index(). Формат
# метода:
# index(<Значение>[, <Начало>[, <Конец>]])
# В параметре <Начало> указывается индекс элемента, с которого начнется поиск. Если он не задан, поиск начнется с начала
# списка. В параметре <Конец> можно задать индекс элемента, на котором закончится поиск. Если этот параметр не указан,
# поиск будет вестись до конца списка.
# Метод index() возвращает индекс элемента, имеющего указанное значение. Если значение не входит в список, то
# возбуждается исключение ValueError. Примеры:
arr = [1, 2, 1, 2, 1]
print(arr.index(1), arr.index(2))
print(arr.index(1, 1), arr .index(1, 3, 5))
# print(arr. index(3))
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 460, in <module>
#     print(arr. index(3))
#           ^^^^^^^^^^^^^
# ValueError: 3 is not in list
# Узнать количество элементов списка с указанным значением позволяет метод count(<Значение>):
arr = [1, 2, 1, 2, 1]
print(arr.count(1), arr.count(2))
print(arr.count(3))                # Элемент не входит в список
# С помощью функций max() и min(), можно узнать максимальное и минимальное значения из всех, что входят в список,
# соответственно:
arr = [1, 2, 3, 4, 5]
print(max(arr), min(arr))
# Функция аnу(<Последовательность>) возвращает значение True, если в заданной последовательности существует хотя бы один
# элемент, который в логическом контексте возвращает значение True. Если последовательность не содержит элементов,
# возвращается значение False. Пример:
print(any([0, None]), any([0, None, 1]), any([]))
# Функция all(<Последовательность>) возвращает значение True, если все элементы заданной последовательности в логическом
# контексте возвращают True, или последовательность не содержит элементов:
print(all([0, None]), all([0, None, 1]), all([]), all(['str', 10]))


# 8.9. Переворачивание и перемешивание списка
print('8.9. Переворачивание и перемешивание списка')
# Метод reverse() изменяет порядок следования элементов текущего списка на противоположный. Результата не возвращает.
# Пример:
arr = [1, 2, 3, 4, 5]
arr.reverse()          # Изменяется текущий список
print(arr)
# Если необходимо изменить порядок следования и получить новый список, следует воспользоваться функцией
# reversed(<Последовательность>). Она возвращает итератор, который можно преобразовать в список с помощью функции list()
# или генератора списков. Примеры:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reversed(arr))
print(list(reversed(arr)))             # Использование функции list()
for i in reversed(arr):
    print(i, end=' ')                  # Вывод с помощью цикла
print()
print([i for i in reversed(arr)])      # Использование генератора списков
# Функция shuffle(<Список>) из модуля random перемешивает элементы списка случайным образом. Результата не возвращает.
# Примеры:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(arr)                    # Перемешиваем список случайным образом
print(arr)
# ПРИМЕЧАНИЕ - Второй параметр функции shuffle() в Python 3.9 объявлен устаревшим и не рекомендованным к применению.
# Его поддержка будет удалена в Python 3.11.


# 8.10. Выбор элементов списка случайным образом
print('8.10. Выбор элементов списка случайным образом')
# Выбрать элементы из списка случайным образом позволяют следующие функции из модуля random:
# - choice(<Последовательность>) - возвращает случайный элемент из заданной последовательности, которая может быть
# любого типа (строкой, списком, кортежем и др.):
print(random.choice(['s', 't', 'r']))  # Список

# - sample() - возвращает список из указанного количества элементов заданной последовательности, выбранных случайным
# образом. Формат вызова:
# sample(<Последовательность>, <Количество элементов>[, counts=<Количество повторений элементов>])
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(arr, 2))
print(arr)                             # Сам список не изменяется
# Начиная с Python 3.9, поддерживается именованный параметр counts, в котором можно указать последовательность,
# содержащую значения количества повторений элементов из последовательности, заданной первым параметром. Первый элемент
# последовательности из параметра counts укажет количество повторений первого элемента из первой последовательности,
# второй элемент - количество повторений второго элемента и т. д. Например, следующие два вызова функции sample()
# эквивалентны:
print(random.sample([1, 1, 1, 2, 2, 3, 3, 3, 3], 5))
print(random.sample([1, 2, 3], 5, counts=[3, 2, 4]))
# Также, начиная с Python 3.9, указывать множества в первом параметре функции sample() не допускается - эта возможность
# объявлена устаревшей и подлежащей удалению в будущих версиях языка;

# - choices() - возвращает список из указанного количества элементов заданной последовательности, выбранных случайным
# образом на основе заданных весовых коэффициентов. Формат вызова:
# choices(<Последовательность>[, <Весовые коэффициенты>][, k=1])
# Количество элементов в результирующем списке указывается в параметре k. Весовые коэффициенты задаются в виде
# последовательности чисел. Чем больше весовой коэффициент, тем выше вероятность, что соответствующий элемент
# последовательности из первого параметра попадет в результирующий список. Однако следует учесть, что элементы с
# высокими коэффициентами могут быть включены в результат по нескольку раз. Пример:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [10, 20, 10, 40, 30, 50, 100, 40, 10, 20]
print(random.choices(arr, weights, k=4))
# Если весовые коэффициенты не указаны, вероятность попадания каждого элемента заданной последовательности в
# результирующий список одинакова:
print(random.choices(arr, k=4))


# 8.11. Сортировка списка
print('8.11. Сортировка списка')
# Отсортировать текущий список позволяет метод sort(). Он имеет следующий формат:
# sort([key=None][, reverse=False])
# Метод ничего не возвращает. Отсортируем список по возрастанию значений:
arr = [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
arr.sort()                             # Изменяет текущий список
print(arr)
# Чтобы отсортировать список по убыванию, следует в параметре reverse указать значение True:
arr = [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
arr.sort(reverse=True)                 # Сортировка по убыванию
print(arr)
# В параметре key можно указать функцию, выполняющую какое-либо действие над каждым элементом списка. В качестве
# единственного параметра она должна принимать очередной элемент списка и возвращать результат действий над ним. Этот
# результат будет участвовать в процессе сортировки, но значения самих элементов списка не изменятся.
# Стандартная сортировка зависит от регистра символов test_00044.py.
# Выполнив пример из test_00044.py, мы получили неправильный результат сортировки, ведь Единый и Единица2 больше
# единица1. Чтобы регистр символов не учитывался, в параметре key мы укажем функцию для изменения регистра символов
# test_00045.py.
# Метод sort() сортирует сам текущий список и не возвращает результата. Если необходимо получить отсортированный список,
# а текущий оставить без изменений, следует воспользоваться функцией sorted(). Функция имеет следующий формат:
# sorted(<Последовательность>[, key=None] [, reverse=False])
# В первом параметре указывается список, который необходимо отсортировать. Остальные параметры эквивалентны параметрам
# метода sort(). Пример:
arr = [2, 7, 10, 4, 6, 8, 9, 3, 1, 5]
print(sorted(arr))                     # Возвращает новый список!
print(sorted(arr, reverse=True))       # Возвращает новый список!
arr = ['единица1', 'Единый', 'Единица2']
print(sorted(arr, key=str.lower))


# 8.12. Заполнение списка числами
print('8.12. Заполнение списка числами')
# Создать список, содержащий диапазон чисел, можно, вызвав функцию range() и преобразовав возвращенный ею диапазон в
# список вызовом функции list(). Функция range() имеет следующий формат:
# range([<Начало>, ]<Конец>[, <Шаг>])
# Первый параметр задает начальное значение, а если он не указан, используется значение 0. Во втором параметре
# указывается конечное значение. Следует заметить, что это значение не входит в возвращаемый диапазон. Если параметр
# <Шаг> не указан, используется значение 1. В качестве примера заполним список числами от 0 до 10:
print(list(range(11)))
# Создадим список, состоящий из диапазона чисел от 1 до 15:
print(list(range(1, 16)))
# Изменим порядок следования чисел на противоположный:
print(list(range(15, 0, -1)))
# Список со случайными числами (или случайными элементами из другого списка) можно получить вызовом функции sample():
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.sample(arr, 3))
print(random.sample(range(300), 5))


# 8.13. Преобразование списка в строку
print('8.13. Преобразование списка в строку')
# Преобразовать список в строку позволяет метод join(). Элементы добавляются в формируемую строку через указанный
# разделитель. Формат метода:
# <Разделитель>.join(<Последовательность>)
# Пример:
arr = ['word1', 'word2', 'word3']
print(' - '.join(arr))
# Все элементы списка должны быть строками, иначе генерируется исключение TypeError:
# arr = ['word1', 'word2', 'word3', 2]
# print(' - '.join(arr))
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 608, in <module>
#     print(' - '.join(arr))
#           ^^^^^^^^^^^^^^^
# TypeError: sequence item 3: expected str instance, int found
# Избежать этого исключения можно с помощью выражения-генератора, внутри которого текущий элемент списка преобразуется в
# строку с помощью функции str():
arr = ['word1', 'word2', 'word3', 2]
print(' - '.join(str(i) for i in arr))


# 8.14. Кортежи
print('8.14. Кортежи')
# Кортеж - это неизменяемая пронумерованная последовательность, фактически - неизменяемый список.
# Создать кортеж можно следующими способами:
# - с помощью функции tuple([<Последовательность>]). Функция возвращает кортеж, составленный из элементов заданной
# последовательности. Если параметр не указан, выдается пустой кортеж. Примеры:
print(tuple())                 # Создаем пустой кортеж
print(tuple('String'))         # Преобразуем строку в кортеж
print(tuple([1, 2, 3, 4, 5]))  # Преобразуем список в кортеж
# - приведя элементы создаваемого кортежа через запятую внутри круглых скобок (или без скобок):
t1 = ()                  # Создаем пустой кортеж
t2 = (5,)                # Создаем кортеж из одного элемента
t3 = (1, 'str', (3, 4))  # Кортеж из трех элементов
t4 = 1, 'str', (3, 4)    # Кортеж из трех элементов
print(t1, t2, t3, t4)
# Обратите особое внимание на вторую строку примера. Чтобы создать кортеж из одного элемента, необходимо в конце указать
# запятую. Именно запятые формируют кортеж, а не круглые скобки. Если внутри круглых скобок нет запятых, будет создан
# объект другого типа:
t = (5)
print(type(t))  # Получили число, а не кортеж!
t = ('str')
print(type(t))  # Получили строку, а не кортеж!
# Четвертая строка в исходном примере также доказывает, что не скобки формируют кортеж, а запятые. Помните, что для
# создания кортежа необходимо указать запятые.
# Как и списки, кортежи поддерживают обращение к элементу по индексу, получение среза, объединение (оператор +),
# повторение (оператор *), проверку на вхождение (оператор in) и невхождение (оператор not in):
t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(t[0])                    # Получаем значение первого элемента кортежа
print(t[::-1])                 # Изменяем порядок следования элементов
print(t[2:5])                  # Получаем срез
print(8 in t, 0 in t)          # Проверка на вхождение
print((1, 2, 3) * 3)           # Повторение
print((1, 2, 3) + (4, 5, 6))   # Конкатенация
print(8 not in t, 0 not in t)  # Проверка на вхождение
# Изменять элементы кортежа нельзя:
# t = (1, 2, 3)  # Создаем кортеж
# t[0] = 50      # Изменить элемент по индексу нельзя!
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 656, in <module>
#     t[0] = 50      # Изменить элемент по индексу нельзя!
#     ~^^^
# TypeError: 'tuple' object does not support item assignment
# Кортежи поддерживают уже знакомые нам по спискам функции len(), min(), max(), методы index() и count():
t = (1, 2, 3)                  # Создаем кортеж
print(len(t))                  # Получаем размер
t = (1, 2, 1, 2, 1)
print(t.index(1), t.index(2))  # Ищем элементы в кортеже
# Будучи неизменяемыми, кортежи занимают меньше оперативной памяти и обрабатываются быстрее, чем изменяемые списки.
# Поэтому по возможности рекомендуется предпочитать кортежи спискам.


# 8.15. Множества, изменяемые и не изменяемые
print('8.15. Множества, изменяемые и не изменяемые')
# Множество - это изменяемая непронумерованная последовательность, хранящая только уникальные значения (повторяющиеся
# значения при попытке добавить их в множество отбрасываются).
# Создать множество из элементов указанной последовательности можно с помощью функции set(<Последовательность>). Если
# параметр не указан, создается пустое множество. Примеры:
s = set()                       # Создаем пустое множество
print(s)
print(set('string'))            # Преобразуем строку в множество
print({1, 2, 3, 4, 5})     # Преобразуем список в множество
print({1, 2, 3, 4, 5})     # Преобразуем кортеж в множество
print({1, 2, 3, 1, 2, 3})  # Остаются только уникальные элементы
# Перебрать элементы множества позволяет цикл перебора последовательности:
for i in {1, 2, 3}:
    print(i)
# Получить размер множества позволяет функция len():
print(len({1, 2, 3}))
# Поскольку множество является непронумерованной последовательностью, получить значение его элемента по индексу,
# изменить значение элемента по индексу и извлечь срез у множества нельзя - это приведет к генерированию исключения
# TypeError:
# s = set([1, 2, 3])
# print(s[1])
# Traceback (most recent call last):
#   File "/Chapter_08.py", line 692, in <module>
#     print(s[1])
#           ~^^^
# TypeError: 'set' object is not subscriptable
# Для работы с множествами предназначены следующие операторы и соответствующие им методы, поддерживаемые объектом
# множества:
# - | и union() - объединяют два множества:
s = {1, 2, 3}
print(s.union({4, 5, 6}), s | {4, 5, 6})
print({1, 2, 3} | {2, 3, 4})
# - а |= b и a.update(b) - добавляют элементы множества b во множество b:
s = {1, 2, 3}
s.update({4, 5, 6})
print(s)
s |= {7, 8, 9}
print(s)
# - - и difference() - вычисляют разницу множеств:
print({1, 2, 3} - {1, 2, 4})
s = {1, 2, 3}
print(s.difference({1, 2, 4}))
# - a -= b и a.difference_update(b) - удаляют из множества a элементы, которые существуют в обоих исходных множествах:
s = {1, 2, 3}
s.difference_update({1, 2, 4})
print(s)
s = {1, 2, 3}
s -= {3, 4, 5}
print(s)
# - & и intersection() - возвращают множество с элементами, которые существуют в обоих исходных множествах:
print({1, 2, 3} & {1, 2, 4})
s = {1, 2, 3}
print(s.intersection({1, 2, 4}))
# - а &= b и a.intersection_update(b) - оставляют во множестве a элементы, которые существуют в обоих исходных
# множествах:
s = {1, 2, 3}
s.difference_update({1, 2, 4})
print(s)
s = {1, 2, 3}
s &= {1, 6, 7}
print(s)
# - ^ и symmetric_difference() - возвращают множество с элементами, которые существуют только в одном из исходных
# множеств:
s = {1, 2, 3}
print(s ^ {1, 2, 4}, s.symmetric_difference({1, 2, 4}))
print(s ^ {1, 2, 3}, s.symmetric_difference({1, 2, 3}))
print(s ^ {4, 5, 6}, s.symmetric_difference({4, 5, 6}))
# - а ^= b и а.symmetric_difference_update (b) - оставляют во множестве а элементы, присутствующие только в одном из
# исходных множеств:
s = {1, 2, 3}
s.symmetric_difference_update({1, 2, 4})
print(s)
s ^= {3, 5, 6}
print(s)

# Операторы сравнения множеств:
# - in - проверка наличия элемента во множестве:
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# 143


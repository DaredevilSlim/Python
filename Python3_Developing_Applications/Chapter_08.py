#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy  # Подключаем модуль сору

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
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
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


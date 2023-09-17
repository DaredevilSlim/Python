#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time  # Подключаем модуля time
import math  # Подключаем модуля math

# ГЛАВА 12
# Модули, пакеты и импорт
# Модуль-это любой файл с программным кодом. Любой модуль может использовать идентификаторы (переменные, функции и
# классы, о которых речь пойдет в главе 13), созданные в другом модуле, выполнив процедуру подключения, или импорта,
# последнего. В составе интерпретатора Python поставляется большой набор модулей, содержащих полезные переменные,
# функции и классы. Эти модули называются встроенными, а их совокупность - стандартной библиотекой языка.

# ПРИМЕЧАНИЕ - Модули можно создавать не только на самом Python, но и на языке С++, компилируя их в машинный код. В
# стандартной библиотеке содержится ряд таких модулей.

# Модуль Python представляется особым объектом, содержащим ряд атрибутов. Так, атрибут __name__ содержит имя модуля в
# виде строки. У модуля, непосредственно запущенного на исполнение, этот атрибут хранит строку '__main__'. Пример:
print(__name__)  # Выведет: main
# Проверить, является модуль непосредственно запущенным (главным модулем, или главной программой) или импортированным,
# позволяет следующий код:
if __name__ == '__main__':
    print('Это главная программа')
else:
    print('Импортированный модуль')


# 12.1. Импорт модуля целиком
print('12.1. Импорт модуля целиком')
# Можно импортировать модуль целиком и использовать любые созданные в нем переменные, функции и классы. Для этого
# предназначена языковая конструкция следующего формата:
# import <Модуль 1> [as <Псевдоним 1>], ..., <Модуль N> [as <Псевдоним N>]
# Имя модуля не должно содержать расширения и пути к файлу, а также удовлетворять всем требованиям, предъявляемым к
# именам переменных (см.разд. 2.1). Дело в том, что при импорте модуля интерпретатор создает переменную, которой
# присваивает объект импортированного модуля.
# Все идентификаторы, созданные в импортированном модуле, доступны через атрибуты объекта этого модуля (атрибут - это
# переменная, входящая в состав объекта). Для доступа к атрибутам следует использовать такой синтаксис:
# <Переменная с объектом модуля>.<Атрибут с нужным идентификатором>
# Поскольку переменная с объектом модуля и атрибут отделяются друг от друга точкой, такая запись получила название
# точечной нотации.
# Для примера импортируем модуль time и получим текущую дату вызовом функции strftime(), определенной в этом модуле:
print(time.strftime('%d.%m.%Y'))
# Подключим сразу два модуля: time и math:
print(time.strftime('%d.%m.%Y'))
print(math .pi)  # Число п
# Функция getattr() позволяет получить значение атрибута с заданным в виде строки именем, принадлежащего указанному
# модулю. С помощью этой функции можно сформировать имя нужного атрибута программно. Формат функции:
# getattr(<Объект модуля>, <Имя атрибута>[, <Значение по умолчанию>])
# Если указанный атрибут не найден, возвращается заданное значение по умолчанию, а если оно не указано - возбуждается
# исключение AttributeError. Пример:
print(getattr(math, 'pi'))     # Будет выведено число п
print(getattr(math, 'х', 50))  # Будет выведено 50, т.к. х не существует
# Проверить существование атрибута с заданным именем в указанном модуле позволяет функция
# hasattr(<Модуль>, <Имя атрибута>). Если атрибут существует, функция возвращает значение True, в противном случае
# - False. Напишем функцию проверки существования атрибута в модуле math test_00077.py.
# Если имя модуля слишком длинное и его неудобно указывать каждый раз для доступа к атрибутам, то можно дать модулю
# псевдоним. После чего для доступа к модулю следует использовать исключительно указанный псевдоним (при попытке доступа
# по имени модуля возникнет ошибка). Дадим модулю math псевдоним m:
# import math as m
# print(m.pi)
# Идентификаторы, содержащиеся в импортированном модуле, не смешиваются с идентификаторами, созданными в импортирующем
# модуле. Это значит, что, например, в импортируемом и импортирующем модулях могут содержаться совершенно разные
# переменные с одинаковым именем х.
# Проиллюстрируем это примером. Создадим модуль test_00078.py, в котором определим переменную х.
# В главной программе также определим переменную х, но с другим значением. Затем подключим модуль test_00078.py и
# выведем значения переменных test_00079.py.
# Оба модуля размещаем в одном каталоге и запускаем модуль с главной программой. Программа выведет числа 50 и 22
# - значения переменных с именем х, хранящихся в разных модулях. Как видно из результата, одноименные переменные из
# разных модулей никак не конфликтуют друг с другом.
# Объект каждого импортированного модуля заносится в словарь modules из модуля sys. При попытке импорта модуля сначала
# проверяется, есть ли этот модуль в упомянутом словаре, и если он там есть, повторный импорт выполнен не будет.
# Выведем ключи словаря modules, предварительно отсортировав их test_00080.py.
# Инструкция импорта требует явного указания объекта модуля. Задать имя модуля в виде строки нельзя.
# Чтобы подключить модуль, имя которого формируется программно, следует воспользоваться функцией
# __import__( <Имя модуля>). Функция возвращает объект импортированного модуля. Для примера импортируем модуль
# test_00078.py с помощью функции __import__() test_00081.py.
# Получить список всех идентификаторов, созданных в указанном модуле, позволяет функция dir(<Объект модуля>). Еще можно
# воспользоваться словарем из атрибута __dict__ объекта модуля, который содержит все идентификаторы и их значения
# test_00082.py.
# ПРИМЕЧАНИЕ - При импорте модуля он всегда компилируется (о компиляции рассказывалось в разд. 1. 10).


# 12.2. Импорт отдельных идентификаторов
print('12.2. Импорт отдельных идентификаторов')
# Также можно импортировать из модуля только отдельные идентификаторы, нужные для работы. Для этого применяется языковая
# конструкция, записываемая в одном из следующих форматов:
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# 244
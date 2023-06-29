#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math    # Подключаем модуль math
import locale  # Подключаем модуль locale

# ГЛАВА 6
# Строки и двоичные данные
# Строка - это неизменяемая последовательность произвольных символов в кодировке Unicode. Длина строки ограничена лишь
# объемом оперативной памяти компьютера.
# Двоичные данные - это последовательность байтов (чисел от О до 255), которая может быть как неизменяемой, так и
# изменяемой. Длина такой последовательности также ограничена лишь объемом оперативной памяти. В виде двоичных данных
# может быть сохранена информация любого рода: строка, графическое изображение, архив и др.


# 6.1. Создание строк
print('6.1. Создание строк')
# Создать строку можно следующими способами:
# - записав составляющие строку символы между одинарными или двойными кавычками:
print('строка', 'строка')
# Строки, созданные с применением одинарных и двойных кавычек, ничем не отличаются друг от друга.
# В строках, созданных одинарными кавычками, можно размещать двойные кавычки, а в строках, созданных двойными кавычками,
# - одинарные кавычки:
print('Группа "Кино"', "О'Брайен")
# Попытка вставить одинарную кавычку в строку, созданную одинарными кавычками, или двойную кавычку в строку в двойных
# кавычках приведет к ошибке:
# print('Группа 'КИно'')
# SyntaxError: invalid syntax
# В строках можно указать специальные символы - символы, обрабатываемые особым образом. Обозначение специального символа
# начинается со знака обратного слеша (\).
# Например, специальный символ \n обозначает разрыв строки, специальный символ \' - одинарную кавычку, символ \' -
# двойную кавычку, а \\ - обратный слеш. Более подробно специальные символы будут описаны в разд. 6.1.1. Примеры:
print('Строка1\\nСтрока2')
print('Группа \'КИно\'', 'О\'Брайен')
# Специальный символ \\ обычно применяется для вставки символа обратного слеша в конец строки:
print('string\\')
# Если же использовать единичный символ обратного слеша, интерпретатор посчитает его и следующую за ним кавычку
# специальным символом и выведет сообщение о синтаксической ошибке:
# print('string\')
# SyntaxError: unterminated string literal (detected at line 36)
# Нельзя разбивать строковый объект, созданный с помощью кавычек, на несколько строк - это вызовет синтаксическую
# ошибку:
# print('string)
# SyntaxError: unterminated string literal (detected at line 40)
# Чтобы расположить строковое значение на нескольких строках, следует либо перед символом перевода строки указать
# символ \, либо поместить отдельные части строки внутри круглых скобок, либо выполнить конкатенацию строк также внутри
# круглых скобок:
print('string1\
      string2')  # После \ не должно быть никаких символов
print('string1'
      'string2')  # Неявная конкатенация строк
print('string1' +
      'string2')  # Явная конкатенация строк
#
#
#
# - указав строку между утроенными одинарными или двойными кавычками. Такие строковые объекты могут размещаться на
# нескольких строках, содержать одинарные и двойные кавычки. Примеры:
print('''Строка1
      Строка2''')
print('''Строка1
      Строка2''')
# - с помощью функции str([ <Значение>[, <Кодировка>[, <Обработка ошибок>]]]). Если указан только первый параметр,
# функция возвращает строковое представление указанного значения. Если параметры не указаны вообще, возвращается пустая
# строка. Примеры:
print(str(), str([1, 2]), str((3, 4)), str({'x': 1}))
# При попытке преобразовать двоичные данные типа byte или bytearray в строку будет выдано строковое представление
# двоичных данных:
print(str(b'\xf1\xf2\xf0\xee\xea\xe0'))
# Чтобы получить строку, следует указать кодировку:
print(str(b'\xf1\xf2\xf0\xee\xea\xe0', 'cp1251'))
# В третьем параметре могут быть указаны значения 'strict' (при ошибке возбуждается исключение UnicodeDecodeError - 
# значение по умолчанию), 'replace' (неизвестный символ заменяется символом с кодом \uFFFD) или 'ignore' (неизвестные
# символы игнорируются):
obj1 = bytes('строка1', 'utf-8')
print(obj1)
obj2 = bytearray('строка2', ':utf-8')
print(obj2)
print(str(obj1, 'utf-8'), str(obj2, 'utf-8'))
# str(obj1, 'ascii', 'strict')
# Traceback (most recent call last):
#   File "/Chapter_06.py", line 77, in <module>
#     str(obj1, 'ascii', 'strict')
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xd1 in position 0: ordinal not in range(128)
print(str(obj1, 'ascii', 'ignore'))


# Если строка не присваивается переменной, то она считается строкой документирования.
# Такая строка сохраняется в атрибуте _doc_ того объекта, в котором расположена. В качестве примера создадим функцию со
# строкой документирования, а затем выведем содержимое строки:


def test():
    """Это описание функции"""
    pass


print(test.__doc__)


# 6.1.1. Специальные символы
print('6.1.1. Специальные символы')
# Специальные символы, как говорилось ранее, имеют особое значение и обрабатываются особым образом. Python поддерживает
# следующие специальные символы:
# - \n - перевод строки;
# - \r - возврат каретки;
# - \t - знак табуляции;
# - \v - вертикальная табуляция;
# - \а - звонок;
# - \b - забой;
# - \f - перевод формата;
# - \0 - нулевой символ;
# - \" - двойная кавычка;
# - \' - одинарная кавычка (апостроф);
# - \\ - обратный слеш;
# - \<N> - символ с восьмеричным кодом <N>. Например, \74 соответствует символу <;
# - \x<N> - символ с шестнадцатеричным кодом <N>. Например, \x6a соответствует символу j;
# - \u<nnnn> - символ с 16-битным Unicode-кодом <nnnn>. Например, \u04За соответствует русской букве к;
# - \U<nnnnnnnn> - символ с 32-битным Unicode-кодом <nnnnnnnn>;
# - \N{<name>} - символ с Unicode-именем <name>. Например, \N{Registered Sign} соответствует знаку зарегистрированной
# торговой марки ®·
# Комбинация обратного слеша с любым другим символом выводится как есть:
print('Этот символ \не специальный')
# Тем не менее для вставки обратного слеша лучше использовать специальный символ \\:
print('Этот символ \\не специальный')
# Этот символ \не специальный


# 6.1.2. Необрабатываемые строки
print('6.1.2. Необрабатываемые строки')
# В необрабатываемых строках специальные символы не обрабатываются, а выводятся как есть. Чтобы превратить строку в
# необрабатываемую, достаточно предварить ее модификатором r или R. Примеры:
print('Строка1\nСтрока2')
print(r'Строка1\nСтрока2')
print(R'Строка1\nСтрока2')
print(r"""Строка1\nСтрока2""")
# Необрабатываемые строки удобно использовать в шаблонах регулярных выражений и при записи файловых путей:
print(r'C:\Python310\lib\site-packages')
# В обычных строках все обратные слеши придется заменять на специальные символы \\:
print('C:\\Python310\\lib\\site-packages')
# Если в конце необрабатываемой строки должен располагаться слеш, следует использовать специальный символ \\. Однако
# этот символ будет добавлен в строку. Пример:
# print(r'C:\Python310\lib\site-packages\')
# File "/Chapter_06.py", line 140
#     print(r'C:\Python310\lib\site-packages\')
# SyntaxError: unterminated string literal (detected at line 140)
print(r'C:\Python310\lib\site-packages\\')
# Избавиться от лишнего слеша можно, использовав конкатенацию строк, обычные строки
# или удалив слеш явно:
print(r'C:\Python310\lib\site-packages' + '\\')  # Конкатенация
print('С:\\Python310\\lib\\site-packages\\')     # Обычная строка
print(r'C:\PythonЗlO\lib\site-packages\\'[:-1])  # Удаление слеша


# 6.2. Операции над строками
print('6.2. Операции над строками')
# Строки относятся к последовательностям и, соответственно, поддерживают все операции, выполняемые над
# последовательностями.
# Можно извлечь любой символ строки, указав индекс этого символа в квадратных скобках. Нумерация символов начинается
# с нуля. Пример:
s = 'Python'
print(s[0], s[1], s[2], s[3], s[4], s[5])
# При обращении к символу с несуществующим индексом возбуждается исключение IndexError:
# s = "Python"
# print(s[10])
# Traceback (most recent call last):
#   File "/Chapter_06.py", line 162, in <module>
#     print(s[10])
# IndexError: string index out of range
# Можно указать отрицательный индекс - он будет отсчитываться от конца строки:
s = 'Python'
print(s[-1], s[-4])
# Так как строки относятся к неизменяемым типам данных, то изменить символ с указанным индексом нельзя:
# s = "Python"
# s[0] = 'J'
# Traceback (most recent call last):
#   File "Chapter_06.py", line 172, in <module>
#     s[0] = 'J'
# TypeError: 'str' object does not support item assignment
# Чтобы выполнить изменение, можно воспользоваться операцией извлечения среза - фрагмента последовательности, также
# представляющего собой последовательность. Формат записи среза:
# [<Начало>:<Конец>:<Шаг>]
# Все параметры здесь не являются обязательными. Если параметр <Начало> не указан, то используется значение О. Если
# параметр <Конец> не указан, то возвращается фрагмент до конца строки. Символ с индексом, указанным в этом параметре,
# не входит в возвращаемый фрагмент. Если параметр <Шаг> не указан, то используется значение 1. В качестве значения
# параметров можно указать отрицательные значения. Примеры:
# - получение копии строки:
s = 'Python'
print(s[:])         # Возвращается фрагмент от позиции 0 до конца строки
# - вывод символов в обратном порядке:
print(s[::-1])      # Указываем отрицательное значение в параметре <Шаг>
# - замена первого символа в строке:
print('J' + s[1:])  # Извлекаем фрагмент от символа 1 до конца строки
# - удаление последнего символа:
print(s[:-1])       # Возвращается фрагмент от 0 до len(s)-1
# - получение первого символа в строке:
print(s[0:1])       # Символ с индексом 1 не входит в диапазон
# - получение последнего символа:
print(s[-1:])       # Получаем фрагмент от len(s)-1 до конца строки
# - вывод символов с индексами 2, 3 и 4:
print(s[2:5])       # Возвращаются символы с индексами 2, З и 4
# Узнать длину строки (количество символов в ней) позволяет функция len():
print(len('Python'), len('\r\n\t'), len(r'\r\n\t'))
# Можно перебрать все символы в строке с помощью цикла перебора последовательности:
s = 'Python'
for i in s:
    print(i, end=' ')
print('')
# Выполнить конкатенацию строк позволяет оператор +:
print('Строка1' + 'Строка2')
s = 'Строка1'
print(s + 'Строка2')
# Кроме того, можно выполнить неявную конкатенацию строк, записав их через пробел:
print('Строка1' 'Строка2')
# Однако выполнить неявную конкатенацию переменной и строки нельзя - это вызовет ошибку:
# print(s 'Строка2')
# File '/Chapter_06.py', line 213
#     print(s 'Строка2')
# SyntaxError: invalid syntax
# При необходимости объединить строку со значением другого типа (например, с числом) следует произвести явное
# преобразование типов с помощью функции str():
print('string' + str(10))
# Еще строки поддерживают операцию повторения, проверки на вхождение и невхождение.
# Повторить строку указанное количество раз можно с помощью оператора *, выполнить проверку на вхождение фрагмента в
# строку позволяет оператор in, а проверить на невхождение - оператор not in:
print('-' * 20)
print('yt' in 'Python')       # Найдено
print('yt' in 'Perl')         # Не найдено
print('PHP' not in 'Python')  # Не найдено


# 6.3. Форматирование строк
print('6.3. Форматирование строк')
# При форматировании указанная строка объединяется со значениями любых других типов.
# Форматирование выполняется быстрее конкатенации.
# Операция форматирования записывается в следующем формате:
# <Строка специального формата> % <Значения>
# Внутри параметра <Строка специального формата> могут быть указаны спецификаторы, имеющие следующий синтаксис:
# %[(<Ключ>)][<Флаг>][<Ширина>][.<Точность>]<Тип преобразования>
# Количество спецификаторов внутри строки должно быть равно количеству элементов в параметре <Значения>. Если
# спецификатор один, то параметр <Значения> может содержать одно значение, в противном случае следует задать кортеж.
# Примеры:
print('%s' % 10)                      # Один элемент
print('%s - %s - %s' % (10, 20, 30))  # Несколько элементов
# Параметры внутри спецификатора имеют следующий смысл:
# - <Ключ> - ключ словаря. Если задан ключ, то в параметре <Значения> необходимо указать словарь, а не кортеж:
print('%(name)s - %(year)s' % {'year': 1978, 'name': 'Nik'})

# - <Флаг> - флаг преобразования. Может содержать следующие значения:
#  - # - у восьмеричных чисел добавляет в начало комбинацию символов 0o, у шестнадцатеричных - комбинацию символов 0x
# (если используется тип х) или 0X (если используется тип X), у вещественных чисел предписывает всегда выводить дробную
# точку, даже если в параметре <Точность> задано значение 0:
print('%#o %#o %#o' % (0o77, 0xff, 10))
print('%#x %#x %#x' % (0o77, 0xff, 10))
print('%#X %#X %#X' % (0o77, 0xff, 10))
print('%#.0F %.0F' % (300, 300))
#  - 0 - вывод ведущих нулей у чисел:
print("'%d' - '%05d'" % (3, 3))  # 5 - ширина поля
#  - - выравнивание по левой границе области (по умолчанию используется выравнивание по правой границе). Если флаг
# указан одновременно с флагом 0, то действие последнего будет отменено. Примеры:
print("'%5d' - '%-5d'" % (3, 3))    # 5 - ширина поля
print("'%05d' - '%-05d'" % (3, 3))
# пробел - вывод пробела перед положительным числом и минуса - перед отрицательным:
print("'% d' - '% d'" % (-3, 3))
#  + - вывод знака как у отрицательных, так и у положительных чисел. Если флаг + указан одновременно с флагом пробел, то
# действие последнего будет отменено. Пример:
print("'%+d' - '%+d'" % (-3, 3))

# - <Ширина> - минимальная ширина поля. Если строка не помещается в указанную ширину, значение игнорируется, и строка
# выводится полностью. Примеры:
print("'%10d' - '%-10d'" % (3, 3))
print("'%3s' - '%10s'" % ('string', 'string'))
# Вместо значения ширины можно указать символ "*". В этом случае ширину следует задать внутри кортежа. Пример:
print("'%*s' - '%10s'" % (10, 'string', 'str'))

# - <Точность>- количество знаков после точки у вещественных чисел. Перед этим параметром обязательно должна стоять
# точка. Пример:
print('%s %f %.2f' % (math.pi, math.pi, math.pi))
# Вместо значения точности можно указать символ "*". В этом случае точность следует задать внутри кортежа. Пример:
print("'%*.*f'" % (8, 5, math.pi))

# - <Тип преобразования>
#  - s - преобразование выводимого значения в строку с помощью функции str():
print('%s' % 'Обычная строка')
print('%s %s %s' % (10, 10.52, [1, 2, 3]))
#  - r - преобразование выводимого значения в строку с помощью функции repr():
print('%r' % 'Обычная строка')
#  - а - преобразование выводимого значения в строку вызовом функции ascii():
print('%a' % 'строка')
#  - с - вывод символа с указанным кодом. Выведем числовое значение и соответствующий ему символ:
for i in range(33, 127):
    print('%s => %c' % (i, i))
#  - d и i - вывод целой части заданного числа:
print('%d %d %d' % (10, 25.6, -80))
print('%i %i %i' % (10, 25.6, -80))
#  - о - вывод заданного целого числа в восьмеричном представлении:
print('%o %o' % (0o77, 10))
print('%#o %#o' % (0o77, 10))
# При попытке вывести таким образом вещественное число возникнет ошибка;
#  - х - вывод заданного целого числа в шестнадцатеричном представлении в нижнем регистре (при попытке вывести
#  вещественное число возникнет ошибка):
print('%x %x' % (0xff, 10))
print('%#x %#x' % (0xff, 10))
#  - X - вывод заданного целого числа в шестнадцатеричном представлении в верхнем регистре (при попытке вывести
#  вещественное число возникнет ошибка):
print('%X %X' % (0xff, 10))
print('%#X %#X' % (0xff, 10))
#  - f и F - вывод заданного вещественного числа в десятичном представлении:
print('%f %f %f' % (300, 18.65781452, -12.5))
print('%F %F %F' % (300, 18.65781452, -12.5))
print('%#.0F %.0F' % (300, 300))
#  - е - вывод заданного вещественного числа в экспоненциальной форме (буква е выводится в нижнем регистре):
print('%e %e' % (3000, 18657.81452))
#  - Е - вывод заданного вещественного числа в экспоненциальной форме (буква Е выводится в верхнем регистре):
print('%E %E' % (3000, 18657.81452))
#  - g - эквивалентно f или е (выбирается более короткая запись числа):
print('%g %g %g' % (0.086578, 0.000086578, 1.865E-005))
#  - G - эквивалентно F или E (выбирается более короткая запись числа):
print('%G %G %G' % (0.086578, 0.000086578, 1.865E-005))

# Если внутри строки необходимо использовать символ процента, этот символ следует удвоить, иначе будет выведено
# сообщение об ошибке:
# print('%%s' % '- это символ процента')  # Ошибка
# Traceback (most recent call last):
#   File "/Chapter_06.py", line 322, in <module>
#     print('%%s' % '- это символ процента') # Ошибка
#           ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~
# TypeError: not all arguments converted during string formatting
print('%% %s' % '- это символ процента')  # Нормально
# Форматирование строк очень удобно использовать при передаче данных в шаблон веб-страницы. Для этого заполняем словарь
# данными и указываем его справа от символа %, а сам шаблон - слева. Продемонстрируем это на примере test_00028.py.
# Результат выполнения:
# <html>
# <head><title>Это название документа</title>
# </head>
# <body>
# <h1>Это заголовок первого уровня</hl>
# <div>Это основное содержание страницы</div>
# </body>
# </html>

# Для форматирования строк также можно использовать следующие методы, поддерживаемые объектом строки:
# - expandtabs([<Ширина поля>])- заменяет каждый символ табуляции в текущей строке пробелами так, чтобы общая ширина
# фрагмента вместе с текстом, расположенным перед символом табуляции, была равна указанной величине. Если параметр не
# указан, то ширина поля предполагается равной 8 символам. Пример:
s = '1\t12\t123\t'
print("'%s'" % s.expandtabs(4))
# В этом примере ширина задана равной четырем символам. Поэтому во фрагменте 1\t табуляция будет заменена тремя
# пробелами, во фрагменте 12\t - двумя пробелами, а во фрагменте 123\t - одним пробелом. Во всех трех фрагментах ширина
# будет равна четырем символам.
# Если перед символом табуляции нет текста или количество символов перед табуляцией равно указанной в вызове метода
# ширине, то табуляция заменяется указанным количеством пробелов:
s = '\t'
print("'%s' - '%s'" % (s.expandtabs(), s.expandtabs(4)))
s = '1234\t'
print("'%s'" % s.expandtabs(4))
# Если количество символов перед табуляцией больше ширины, то табуляция заменяется пробелами таким образом, чтобы ширина
# фрагмента вместе с текстом делилась без остатка на указанную ширину:
s = '12345\t123456\t1234567\t1234567890\t'
print("'%s'" % s.expandtabs(4))
# Таким образом, если количество символов перед табуляцией больше 4, но менее 8, то фрагмент дополняется пробелами до 8
# символов. Если количество символов больше 8, но менее 12, то фрагмент дополняется пробелами до 12 символов и т. д. Все
# это справедливо при указании, в качестве параметра числа 4;

# - center(<Ширина>[, <Символ>]) - выравнивает текущую строку по центру внутри поля указанной ширины с добавлением слева
# и справа символов из второго параметра (если он не указан, будут добавлены пробелы):
s = 'str'
print(s.center(15), s.center(11, '-'))
# Теперь произведем выравнивание трех фрагментов шириной 15 символов: первого - по правому краю, второго - по левому, а
# третьего - по центру:
s = 'str'
print("'%15s' '%-15s' '%s'" % (s, s, s.center(15)))
# Если количество символов в текущей строке превышает ширину поля, то значение ширины игнорируется и строка возвращается
# полностью:
s = 'string'
print(s.center(6), s.center(5))

# - ljust(<Ширина>[, <Символ>]) - выравнивает текущую строку по левому краю внутри поля указанной ширины с добавлением
# справа символов из второго параметра (если он не указан, будут добавлены пробелы). Если количество символов в текущей
# строке превышает ширину поля, то значение ширины, игнорируется и строка возвращается полностью. Примеры:
s = 'string'
print(s.ljust(15), s.ljust(15, '-'))
print(s.ljust(6), s.ljust(5))

# - rjust(<Ширина>[, <Символ>]) - выравнивает текущую строку по правому краю внутри поля указанной ширины с добавлением
# слева символов из второго параметра (если он не указан, будут добавлены пробелы). Если количество символов в текущей
# строке превышает ширину поля, то значение ширины, игнорируется и строка возвращается полностью. Пример:
s = 'string'
print(s.rjust(15), s.rjust(15, '-'))
print(s.rjust(6), s.rjust(5))

# - zfill(<Ширина>) - выравнивает текущую строку по правому краю внутри поля указанной ширины с добавлением слева нулей.
# Если количество символов в текущей строке превышает ширину поля, то значение ширины, игнорируется и строка
# возвращается полностью. Примеры:
print('5'.zfill(20), '123456'.zfill(5))


# 6.4. Метод format()
print('6.4. Метод format()')
# Для форматирования строк можно использовать метод format(). Он имеет следующий синтаксис вызова:
# <Строка специального формата>.format(*args, **kwargs)
# В качестве результата возвращается отформатированная строка.
# В параметре <Строка специального формата> внутри символов фигурных скобок {и} указываются спецификаторы, имеющие
# следующий синтаксис:
# {[<Поле>][!<Функция>][:<Формат>]}
# Все символы, расположенные вне фигурных скобок, выводятся без преобразований. Если внутри строки необходимо
# использовать символы {и}, то эти символы следует удвоить, иначе возбуждается исключение ValueError, например:
print('Символы {{ и }} - {0}'.format('специальные'))

# - <Поле> - параметр метода format(), в котором указано выводимое значение, в виде его порядкового номера (нумерация
# начинается с нуля) или имени. Допустимо комбинировать позиционные и именованные параметры, при этом именованные
# параметры следует указать последними. Примеры:
print('{0} - {1} - {2}'.format(10, 12.3, 'string'))          # Индексы
arr = [10, 12.3, 'string']
print('{0} - {1} - {2}'.format(*arr))                        # Индексы
print('{model} - {color}'.format(color='red', model='BМW'))  # Имена
d = {'color': 'red', 'model': 'BМW'}
print('{model} - {color}'.format(**d))                       # Имена
print('{color} - {0}'.format(2015, color='red'))             # Комбинация
# В вызове метода format() можно указать список, словарь или объект. Для доступа к элементам списка по индексу внутри
# строки формата применяются квадратные скобки, а для доступа к элементам словаря или атрибутам объекта - точечная
# нотация. Пример:
arr = [10, [12.3, 'string']]
print('{0[0]} - {0[1][0]} - {0[1][1]}'.format(arr))          # Индексы
print('{arr[0]} - {arr[1][1]}'.format(arr=arr))              # Индексы


class Car:
    color = 'red'
    model = 'BMW'


car = Car()
print('{0.model} - {0.color}'.format(car))                   # Атрибуты объекта
# Существует также краткая форма записи, при которой <Поле> не указывается. В этом случае скобки без заданного индекса
# нумеруются слева направо, начиная с нуля. Пример:
print('{} - {} - {} - {n}'.format(1, 2, 3, n = 4))  # '{0} - {1} - {2} - {n}'
print('{} - {} - {n} - {}'.format(1, 2, 3, n = 4))  # '{0} - {1} - {n} - {2}'

# - <Функция> - обозначение функции, обрабатывающей значение перед вставкой в строку. Если указано обозначение s, то
# значение обрабатывается функцией str() , если r, то функцией repr(), а если а, то функцией ascii(). Если параметр не
# указан, для преобразования значения используется функция str(). Пример:
print('{0!s}'.format('строка'))  # str()
print('{0!r}'.format('строка'))  # repr()
print('{0!a}'.format('строка'))  # ascii()

# - <Формат> - должен иметь следующий синтаксис:
# [[<Заполнитель>]<Выравнивание>][<Знак>][#][0][<Ширина>][,][_][.<Точность>][<Преобразование>]
#  - <Ширина> - минимальная ширина поля. Если выводимое значение не помещается в указанную ширину, то ширина,
# игнорируется и значение выводится полностью. Пример:
print("'{0:10}' '{1:3}'".format(3, 'string'))
# Ширину поля можно передать в качестве параметра в методе format(). В этом случае вместо значения ширины внутри
# фигурных скобок указывается индекс соответствующего параметра. Пример:
print("'{0:{1}}'".format(3, 10))  # 10 - это ширина поля
#  - <Выравнивание>:
# < - по левому краю;
# > - по правому краю (поведение по умолчанию);
# ^ - по центру поля.
# Пример:
print("'{0:<10}' '{1:>10}' '{2:^10}'".format(3, 3, 3))
# = - знак числа выравнивается по левому краю, а число - по правому:
print("'{0:=10}' '{1:=10}'".format(-3, 3))
# Как видно из приведенного примера, пространство между знаком и числом по умолчанию заполняется пробелами, а знак у
# положительного числа не указывается. Чтобы вместо пробелов пространство заполнялось нулями, необходимо указать нуль
# перед шириной поля, например:
print("'{0:=010}' '{1:=010}'".format(-3, 3))
# Начиная с Python 3.10, такое же поведение характерно и при выводе строк:
print("'{0:10}'".format('string'))
print("'{0:010}'".format('string'))
#  - <Заполнитель> - символ, которым будет заполняться свободное пространство в поле (по умолчанию пробел):
print("'{0:0=10}' '{1:0=10}'".format(-3, 3))
print("'{0:*<10}' '{1:*>10}' '{2:.^10}'".format(3, 3, 3))
#  - <Знак> - управляет выводом знака числа:
# +- вывод знака как у отрицательных, так и у положительных чисел;
# - - вывод знака только у отрицательных чисел (значение по умолчанию);
# пробел - вывод пробела у положительных чисел и минуса у отрицательных.
# Примеры:
print("'{0:+}' '{1:+}' '{0:-}' '{1:-}'".format(3, -3))
print("'{0: }' '{1: }'".format(3, -3))                  # Пробел
#  - <Преобразование> - у целых чисел:
#   - b - в двоичную систему счисления:
print("'{0:b}' '{0:#b}'".format(3))
#   - с - заданного числа в соответствующий символ:
print("'{0:c}'".format(167))
#   - d - в десятичную систему счисления;
#   - n - аналогично опции d, но учитывает настройки локали. Например, выведем большое число с разделением тысячных
#   разрядов пробелом (точнее, символом с кодом \xao, который при выводе преобразуется в пробел):
print(locale.setlocale(locale.LC_NUMERIC, 'ru_RU.UTF-8'))
print('{0:n}'.format(100000000).replace('\uffa0', ' '))
# Также можно разделить тысячные разряды запятой, указав ее в строке формата:
print('{0:,d}'.format(100000000))
# или символами подчеркивания - таким же образом:
print('{0:_d}'.format(100000000))
#   - о - в восьмеричную систему счисления:
print("'{0:d}' '{0:o}' '{0:#o}'".format(511))
#   - x - в шестнадцатеричную систему счисления в нижнем регистре:
print("'{0:x}' '{0:#x}'".format(255))
#   - X - в шестнадцатеричную систему счисления в верхнем регистре:
print("'{0:X}' '{0:#X}'".format(255))
#  - <Преобразование>- у вещественных чисел:
#   - f и F - в десятичную систему счисления:
print("'{0:f}' '{1:f}' '{2:f}'".format(30, 18.6578145, -2.5))
# По умолчанию выводимое число имеет шесть знаков после запятой. Задать другое количество знаков после запятой можно в
# параметре <Точность>, например:
print("'{0:.7f}' '{1:.2f}'".format(18.6578145, -2.5))
#   - e - в экспоненциальную форму (буква ев нижнем регистре):
print("'{0:e}' '{1:e}'".format(3000, 18657.81452))
#   - E - в экспоненциальную форму (буква Ев верхнем регистре):
print("'{0:E}' '{1:E}'".format(3000, 18657.81452))
# Здесь количество знаков после запятой по умолчанию также равно шести, но можно указать другое количество знаков в
# параметре <Точность>:
print("'{0:.2e}' '{1:.2E}'".format(3000, 18657.81452))
#   - g - эквивалентно f или е(выбирается более короткая запись числа):
print("'{0:g}' '{1:g}'".format (0.086578, 0.000086578))
#   - G - эквивалентно f или Е(выбирается более короткая запись числа):
print("'{0:G}' '{1:G}'".format(0.086578, 0.000086578))
#   - n - аналогично опции g, но учитывает настройки локали;
#   - % - умножает число на 100 и добавляет символ процента в конец. Значение отображается в соответствии с опцией f.
# Пример:
print("'{0:%}' '{1:.4%}'".format(0.086578, 0.000086578))


# 6.4.1. Форматируемые строки
print('6.4.1. Форматируемые строки')
# Форматируемая строка - это более компактная и удобная альтернатива методу format(). Форматируемая строка предваряется
# буквой f или F. В нужных местах такой строки записываются команды на вставку в эти места значений, хранящихся в
# переменных,- точно так же, как и в строках специального формата, описанных ранее. Такие команды имеют следующий
# синтаксис:
# {[<Переменная>][!<Функция>][:<Формат>]}
# Параметр <Переменная> задает имя переменной, из которой будет извлечено вставляемое в строку значение. Вместо имени
# переменной можно записать выражение, вычисляющее значение, которое нужно вывести. Параметры <Функция> и <Формат> имеют
# то же назначение и записываются так же, как и в случае метода format(). Примеры:
a = 10; b = 12.3; s = 'string'
print(f'{a} - {b} - {s}')  # Простой вывод чисел и строк
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# 95

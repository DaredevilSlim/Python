#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Глава 1
# 1.4. Принципы написания Руthоn-программ
# Программа, написанная на Python, представляет собой обычный текстовый файл с расширением ру (будет исполнен обычным
# интерпретатором python.exe) или pyw (будет исполнен «оконным» интерпретатором pythonw.exe).
# Для написания Руthоn-программ, как уже ранее отмечалось, можно использовать, помимо IDLE, любой подходящий текстовый
# редактор: стандартный Блокнот, Notepad++ (https://notepad-plus-plus.org/), Visual Studio Code
# (https://code.visualstudio.com/) и др.
# Также существует ряд специализированных текстовых редакторов, предназначенных именно для Руthоn-программистов, в
# частности PyChaпn' (https://www.jetbrains.com/ru-ru/pycharm/).
# Инструкции, записанные в коде программы, выполняются последовательно, в порядке сверху вниз.
# Каждая инструкция Python должна располагаться на отдельной строке. Признаком конца инструкции является перевод строки.
# Пример программы из двух выражений (test_00003.py).
# Первое выражение складывает числа 15, 20 и 30 и заносит сумму в переменную с именем х (переменная - ячейка памяти,
# имеющая уникальное имя, способная хранить какое-либо значение - например, число, и создаваемая при присваивании ей
# значения). Второе выражение выводит содержимое этой переменной - число 65 - в консоли.
# В первом выражении используются два оператора. Оператором называется языковая конструкция, выполняющая над переданными
# ему значениями какое-либо элементарное действие (например, сложение чисел или присваивание результата указанной
# переменной). Оператор сложения обозначается привычным символом +, а оператор присваивания - символом =.
# В Windows перевод строки формируется комбинацией символов \r (перевод каретки) и \n (перевод строки), в UNIX - одним
# символом \n.
# Если загрузить файл Руthоn-программы по протоколу FTP в бинарном режиме, то символ \r вызовет фатальную ошибку. По
# этой причине файлы по протоколу FTP следует загружать только в текстовом (ASCII) режиме - тогда символ \r будет удален
# автоматически.
# Если строка с инструкцией получилась слишком длинной, инструкцию можно разделить на несколько строк одним из следующих
# способов:
# - поставить в месте разрыва строк символ \, сразу после которого вставить перевод строки(как обычно, нажатием клавиши
# <Enter>):
x = 15 + 20 + \
    30
print(x)
# Как правило, вторая и все последующие строки, содержащие длинное ,выражение, набираются с отступами слева - для
# улучшения читаемости кода. Следует только формировать эти отступы исключительно пробелами и делать одинаковой длины
# (содержащими одинаковое количество пробелов).
# При вводе подобного рода многострочной инструкции в интерпретаторе, работающем в интерактивном режиме, строки с
# продолжением инструкции помечаются расположенным слева приглашением в виде трех точек( ... , а не >>>, как обычно).
# Кроме того, интерпретатор сам выводит последующие строки с отступами. Чтобы завершить ввод многострочной инструкции,
# следует, введя ее последнюю строку, нажать клавишу <Enter> (при этом после многострочной инструкции будет создана
# пустая строка с приглашением из трех точек).
# - заключить выражение в круглые скобки, внутри которых вставить нужное количество переводов строки:
x = (15 +
     20 +
     30)
print(x)
# - определение списка и словаря, при оформлении которых используются квадратные и фигурные скобки соответственно, также
# можно разбить на несколько строк:
#  - пример определения списка:
arr = [15, 20,
       30]
print(arr)
#  - пример определения словаря:
arr = {'x': 15, 'y': 20,
       'z': 30}
print(arr)
# - Короткие инструкции можно записать в одной строке, разделив их символами точки с запятой (;):
x = 15 + 20 + 30; print(x)
# После точки с запятой не возбраняется ставить пробел - для улучшения читаемости кода.
# - Блоки (наборы из произвольного количества инструкций, входящие в состав более сложных инструкций) формируются
# отступами слева. Такие отступы должны формироваться исключительно пробелами и быть одинаковой длины (т. е. содержать
# одинаковое количество пробелов). Символы табуляции в отступах не допускаются и при выполнении программы вызывают
# возникновение ошибки.
# Код программы, выводящей последовательно числа от 1 до 10, которые разделяются тремя дефисами (test_00004.py).
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#







# 28

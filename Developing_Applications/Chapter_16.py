#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from os.path import sep

# ГЛАВА 16
print('ГЛАВА 16')
# Работа с файлами и каталогами


# 16.1. Открытие файлов
print('16.1. Открытие файлов')
# Для открытия файла применяется функция open(), имеющая следующий формат вызова:
# open(<Путь к файлу>[, mode= 'r'][, buffering=-1][, encoding=None][, errors=None][, newline=None][, closefd=True])
# Задаваемый путь к открываемому файлу может быть абсолютным или относительным. Для разделения сегментов путей можно
# применять как обратные, так и прямые слеши (подробнее указание путей рассмотрено в разд. 16.1.1).
# Параметр mode указывает режим открытия файла в виде строки (чтение, запись или чтение и запись), содержащей одно из
# следующих обозначений:
# - r - чтение. Если файл не существует, генерируется исключение FileNotFoundError; Python помечает место, с которого
# начнется чтение из файла или запись в него, особым указателем. После открытия файла только на чтение этот указатель
# устанавливается на начало файла;
# - r+ - чтение и запись. Указатель устанавливается на начало файла. Если файл не существует, генерируется исключение
# FileNotFoundError;
# - w - запись. Указатель устанавливается на начало файла. Если файл не существует, он будет создан, если существует -
# перезаписан;
# - w+ - чтение и запись. Указатель устанавливается на начало файла. Если файл не существует, он будет создан, если
# существует - перезаписан;
# - а - дозапись. Указатель устанавливается на конец файла. Если файл не существует, он будет создан, если существует,
# данные будут добавлены в него;
# - а+ - чтение и дозапись. Указатель устанавливается на конец файла. Если файл не существует, он будет создан, если
# существует, данные будут добавлены в него;
# - х - создание файла для записи. Если файл уже существует, генерируется исключение FileExistsError;
# - х+ - создание файла для чтения и записи. Если файл уже существует, генерируется исключение FileExistsError.
# После собственно обозначения режима может следовать обозначение подрежима открытия файла, задающее формат читаемых или
# записываемых данных:
# - b - двоичный (бинарный) подрежим. Читаемые и записываемые данные представляются объектами типа bytes;
# - t - текстовый подрежим (используется по умолчанию в Windows). Читаемые и записываемые данные представляются
# строками.
# В текстовом подрежиме автоматически выполняется обработка символов конца строки - так, в Windows при чтении вместо
# символов \r\n будет подставлен символ \n. Для примера создадим файл file.txt и запишем в него две строки:
f = open(r'./Examples/file.txt', 'w')  # Открываем файл на запись
f.write('String1\nString2')            # Записываем две строки в файл
f.close()                              # Закрываем файл
# Поскольку мы указали режим w, то, если файл не существует, он будет создан, а если существует - перезаписан.
# Теперь выведем содержимое файла в двоичном и текстовом подрежимах:
# Двоичный подрежим (символ \r остается)
with open(r'./Examples/file.txt', 'rb') as f:
    for line in f:
        print(repr(line))
print()
# Текстовый подрежим (символ \r удаляется)
with open(r'./Examples/file.txt', 'r') as f:
    for line in f:
        print(repr(line))
print()
# Для ускорения работы производится буферизация записываемых данных. Информация из буфера записывается в файл полностью
# только в момент закрытия файла или после вызова функции или метода flush(). В необязательном параметре buffering можно
# указать размер буфера. Если указано значение 0, то данные будут сразу записываться в файл (допустимо только в двоичном
# подрежиме). Значение 1 используется при построчной записи в файл (допустимо только в текстовом подрежиме). Другое
# положительное число задает примерный размер буфера, а отрицательное значение (или отсутствие значения) означает
# установку размера, применяемого в системе по умолчанию. По умолчанию текстовые файлы буферизуются построчно, а
# двоичные - частями, размер которых интерпретатор выбирает самостоятельно в диапазоне от 4096 до 8192 байтов.
# При чтении файла в текстовом подрежиме производится попытка преобразовать данные в кодировку Unicode, а при записи
# выполняется обратная операция - строка преобразуется в последовательность байтов в определенной кодировке.
# По умолчанию назначается кодировка, применяемая в системе. Если преобразование невозможно, генерируется исключение.
# Указать кодировку, которая будет использоваться при записи и чтении файла, позволяет параметр encoding. Для примера
# запишем данные в кодировке UTF-8:
f = open(r'./Examples/file.txt', 'w', encoding='utf-8')
f.write('Строка')  # Записываем строку в файл
f.close()          # Закрываем файл
# При открытии этого файла для чтения следует явно указать кодировку:
with open(r'./Examples/file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(repr(line))
print()
# При работе с текстовыми файлами в кодировках UTF-8, UTF-16 и UTF-32 следует учитывать, что в начале файла может
# присутствовать метка порядка байтов (ВОМ). Для кодировки UTF-8 эта метка является необязательной, и в предыдущем
# примере она не была добавлена в файл при записи. Чтобы ВОМ была добавлена, в параметре encoding следует указать
# значение utf-8-sig. Запишем строку в файл в кодировке UTF-8 с ВОМ:
f = open(r'./Examples/file.txt', 'w', encoding='utf-8-sig')
f.write('Строка')  # Записываем строку в файл
f.close()          # Закрываем файл
# Теперь прочитаем файл с разными значениями параметра encoding:
with open(r'./Examples/file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(repr(line))
print()
with open(r'./Examples/file.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        print(repr(line))
print()
# Если неизвестно, есть ли ВОМ в файле, и необходимо получить данные без нее, то при чтении файла в кодировке UTF-8
# всегда следует указывать кодировку utf-8-sig.
# При указании кодировок utf-16 и utf-32 в параметре encoding обработка ВОМ производится автоматически: при записи ВОМ
# автоматически вставляется в начало файла, а при чтении она игнорируется. Запишем строку в файл, а затем прочитаем ее
# из файла:
with open(r'./Examples/file.txt', 'w', encoding='utf-16') as f:
    f.write('Строка')
with open(r'./Examples/file.txt', 'r', encoding='utf-16') as f:
    for line in f:
        print(repr(line))
print()
# При указании кодировок utf-16-le, utf-16-be, utf-32-le и utf-32-be ВОМ необходимо добавить в начало файла
# самостоятельно, а при чтении удалить ее.
# В параметре errors можно указать уровень обработки ошибок. Возможные значения:
# "strict" (при ошибке генерируется исключение ValueError - значение по умолчанию),
# "replace" (неизвестный символ заменяется знаком вопроса или символом с кодом \ufffd),
# "ignore" (неизвестные символы игнорируются), "xmlcharrefreplace" (неизвестный символ заменяется последовательностью
# &#хххх) и "backslashreplace" (неизвестный символ заменяется последовательностью \uxxxx).
# Параметр newline задает режим обработки символов конца строки. Поддерживаемые им значения таковы:
# - None (значение по умолчанию) - выполняется стандартная обработка символов конца строки. Например, в Windows при
# чтении символы \r\n преобразуются в символ \n, а при записи производится обратное преобразование;
# - "" (пустая строка) - обработка не выполняется;
# - "<Специальный символ>" - для обозначения конца строки используется заданный специальный символ, в качестве которого
# можно указать \r\n, \r и \n.


# 16.1.1. Указание путей к файлам и каталогам
print('16.1.1. Указание путей к файлам и каталогам')
# В путях к файлам и каталогам для разделения отдельных сегментов (обозначений дисков, имен каталогов и файлов) можно
# применять как обратные, так и прямые слеши.
# Символ-разделитель сегментов путей, применяемый в текущей операционной системе, хранится в переменной sep из модуля
# os.path. Выведем разделитель, применяемый в Windows:
print(sep)
# При использовании обратных слешей следует помнить, что в Python они являются специальными символами (подробности -
# в разд. 6.1.1). По этой причине обратные слеши следует заменять спецсимволами \\ или вместо обычных строк использовать
# необрабатываемые (описаны в разд. 6.1.1). Примеры:
print('C:\\temp\\new\\file.txt')  # Правильно
print('C:\\temp\\new\\file.txt')  # Правильно
print('C:\temp\new\file.txt')     # Неправильно!!!
# В последнем примере интерпретатор принял последовательность символов \f за специальный символ, что привело к искажению
# заданного нами пути. Если такой искаженный путь передать функции open(), возникнет исключение OSError.
# Кроме того, слеш, расположенный в конце строки, необходимо удваивать даже при использовании неформатированных строк:
# print(r'C:\temp\new\')  # Неправильно!!!
# File "/Chapter_16.py", line 134
#     print(r'C:\temp\new\')
#           ^
# SyntaxError: unterminated string literal (detected at line 134)
print(r'C:\temp\new\\')  # Правильно
# В первом примере последний слеш экранирует закрывающую кавычку, что приводит к синтаксической ошибке. Решить эту
# проблему можно, удвоив последний слеш. Однако тогда два слеша превратятся в четыре (см. второй пример). Так что в этой
# ситуации лучше использовать обычные строки, например:
print('C:\\temp\\new\\')       # Правильно
print('C:\\temp\\new\\'[:-1])  # Можно и удалить слеш
# Вместо абсолютного пути (отсчитываемого от обозначения диска) можно указать относительный, который отсчитывается от
# текущего рабочего каталога (о нем - позже). Возможны следующие варианты:
# - если открываемый файл находится в текущем рабочем каталоге, можно указать только имя файла:
# open(r'filel.txt')
# - если открываемый файл расположен в каталоге, вложенном в текущий рабочий каталог, перед именем файла через слеш
# указываются имена каталогов, в которые последовательно вложен файл:
# open(r"folder1/file2.txt")
# open(r"folder2/folder3/file3.txt")
# - если каталог с файлом расположен ниже уровнем, перед именем файла указываются две точки и слеш ("../"):
# open(r"../file4.txt")
# - если в начале пути расположен слеш, путь отсчитывается от корня текущего диска.
# В этом случае местоположение текущего рабочего каталога не имеет значения:
# open(r"/book/folder4/file4.txt")
# open(r"/book/folder5/folder6/file5.txt")


# 16.1.2. Текущий рабочий каталог
print('16.1.2. Текущий рабочий каталог')
# Текущий рабочий каталог - это каталог, от которого интерпретатор отсчитывает относительные пути файлов. По умолчанию
# текущим рабочим является следующий каталог:
# - при запуске интерпретатора в интерактивном режиме - каталог, в котором установлен Python (например, C:\Python310);
# - при запуске Python-файла щелчком мыши - каталог, в котором хранится запущенный файл;
# - при запуске Python-файла из консоли - каталог, из которого был запущен файл. Например, если запустить консоль,
# выполнить в ней переход в каталог d:\work и запустить Python-файл c:\book\program.py, текущим рабочим станет каталог
# d:\work.
# Получить путь к текущему рабочему каталогу можно вызовом функции getcwd() из модуля os:
print(os.getcwd())
# Задать в качестве текущего рабочего каталог с указанным путем можно вызовом функции chdir(<Путь>) из модуля os:
# os.chdir(r'c:\book')
# Указать в качестве текущего рабочего каталог, в котором хранится запущенный Python-файл, можно, вставив в код этого
# файла следующие инструкции:
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Переменная __file__ хранит в разных случаях путь к запущенному файлу или только имя файла без пути. Чтобы
# гарантированно получить полный путь к файлу, следует-передать значение переменной в функцию abspath() из модуля
# os.path. Функция dirname() извлекает из переданного ей полного пути к файлу путь к хранящему его каталогу, который
# передается функции chdir().


# 16.2. Чтение и запись данных: объектные инструменты
print('16.2. Чтение и запись данных: объектные инструменты')
# Функция open() возвращает объект, представляющий открытый файл. Рассмотрим основные методы, поддерживаемые этим
# объектом:

# - close() - закрывает текущий файл. При удалении из памяти объекта, представляющего файл, закрытие файла выполняется
# автоматически, поэтому в небольших программах файлы можно не закрывать явно. Тем не менее явное закрытие файла
# является признаком хорошего стиля программирования. Кроме того, при наличии незакрытого файла генерируется
# предупреждающее сообщение: "ResourceWarning: unclosed file".
# Классы объектов-файлов являются менеджерами контекста, поэтому для работы с файлами можно использовать обработчики
# контекста (см.разд. 14.2):
with open(r'./Examples/file.txt', 'w', encoding='cp1251') as f:
    f.write('Строка')  # Записываем строку в файл
# Здесь файл уже закрыт автоматически

# - write(<Значение>) - записывает в текущий файл указанное значение. Если файл открыт в текстовом подрежиме, значение
# должно быть задано в виде строки, если в двоичном подрежиме - в виде последовательности байтов. Метод возвращает
# количество записанных символов или байтов. Пример:
# Текстовый подрежим
with open(r'./Examples/file.txt', 'w', encoding='cp1251') as f:
    f.write('Строка1\nСтрока2')
    f.close()
# Двоичный подрежим
f = open(r'./Examples/file.txt', 'wb')
f.write(bytes('Строка1\nСтрока2', 'cp1251'))
f.write(bytearray('Строка3', 'cp1251'))
f.close()

# - writelines(<Последовательность>) - записывает в текущий файл заданную последовательность. Если файл открыт в
# текстовом подрежиме, элементы последовательности должны представлять собой строки, если в двоичном подрежиме -
# последовательности байтов. Пример:
# Текстовый подрежим
f = open(r'./Examples/file.txt', 'w', encoding='cp1251')
f.writelines(['Строка1\n', 'Строка2'])
f.close()
# Двоичный подрежим
f = open(r'./Examples/file.txt', 'wb')
arr = [bytes('Строка1\n', 'cp1251'), bytes('Строка2', 'cp1251')]
f.writelines(arr)
f.close()

# - writable() - возвращает True, если в текущий файл можно писать, и False - в противном случае:
f = open(r'./Examples/file.txt', 'r')  # Открываем файл дпя чтения
print(f.writable())
f = open(r'./Examples/file.txt', 'w')  # Открываем файл дпя записи
print(f.writable())

# - read([<Количество>]) - считывает данные из текущего файла и возвращает их. Если файл открыт в текстовом подрежиме,
# выдается строка, а если в двоичном - последовательность байтов. Если параметр не указан, возвращается содержимое файла
# от текущей позиции указателя до конца файла. Пример:
# Текстовый подрежим
with open(r'./Examples/file.txt', 'r', encoding='cp1251') as f:
    f.read()
# Двоичный подрежим
with open(r'./Examples/file.txt', 'rb') as f:
    f.read()
# В параметре можно указать количество символов или байтов, которое требуется прочитать из файла. Когда достигается
# конец файла, метод возвращает пустую строку или пустую последовательность байтов. Пример:
f = open(r'./Examples/file.txt', 'r', encoding='cp1251')
print(f.read(8))  # Считываем 8 символов
print(f.read(8))  # Считываем 8 символов
print(f.read(8))  # Достигнут конец файла

# - readline([<Количество>]) - считывает из текущего файла очередную строку и возвращает ее. Если файл открыт в
# текстовом подрежиме, выдается строка, а если в двоичном - последовательность байтов. Возвращаемая строка включает
# символ перевода строки. Исключением является последняя строка - если она не завершается символом перевода строки, то
# таковой добавлен не будет. При достижении конца файла возвращается пустая строка или последовательность байтов.
# Пример:
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 310



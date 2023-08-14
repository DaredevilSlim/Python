#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time      # Подключаем модуля time
import locale    # Подключаем модуля locale
import datetime  # Подключаем модуля datetime

# ГЛАВА 10
# Работа с датой и временем
# Python предоставляет средства для работы со значениями даты и времени, а также комбинациями даты и времени (временными
# отметками). Кроме того, он содержит инструменты для вывода календаря в виде текста или в формате HTML и измерения
# времени выполнения определенных фрагментов программы для целей отладки.


# 10.1 Получение текущих даты и времени
print('10.1 Получение текущих даты и времени')
# - time() - возвращает количество секунд, прошедшее с начала эпохи (обычно с 1 января 1970 г.), в виде вещественного
# числа:
print(time.time())  # Получаем количество секунд

# - gmtime([<Количество секунд>]) - возвращает универсальное время (UTC) в виде объекта struct_time. Если параметр не
# указан, возвращается текущее время. Если параметр указан, время будет соответствующим заданному количеству секунд,
# прошедших с начала эпохи. Примеры:
print(time.gmtime(0))             # Начало эпохи
print(time.gmtime())              # Текущая дата и время
print(time.gmtime(1690476586.0))  # Дата 27.07.2023
# Получить значение конкретного атрибута можно, указав его имя или индекс внутри объекта:
d = time.gmtime()
print(d.tm_year, d[0])
print(tuple(d))  # Преобразование в кортеж

# - localtime([<Количество секунд>]) - возвращает местное время в виде объекта struct_time. Если параметр не указан,
# возвращается текущее время. Если параметр указан, время будет соответствующим заданному количеству секунд, прошедших с
# начала эпохи. Примеры:
print(time.localtime())              # Текущая дата и время
print(time.localtime(1690476586.0))  # Дата 27.07.2023

# - mktime(<Объект struct_time>) - возвращает количество секунд, прошедших с начала эпохи, в виде вещественного числа.
# В качестве параметра указывается объект struct_time или кортеж из девяти элементов. Если указанная дата некорректна,
# возбуждается исключение OverflowError. Примеры:
d = time.localtime(1690476586.0)
print(time.mktime(d))
print(tuple(time.localtime(1690476586.0)))
print(time.mktime((2023, 7, 27, 19, 49, 46, 3, 208, 1)))
print(time.mktime((1940, 0, 31, 5, 23, 43, 5, 31, 0)))
# Объект struct_time, возвращаемый функциями gmtime() и localtime(), содержит следующие атрибуты (указаны тройки вида
# «имя атрибута - индекс - описание»):
# tm_year  - О - год;
# tm_mon   - 1 - месяц (число от 1 до 12);
# tm_mday  - 2 - день месяца (число от 1 до 31);
# tm_hour  - 3 - час (число от 0 до 23);
# tm_min   - 4 - минуты (число от 0 до 59);
# tm_sec   - 5 - секунды (число от 0 до 59);
# tm_wday  - б - день недели (число от 0 для понедельника до 6 для воскресенья);
# tm_yday  - 7 - количество дней, прошедшее с начала года (число от 1 до 366);
# tm_isdst - 8 - флаг коррекции летнего времени (значения 0, 1 или -1).
# Выведем текущие дату и время таким образом, чтобы день недели и месяц были написаны по-русски test_00050.py.


# 10.2. Форматирование даты и времени
print('10.2. Форматирование даты и времени')
# Форматирование даты и времени выполняют следующие функции из модуля time:
# - strftime(<Строка формата>[, <Объект struct_time>]) - возвращает строковое представление даты и времени в
# соответствии с заданной строкой формата. Если второй параметр не указан, будут выведены текущие дата и время. Если во
# втором параметре указан объект struct_time или кортеж из девяти элементов, дата будет соответствовать указанному
# значению. Функция зависит от настройки локали. Примеры:
time.strftime('%d.%m.%Y')  # Форматирование даты
print(time.strftime('%H:%M:%S'))  # Форматирование времени
print(time.strftime('%d.%m.%Y', time.localtime(1691990120.1)))

# - strptime(<Строка с датой>[, <Строка формата>]) - разбирает указанную строку с датой и временем в соответствии с
# заданной строкой формата. Возвращает объект struct_time. Если строка не соответствует формату, возбуждается исключение
# ValueError. Если строка формата не указана, используется строка '%а %Ь %d %Н: %М: %S %Y'. Функция учитывает текущую
# локаль
print(time.strptime('Mon Aug 14 08:20:50 2023'))
print(time.strptime('14.08.2023', '%d.%m.%Y'))
# print(time.strptime('14-08-2023', '%d.%m.%Y'))
# Traceback (most recent call last):
#   File "/Chapter_10.py", line 74, in <module>
#     print(time.strptime('14-08-2023', '%d.%m.%Y'))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/src/Python-3.11.4/Lib/_strptime.py", line 562, in _strptime_time
#     tt = _strptime(data_string, format)[0]
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/src/Python-3.11.4/Lib/_strptime.py", line 349, in _strptime
#     raise ValueError("time data %r does not match format %r" %
# ValueError: time data '14-08-2023' does not match format '%d.%m.%Y'

# asctime([<Объект struct_time>]) - возвращает строку формата '%а %Ь %d %H:%M:%S %Y'. Если параметр не указан, будут
# выведены текущие дата и время. Если в параметре указан объект struct_time или кортеж из девяти элементов, то дата
# будет соответствовать указанному значению.
print(time.asctime())                              # Текущая дата
print(time.asctime(time.localtime(1601990120.0)))  # Дата в прошлом

# - ctime([<Количество секунд>]) - аналогична asctime(), но в качестве параметра принимает количество секунд, прошедших
# с начала эпохи.
print(time.ctime())              # Текущая дата
print(time.ctime(1691990120.0))  # Дата в прошлом
# В параметре <Строка формата> в функциях strftime() и strptime() могут быть использованы следующие комбинации
# специальных символов:
# %y - год из двух цифр (от '00' до '99');
# %Y - год из четырех цифр (например, '2011 ');
# %m - номер месяца с предваряющим нулем (от '01' до '12');
# %b - аббревиатура месяца в зависимости от настроек локали (например, 'янв' для января);
# %В - название месяца в зависимости от настроек локали (например, 'Январь');
# %d - номер дня в месяце с предваряющим нулем (от '01' до '31');
# %j - день с начала года (от '001' до '366');
# %U - номер недели в году (от '00' до '53'). Неделя начинается с воскресенья. Все дни с начала года до первого
# воскресенья относятся к неделе с номером 0;
# %W - номер недели в году (от '00' до '53'). Неделя начинается с понедельника. Все дни с начала года до первого
# понедельника относятся к неделе с номером 0;
# %w - номер дня недели ('0' - для воскресенья, '6' - для субботы);
# %a - аббревиатура дня недели в зависимости от настроек локали (например, 'Пн' для понедельника);
# %A - название дня недели в зависимости от настроек локали (например, 'понедельник');
# %Н - часы в 24-часовом формате (от '00' до '23');
# %I - часы в 12-часовом формате (от '01' до '12');
# %M - минуты (от '00' до '59');
# %S - секунды (от '00' до '59', изредка до '61 ');
# %p - эквивалент значениям АМ и РМ в текущей локали;
# %c - представление даты и времени в текущей локали;
# %x - представление даты в текущей локали;
# %X - представление времени в текущей локали.
locale.setlocale(locale.LC_ALL, '')
print(time.strftime('%x'))  # Представление даты
print(time.strftime('%X'))  # Представление времени
print(time.strftime('%c'))  # Представление даты и времени
# %Z - название часового пояса или пустая строка (например, 'Московское время', 'UTC');
# %% - символ'%'.
# Вывод текущей даты и времени с помощью функции strftime() (test_00051.py)


# 10.3 Приостановка выполнения программы
print('10.3 Приостановка выполнения программы')
# Функция sleep(<Время в секундах>) из модуля time приостанавливает выполнение программы на указанное время. В качестве
# параметра можно указать целое или вещественное число. Пример:
# time.sleep(5)  # 'Засыпаем' на 5 секунд


# 10.4 Значения даты и времени
print('10.4 Значения даты и времени')
# Модуль datetime предоставляет инструменты для работы со значениями даты и времени:
# выполнения арифметических операций, сравнения, вывода в различных форматах и др.
# Предварительно необходимо подключить модуль с помощью инструкции:
# import datetime


# 10.4.1 Временные промежутки
print('10.4.1 Временные промежутки')
# Временной промежуток - это величина разницы между какими-либо временными отметками (т. е. значениями времени и даты).
# Класс timedelta из модуля datetime позволяет выполнять операции над временными промежутками: складывать, вычитать,
# сравнивать и др. Конструктор класса имеет следующий формат:
# timedelta([days][, seconds][, microseconds][, milliseconds][, minutes][, hours][, weeks])
# Все параметры не являются обязательными и по умолчанию имеют значение 0. Их можно записывать как позиционные или как
# именованные. Первые три параметра считаются основными:
# - days - дни (диапазон -999999999 <= days <= 999999999);
# - seconds - секунды (диапазон 0 <= seconds < 3600*24);
# - microseconds - микросекунды (диапазон О <= microseconds < 1000000).
# Примеры:
print(datetime.timedelta(3))
print(datetime.timedelta(0, 2, 10000))
print(datetime.timedelta(days=1, seconds=7200))

# Все остальные параметры автоматически преобразуются в следующие значения:
# - milliseconds - миллисекунды (одна миллисекунда преобразуется в 1000 микросекунд):
print(datetime.timedelta(milliseconds=1))
# - minutes - минуты (одна минута преобразуется в 60 секунд):
print(datetime.timedelta(minutes=1))
# - hours - часы (один час преобразуется в 3600 секунд):
print(datetime.timedelta(hours=1))
# - weeks - недели (одна неделя преобразуется в 7 дней):
print(datetime.timedelta(weeks=1))

# Получить результат можно с помощью следующих атрибутов:
# - days         - дни;
# - seconds      - секунды;
# - microseconds - микросекунды.
d = datetime.timedelta(hours=1, days=2, milliseconds=1)
print(d)
print(d.days, d.seconds, d.microseconds)
# Получить результат в секундах позволяет метод total_seconds():
d = datetime.timedelta(minutes=1)
print(d.total_seconds())
# Над временными промежутками можно производить арифметические операции +, -, /, / /, % и *, использовать унарные
# операторы + и -, а также получать абсолютное значение с помощью функции abs(), вычислять частное и остаток от деления
# нацело функцией divmod():
d1 = datetime.timedelta(days=2)
d2 = datetime.timedelta(days=7)
print(d1 + d2, d2 - d1)  # Сложение и вычитание
print(d2 / d1)           # Деление
print(d1 / 2, d2 / 2.5)  # Деление
print(d2 // d1)          # Деление
print(d1 // 2, d2 // 2)  # Деление
print(d2 % d1)           # Остаток
print(d1 * 2, d2 * 2)    # Умножение
print(2 * d1, 2 * d2)    # Умножение
d3 = -d1
print(d3, abs(d3))
print(divmod(d2, d1))
# Кроме того, можно использовать операторы сравнения =, !=, <, <=, > и >=.
d1 = datetime.timedelta(days=2)
d2 = datetime.timedelta(days=7)
d3 = datetime.timedelta(weeks=1)
print(d1 == d2, d2 == d3)  # Проверка на равенство
print(d1 != d2, d2 != d3)  # Проверка на неравенство
print(d1 < d2, d2 <= d3)   # Меньше, меньше или равно
print(d1 > d2, d2 >= d3)   # Больше, больше или равно
# Также можно получать строковое представление объекта timedelta с помощью функций str() и repr():
d = datetime.timedelta(hours=25, minutes=5, seconds=27)
print(str(d), repr(d))
# Класс timedelta поддерживают следующие атрибуты:
# min        - минимальное значение, которое может иметь объект timedelta;
# max        - максимальное значение, которое может иметь объект timedelta;
# resolution - минимальное возможное различие между значениями timedelta.
# Вывод значения этих атрибутов:
print(datetime.timedelta.min)
print(datetime.timedelta.max)
print(datetime.timedelta.resolution)


# 10.4.2 Значения даты
print('10.4.2 Значения даты')
# Класс date из модуля datetime позволяет выполнять операции над датами. Конструктор класса имеет следующий формат:
# date(<Год>, <Месяц>, <День>)
# В параметрах указываются числа:
# - <Год> - в диапазоне между значениями констант MINYEAR и МАХУЕАR класса datetime (о нем речь пойдет позже). Выведем
# значения этих констант:
print(datetime.MINYEAR, datetime.MAXYEAR)
# - <Месяц> - от 1 до 12 включительно;
# - <День> - от 1 до количества дней в месяце.
# Если значения выходят за диапазон, возбуждается исключение ValueError. Примеры:
print(datetime.date(2023, 8, 14))
# print(datetime.date(2023, 14, 8))  # Неправильное значение для месяца
# Traceback (most recent call last):
#   File "/Chapter_10.py", line 232, in <module>
#     print(datetime.date(2023, 14, 8))  # Неправильное значение для месяца
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: month must be in 1..12

# Для создания даты также можно воспользоваться следующими методами класса date:
# - today() - возвращает текущую дату:
print(datetime.date.today())  # Получение текущей даты
# - fromtimestamp(<Количество секунд>) - возвращает дату, которая соответствует заданному количеству секунд, прошедших
# с начала эпохи:
print(datetime.date.fromtimestamp(time.time()))   # Текущая дата
print(datetime.date.fromtimestamp(1691996144.5))  # Дата 2023-08-14






# fromordinal(<Количество дней с 1-го года>) - возвращает дату, соответствующую количеству дней, прошедших с первого
# года. В качестве параметра указывается число от 1 до datetime.date.max.toordinal().
print(datetime.date.max.toordinal())
print(datetime.date.fromordinal(3652059))
print(datetime.date.fromordinal(1))
# Получить результат можно с помощью следующих атрибутов:
# year  - год (число в диапазоне от MINYEAR до МАХУЕАR);
# month - месяц (число от 1 до 12);
# day   - день (число от 1 до количества дней в месяце).
d = datetime.date.today()  # Текущая дата 2019-03-21
print(d.year, d.month, d.day)
# Над экземплярами класса date можно производить следующие операции:
# date2 = date1 + timedelta - прибавляет к дате указанный период в днях. Значения атрибутов timedelta.seconds и
# timedelta. microseconds игнорируются;
# date2 = date1 - timedelta - вычитает из даты указанный период в днях. Значения атрибутов timedelta.seconds и
# timedelta.microseconds игнорируются;
# timedelta = date1 - date2 - возвращает разницу между датами (период в днях). Атрибуты timedelta.seconds и
# timedelta.microseconds будут иметь значение 0;
# можно также сравнивать две даты с помощью операторов сравнения.
d1 = datetime.date(2015, 4, 3)
d2 = datetime.date(2015, 1, 1)
t = datetime.timedelta(days=10)
print(d1 + t, d1 - t)  # Сложение и вычитание 10 дней
print(d1 - d2)         # Разность между датами
print(d1 < d2, d1 > d2, d1 <= d2, d1 >= d2)
print(d1 == d2, d1 != d2)
# Экземпляры класса date поддерживают следующие методы:
# replace([year][, month][, day]) - возвращает дату с обновленными значениями. Значения можно указывать через запятую в
# порядке следования параметров или присвоить значение названию параметра.
d = datetime.date(2015, 4, 3)
print(d)
print(d.replace(2014, 12))  # Замена года и месяца
print(d.replace(year=2015, month=1, day=31))
print(d.replace(day=30))    # Замена только дня
# strftime(<Строка формата>) - возвращает отформатированную строку. В строке формата можно задавать комбинации
# специальных символов, которые используются в функции strftime() из модуля time.
d = datetime.date(2015, 4, 3)
print(d.strftime('%d.%m.%Y'))
# isoformat() - возвращает дату в формате гггг-мм-дд:
d = datetime.date(2015, 4, 3)
print(d.isoformat())
# ctime() - возвращает строку формата "%а %Ь %d %H:%M:%S %У":
d = datetime.date(2015, 4, 3)
print(d.ctime())
# timetuple() - возвращает объект struct_time с датой и временем:
d = datetime.date(2015, 4, 3)
print(d.timetuple())
# toordinal() - возвращает количество дней, прошедших с 1-ro года:
d = datetime.date(2015, 4, 3)
print(d.toordinal())
print(datetime.date.fromordinal(735691))
# weekday() - возвращает порядковый номер дня в неделе (0 - для понедельника, 6 - для воскресенья):
d = datetime.date(2015, 4, 3)
print(d.weekday())  # 4 - это пятница
# isoweekday() - возвращает порядковый номер дня в неделе (1 - для понедельника, 7 - для воскресенья):
d = datetime.date(2015, 4, 3)
print(d.isoweekday())  # 5 - это пятница
# isocalendar () - возвращает кортеж из трех элементов (год, номер недели в году и порядковый номер дня в неделе):
d = datetime.date(2015, 4, 3)
print(d.isocalendar())
# Наконец, имеется поддержка следующих атрибутов класса:
# min        - минимально возможное значение даты;
# max        - максимально возможное значение даты;
# resolution - минимальное возможное различие между значениями даты.
# Значения этих атрибутов:
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)


# 10.4.3 Класс time
print('Класс time:')
# Класс time из модуля datetime позволяет выполнять операции над временем. Конструктор класса имеет следующий формат:
# time((hour][, minute][, second][, microsecond][, tzinfo])
# Все параметры не являются обязательными. Значения можно указывать через запятую в порядке следования параметров или
# присвоить значение названию параметра. В параметрах можно указать следующий диапазон значений:
# hour        - часы (число от 0 до 23);
# minute      - минуты (число от 0 до 59);
# second      - секунды (число от 0 до 59);
# microsecond - микросекунды (число от 0 до 999999);
# tzinfo      - зона (экземпляр класса tzinfo или значение None).
# fold        - порядковый номер отметки времени. Значение 0 (используется по умолчанию) обозначает первую отметку,
# значение 1 - вторую. Введено в Python 3.6 для тех случаев, когда в той или иной временной зоне практикуется перевод
# часов с зимнего на летнее время и обратно, в результате чего часы могут дважды в сутки показывать одинаковое время.
# Если значения выходят за диапазон, возбуждается исключение ValueError.
print(datetime.time(23, 12, 38, 375000))
t = datetime.time(hour=23, second=38, minute=12)
print(repr(t), str(t))
# print(datetime.time(25, 12, 38, 375000))
# Получить результат можно с помощью следующих атрибутов:
# hour        - часы (число от 0 до 23);
# minute      - минуты (число от 0 до 59);
# second      - секунды (число от 0 до 59);
# microsecond - микросекунды (число от 0 до 999999);
# tzinfo      - зона (экземпляр класса tzinfo или значение None).
# fold        - порядковый номер отметки времени (число 0 или 1). Поддержка этого атрибута появилась в Python 3.6.
t = datetime.time(23, 12, 38, 375000)
print(t.hour, t.minute, t.second, t.microsecond)
# Над экземплярами класса time нельзя выполнять арифметические операции. Можно только производить сравнения.
t1 = datetime.time(23, 12, 38, 375000)
t2 = datetime.time(12, 28, 17)
print(t1 < t2, t1 > t2, t1 <= t2, t1 >= t2)
print(t1 == t2, t1 != t2)
# Экземпляры класса time поддерживают следующие методы:
# replace([hour][, minute][, second][, microsecond][, tzinfo]) - возвращает время с обновленными значениями. Значения
# можно указывать через запятую в порядке следования параметров или присвоить значение названию параметра.
t = datetime.time(23, 12, 38, 375000)
print(t.replace(10, 52))     # Заменяем часы и минуты
print(t.replace(second=21))  # Заменяем только секунды
# isoformat() - возвращает время в формате ISO 8601:
t = datetime.time(23, 12, 38, 375000)
print(t.isoformat())
# strftime(<Строка формата>) - возвращает отформатированную строку. В строке формата можно указывать комбинации
# специальных символов, которые используются в функции strftime() из модуля time.
t = datetime.time(23, 12, 38, 375000)
print(t.strftime('%H:%M:%S'))
# Тип time поддерживает такие атрибуты класса:
# min        - минимально возможное значение времени;
# max        - максимально возможное значение времени;
# resolution - минимальное возможное различие между значениями времени.
# Значения этих атрибутов:
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)
# Примечание - Экземпляры класса time поддерживают также методы dst(), utcoffset() и tzname(). За подробной информацией
# по этим методам, а также по абстрактному классу tzinfo(), обращайтесь к документации по модулю datetime.


# 10.4.4 Класс datetime
print('Класс datetime:')
# Класс datetime из модуля datetime позволяет выполнять операции над комбинацией даты и времени. Конструктор класса
# имеет следующий формат:
# datetime(<Гoд>, <Месяц>, <День>[, hour][, minute][, second][, microsecond][, tzinfo])
# Первые три параметра являются обязательными. Остальные значения можно указывать через запятую в порядке следования
# параметров или присвоить значение названию параметра. В параметрах можно указать следующий диапазон значений:
# <Год>       - в виде числа, расположенного в диапазоне между значениями, хранящимися в константах MINYEAR(1) и
# МАХУЕАR(9999);
# <Месяц>     - число от 1 до 12 включительно;
# <День>      - число от 1 до количества дней в месяце;
# hour        - часы (число от 0 до 23);
# minute      - минуты (число от 0 до 59);
# second      - секунды (число от 0 до 59);
# microsecond - микросекунды (число от 0 до 999999);
# tzinfo      - зона (экземпляр класса tzinfo или значение None).
# fold        - порядковый номер отметки времени. Значение 0 (используется по умолчанию) обозначает первую отметку,
# значение 1 - вторую. Введено в Python 3.6 для тех случаев, когда в той или иной временной зоне практикуется перевод
# часов с зимнего на летнее время и обратно, в результате чего часы могут дважды в сутки показывать одинаковое время.
# Если значения выходят за диапазон, возбуждается исключение ValueError.
print(datetime.datetime(2017, 11, 21))
print(datetime.datetime(2017, 11, 21, hour=12, minute=55))
# print(datetime.datetime(2015, 32, 20))
d = datetime.datetime(2017, 11, 21, 17, 1, 5)
print(repr(d), str(d))
# Для создания экземпляра класса можно также воспользоваться следующими методами:
# today() - возвращает текущие дату и время:
print(datetime.datetime.today())
# now((<Зона>)) - возвращает текущие дату и время. Если параметр не задан, то метод аналогичен методу today().
print(datetime.datetime.now())
# utcnow() - возвращает текущее универсальное время (UTC):
print(datetime.datetime.utcnow())
# fromtimestamp(<Количество секунд>[, <Зона>]) - возвращает дату, соответствующую количеству секунд, прошедших с
# начала эпохи:
print(datetime.datetime.fromtimestamp(time()))
print(datetime.datetime.fromtimestamp(1421579037.0))
# utcfromtimestamp{<Количество секунд>) - возвращает дату, соответствующую количеству секунд, прошедших с начала эпохи,
# в универсальном времени (UTC).
print(datetime.datetime.utcfromtimestamp(time()))
print(datetime.datetime.utcfromtimestamp(1421579037.0))
# fromordinal(<Количество дней с 1-го года>) - возвращает дату, соответствующую количеству дней, прошедших с 1-го года.
# В качестве параметра указывается число от 1 до datetime.datetime.max.toordinal().
print(datetime.datetime.fromordinal(3652059))
print(datetime.datetime.fromordinal(1))
# combine(<Экземпляр класса date>, <Экземпляр класса time>) - создает экземпляр класса datetirne в соответствии со
# значениями экземпляров классов date и time:
d = datetime.date(2017, 11, 21)  # Экземпляр класса date
t = datetime.time(16, 7, 22)   # Экземпляр класса time
print(datetime.datetime.combine(d, t))
# strptime(<Строка с датой>, <Строка формата>) - разбирает строку, указанную в первом параметре, в соответствии со
# строкой формата. Если строка не соответствует формату, возбуждается исключение ValueError.
print(datetime.datetime.strptime('06.04.2015', '%d.%m.%Y'))
# print(datetime.datetime.strptime('O6.04.2015', '%d-%m-%Y'))
# Получить результат можно с помощью следующих атрибутов:
# year        - год (число в диапазоне от MINYEAR до МАХУЕАR);
# month       - месяц (число от 1 до 12);
# dау         - день (число от 1 до количества дней в месяце );
# hour        - часы (число от 0 до 23);
# minute      - минуты (число от 0 до 59);
# second      - секунды (число от о до 59);
# microsecond - микросекунды (число от 0 до 999999);
# tzinfo      - зона (экземпляр класса tzinfo или значение None).
# fold        - порядковый номер отметки времени (число 0 или 1). Поддержка этого атрибута появилась в Python 3.6.
d = datetime.datetime(2017, 11, 21, 17, 7, 22)
print(d.year, d.month, d.day)
print(d.hour, d.minute, d.second, d.microsecond)
# Над экземплярами класса datetime можно производить следующие операции:
# datetime2 = datetimel + timedelta - прибавляет к дате указанный период;
# datetime2 = datetimel - timedelta - вычитает из даты указанный период;
# timedelta = datetimel - datetime2 - возвращает разницу между датами;
# можно также сравнивать две даты с помощью операторов сравнения.
d1 = datetime.datetime(2017, 11, 21, 17, 7, 22)
d2 = datetime.datetime(2015, 4, 1, 12, 31, 4)
t = datetime.timedelta(days = 10, minutes = 10)
print(d1 + t)   # Прибавляем 10 дней и 10 минут
print(d1 - t)   # Вычитаем 10 дней и 10 минут
print(d1 - d2)  # Разница между датами
print(d1 < d2, d1 > d2, d1 <= d2, d1 >= d2)
print(d1 == d2, d1 != d2)
# Экземпляры класса datetime поддерживают следующие методы:
# date() - возвращает экземпляр класса date, хранящий дату:
d = datetime.datetime(2017, 11, 21, 17, 10, 54)
print(d.date())
# time() - возвращает экземпляр класса time, хранящий время:
d = datetime.datetime(2017, 11, 21, 17, 10, 54)
print(d.date())
# timetz() - возвращает экземпляр класса time, хранящий время. Метод учитывает параметр tzinfo;
# timestamp() - возвращает вещественное число, представляющее количество секунд, прошедшее с начала эпохи (обычно с 1
# января 1970 г.).
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.timestamp())
# replace([year][, month][, day][, hour][, minute][, second][, microsecond][, tzinfo]) - возвращает дату с обновленными
# значениями. Значения можно указывать через запятую в порядке следования параметров или присвоить значение названию
# параметра:
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.replace(2016, 12))
print(d.replace(hour=12, month=10))
# timetuple() - возвращает объект struct_time с датой и временем:
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.timetuple())
# utctimetuple() - возвращает объект struct_time с датой в универсальном времени (UTC):
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.utctimetuple())
# toordinal() - возвращает количество дней, прошедшее с 1-го года:
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.toordinal())
# weekday() - возвращает порядковый номер дня в неделе (0 - для понедельника, 6 - для воскресенья):
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.weekday())  # 1 - это вторник
# isoweekday() - возвращает порядковый номер дня в неделе (1- для понедельника, 7 - для воскресенья):
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.isoweekday())  # 2 - это вторник
# isocalendar() - возвращает кортеж из трех элементов (год, номер недели в году и порядковый номер дня в неделе):
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.isocalendar())
# isoformat([<Разделитель даты и времени>]) - возвращает дату в формате ISO 8601. Если разделитель не указан,
# используется буква т:
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.isoformat())  # Разделитель не указан
print(d.isoformat())  # Пробел в качестве разделителя
# ctime() - возвращает строку формата "%а %b %d %H:%M:%S %y":
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.ctime())
# strftime(<Строка формата>) - возвращает отформатированную строку. В строке формата можно указывать комбинации
# специальных символов, которые используются в функции strftime() из модуля time:
d = datetime.datetime(2017, 11, 21, 17, 56, 41)
print(d.strftime('%d.%m.%Y %H:%M:%S'))
# Поддерживаются также следующие атрибуты класса:
# min        - минимально возможные значения даты и времени;
# max        - максимально возможные значения даты и времени;
# resolution - минимальное возможное различие между значениями даты и времени.
# Значения этих атрибутов:
print(datetime.datetime.min)
print(datetime.datetime.max)
print(datetime.datetime.resolution)
# Примечание - Класс datetime также поддерживает методы astimezone(), dst(), utcoffset() и tzname(). За подробной
# информацией по этим методам, а также по абстрактному классу tzinfo обращайтесь к документации по модулю datetime.


# 10.5. Модуль calendar, вывод календаря
print('Модуль calendar, вывод календаря:')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


# 195


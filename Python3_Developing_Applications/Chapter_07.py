#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключаем модуль re

# ГЛАВА 7
# Регулярные выражения
# Регулярное выражение - это шаблон, применяемый для поиска совпадающих с ним фрагментов в строках. Регулярное выражение
# состоит как из обычных знаков, так и всевозможных специальных символов: метасимволов, квантификаторов и др.
# В Python использовать регулярные выражения позволяет модуль re, который необходимо предварительно подключить с помощью
# инструкции:
# import re


# 7.1. Синтаксис регулярных выражений
print('7.1. Синтаксис регулярных выражений')
# Создать откомпилированное и готовое к использованию регулярное выражение позволяет функция compile(). Формат ее
# вызова:
# re.compile(<Шаблон регулярного выражения>[, <Флаги>])
# Шаблон создаваемого регулярного выражения указывается в виде строки или последовательности байтов типа bytes или
# bytearray. Флаги управляют особенностями обработки регулярного выражения. Можно указать как один флаг, так и их
# комбинацию через оператор |. Все поддерживаемые флаги также объявлены в модуле re:
# - I или IGNORECASE - регистр символов не учитывается:
p = re.compile(r'[а-яе]+$', re.I | re.U)
print('Найдено' if p.search('АБВГДЕЕ') else 'Нет')
p = re.compile(r'^[а-яе]+$', re.U)
print('Найдено' if p.search('АБВГДЕЕ') else 'Нет')

# - M или MULTILINE - метасимвол ^ обозначает начало каждой подстроки в строке, в которой выполняется поиск (сразу после
# символа перевода строки \n, который используется для разбиения строки на подстроки), а символ $ - конец каждой
# подстроки (непосредственно перед символом перевода строки). Без этого флага метасимвол ^ обозначает начало самой
# строки, в которой выполняется поиск, а символ $ - ее конец. Примеры:
p = re.compile(r'^.*$', re.M)
print(p.findall('Python\nDjango\nSQLite'))
p = re.compile(r'^.*$')
print(p.findall('Python\nDjango\nSQLite'))

# - S или DOTALL - метасимвол 'точка' соответствует любому символу, включая перевод строки (\n). Без этого флага
# метасимвол 'точка' будет соответствовать любому символу, исключая перевод строки. Примеры:
p = re.compile(r'^.*$')
print(p.findall('Python\nDjango\nSQLite'))
p = re.compile(r'^.*$', re.S)
print(p.findall('Python\nDjango\nSQLite'))

# - X или VERВOSE - пробелы, символы перевода строки и комментарии, поставленные в шаблоне регулярного выражения,
# игнорируются. Этот флаг позволяет форматировать шаблоны регулярных выражений для наилучшей читабельности. Примеры:
p = re.compile(r'''^  # Привязка к началу строки
    [0-9]+            # Строка должна содержать одну цифру (или более)
    $                 # Привязка к концу строки
    ''', re.X | re.S)
print('Найдено' if p.search('1234567890') else 'Нет')
print('Найдено' if p.search('abcd123') else 'Нет')

# - A или ASCII - классы \w, \W, \b, \B, \d, \D, \s и \S соответствуют символам в кодировке ASCII. Без этого флага
# указанные классы соответствуют Unicode-символам.
# ПРИМЕЧАНИЕ - Флаги U и UNICODE, включающие режим соответствия классов \w, \W, \b, \B, \d, \D, \s и \S
# Unicode-символам, сохранены в Python лишь для совместимости с ранними версиями этого языка и никакого влияния на
# обработку регулярных выражений не оказывают.

# - L или LOCALE - учитываются настройки текущей локали. Флаг принимается во внимание, только если шаблон регулярного
# выражения задан в виде последовательности байтов типа bytes или bytearray.

# Шаблоны регулярных выражений удобно записывать в виде необрабатываемых строк (содержащих модификатор r):
# p = re.compile(r'^\w+S')
# В обычных строках все обратные слеши придется заменять специальными символами \\:
# p = re.compile(r'^\\w+S')
# В шаблоне регулярного выражения символы ., ^, $, *, +, ?, {, [, ], \, |, (и) являются специальными и обрабатываются
# особым образом. Если же эти символы должны трактоваться как есть, их следует предварить обратными слешами. Некоторые
# специальные символы теряют свое особое значение, если их разместить внутри квадратных скобок,- в этом случае
# экранировать их не нужно. Например, как уже было отмечено ранее, метасимвол 'точка' по умолчанию соответствует любому
# символу, кроме символа перевода строки. Если необходимо найти именно точку, то перед точкой нужно указать символ \ или
# разместить точку внутри квадратных скобок: [.] Продемонстрируем это на примере проверки правильности введенной даты
# test_00030.py.
# Метасимвол - это специальный символ, обозначающий привязку к началу или концу строки:
# - ^ - к началу строки или подстроки. Поведение зависит от флагов M (или MULTILINE) и S (или DOTALL);
# - $ - к концу строки или подстроки. Поведение зависит от флагов M (или MULTILINE) и S (или DOTALL);
# - \А - к началу строки (не зависит от флагов);
# - \Z - к концу строки (не зависит от флагов).
# Если указан флаг M (или MULTILINE), то при поиске в строке, состоящей из нескольких подстрок, разделенных символом \n,
# метасимвол ^ обозначает привязку к началу каждой такой подстроки (сразу после символа \n), а метасимвол $ - к концу
# каждой подстроки (непосредственно перед символом \n):
p = re.compile(r'^.+$')               # Точка не соответствует \n
print(p.findall('str1\nstr2\nstr3'))  # Ничего не найдено
p = re.compile(r'^.+$', re.S)         # Теперь точка соответствует \n
print(p.findall('str1\nstr2\nstr3'))  # Строка полностью соответствует
p = re.compile(r'^.+$', re.M)         # Многострочный режим
print(p.findall('str1\nstr2\nstr3'))  # Получили каждую подстроку
# Привязку к началу и концу строки следует использовать, если строка должна полностью соответствовать регулярному
# выражению. Например, для проверки, содержит ли строка число test_00031.py.
# Если убрать привязку к началу и концу строки, то любая строка, содержащая хотя бы одну цифру, будет распознана как
# 'Число' test_00032.py.
# Можно указать привязку только к началу или только к концу строки test_00033.py.
# Также поддерживаются два метасимвола, указывающие привязку к началу или концу слова:
# - \b - к началу слова (началом слова считается пробел или любой символ, не являющийся буквой, цифрой или знаком
# подчеркивания);
# - \B - к позиции, не являющейся началом слова.
# Рассмотрим несколько примеров:
p = re.compile(r'\bpython\b')
print('Найдено' if p.search('python') else 'Нет')
print('Найдено' if p.search('pythonware') else 'Нет')
p = re.compile(r'\Bth\B')
print('Найдено' if p.search('python') else 'Нет')
print('Найдено' if p.search('this') else 'Нет')
# В квадратных скобках [] можно перечислить символы, которые могут встречаться на этом месте в строке, или указать
# диапазон таких символов через дефис:
# - [09] - соответствует числу 0 или 9;
# - [0-9] - соответствует любому числу от 0 до 9;
# - [абв] - соответствует буквам 'а', 'б' и 'в';
# - [а-г] -соответствует буквам 'а', 'б', 'в' и 'r';
# - [а-яё] - соответствует любой букве от 'а' до 'я';
# - [АБВ] - соответствует буквам 'А', 'Б' и 'В';
# - [А-ЯЁ] - соответствует любой букве от 'А' до 'Я';
# - [а-яА-ЯёЁ] - соответствует любой русской букве в любом регистре;
# - [0-9а-яА-ЯёЁа-zА-Z] - любая цифра и любая буква независимо от регистра и языка.
# ВНИМАНИЕ! - Буква 'ё' не входит в диапазон [а-я], а буква 'Ё' - в диапазон [А-Я].
# Значение в скобках инвертируется, если после первой скобки вставить символ ^, что позволяет указать символы, которых
# не должно быть на этом месте в строке:
# - [^09] - не цифра 0 или 9;
# - [^0-9] - не цифра от 0 до 9;
# - [^а-яА-ЯёЁа-zА-Z] - не буква.
# Как вы уже знаете, точка теряет свое специальное значение, если ее заключить в квадратные скобки. Кроме того, внутри
# квадратных скобок могут встретиться символы, которые имеют специальное значение (например, ^ и -). Символ ^ теряет
# свое специальное значение, если он не расположен сразу после открывающей квадратной скобки. Чтобы отменить специальное
# значение символа -, его необходимо указать после всех символов, перед закрывающей квадратной скобкой или сразу после
# открывающей квадратной скобки. Все специальные символы можно сделать обычными, если перед ними указать символ \.
# Метасимвол | позволяет сделать выбор между альтернативными значениями. Выражение n | m соответствует одному из
# символов n или m, например:
p = re.compile(r'красн((ая)|(ое))')
print('Найдено' if p.search('красная') else 'Нет')
print('Найдено' if p.search('красное') else 'Нет')
print('Найдено' if p.search('красный') else 'Нет')

# Класс символов - это специальный символ, обозначающий какой-либо символ из определенного набора, символ с указанным
# Unicode-кодом или именем:
# - \d - любая цифра. При указании флага А (ASCII) эквивалентен [0-9];
# - \w - любая буква, цифра или символ подчеркивания. При указании флага А (ASCII) эквивалентен [a-zA-Z0-9_];
# - \s - любой пробельный символ. При указании флага А (ASCII) эквивалентен [\t\n\r\f\v];
# - \D - любой символ, не являющийся цифрой. При указании флага А (ASCII) эквивалентен [^0-9];
# - \W - любой символ, не являющийся буквой, цифрой или подчеркиванием. При указании флага А (ASCII) эквивалентен
# [^a-zA-Z0-9_];
# - \s - любой символ, не являющийся пробельным. При указании флага А (ASCII) эквивалентен [^\t\n\r\f\v].
# - \u<nnnn> - символ с 16-битным Unicode-кодом <nnnn>. Например, \u04За соответствует русской букве к;
# - \U<nnnnnnnn> - символ с 32-битным Unicode-кодом <nnnnnnnn>;
# - \N {<name>) (начиная с Python 3.8)- символ с Unicode-именем <name>. Например, \N {Registered Sign) соответствует
# знаку зарегистрированной торговой марки®.
# ПРИМЕЧАНИЕ - Упомянутые здесь классы трактуются довольно широко. Так, класс \d соответствует не только десятичным
# цифрам, но и другим цифрам из кодировки Unicode (например, дробям), класс \w включает буквы не только латиницы, но и
# других алфавитов, а класс \s охватывает также неразрывные пробелы. Поэтому, если необходимо явно указать набор
# требуемых символов, лучше привести эти символы внутри квадратных скобок, а не использовать классы.

# Квантификатор - специальный символ, задающий количество экземпляров указанного символа, которое должно присутствовать
# в строке:
# - {n} - строго n экземпляров. Например, шаблон r'^[0-9]{2}$' соответствует двум вхождениям любой цифры;
# - {n,} - n или более вхождений символа в строку. Например, шаблон r'^[0-9]{2, }$' соответствует двум и более
# экземплярам любой цифры;
# - {n,m} - не менее n и не более m экземплярам. Значения количества указываются через запятую без пробела. Например,
# шаблон r'^[О-9]{2,4}$' соответствует 2-4 экземплярам любой цифры;
# - * - ноль или больше экземпляров. Эквивалентно комбинации {0, };
# - + - один или больше экземпляров. Эквивалентно комбинации {1, };
# - ? - ноль или один экземпляр. Эквивалентно комбинации {0, 1}.
# Все квантификаторы являются «жадными». При поиске соответствия ищется самая длинная подстрока, соответствующая
# шаблону, и не учитываются более короткие соответствия. Для примера получим содержимое всех тегов <b> вместе с самими
# тегами:
s = '<b>Text1</b>Text2<b>Text3</b>'
p = re.compile(r'<b>.*</b>', re.S)
print(p.findall(s))
# Вместо желаемого результата мы получили всю строку. Чтобы ограничить «жадность», необходимо после квантификатора
# указать символ ?, например:
s = '<b>Text1</b>Text2<b>Text3</b>'
p = re.compile(r'<b>.*?</b>', re.S)
print(p.findall(s))
# Этот код вывел то, что мы искали. Если необходимо получить содержимое без тегов, то нужный фрагмент внутри шаблона
# следует разместить внутри круглых скобок:
s = '<b>Text1</b>Text2<b>Text3</b>'
p = re.compile(r'<b>(.*?)</b>', re.S)
print(p.findall(s))
# Круглые скобки используются для групп внутри регулярных выражений. Фрагменты, соответствующие группам, будут
# запоминаться и станут доступны в результатах поиска (это называется захватом фрагмента). Чтобы избежать захвата
# фрагмента, после открывающей круглой скобки в группе следует разместить символы ?: (вопросительный знак и двоеточие):
s = 'test text'
p = re.compile(r'([a-z]+((st)|(xt)))', re.S)
print(p.findall(s))
p = re.compile(r'([a-z]+(?:(?:st)|(?:xt)))', re.S)
print(p.findall(s))
# В первом примере мы получили список с двумя элементами. Каждый элемент списка является кортежем, содержащим четыре
# элемента. Все эти элементы соответствуют группам, заключенным в шаблоне в круглые скобки: первый элемент соответствует
# первому фрагменту, второй - второму и т.д. Три последних элемента кортежа являются лишними. Чтобы они не включались в
# результаты поиска, во втором примере мы добавили символы ?: после каждой открывающей круглой скобки. В результате
# список состоит только из фрагментов, полностью соответствующих регулярному выражению.
# К найденному фрагменту можно обратиться с помощью механизма обратных ссылок. Для этого в шаблоне регулярного выражения
# следует указать обратный слеш и порядковый номер нужной группы (начиная с 1) (например, \1). Для примера получим текст
# между одинаковыми парными тегами:
s = '<b>Text1</b>Text2<I>Text3</I><b>Text4</b>'
p = re.compile(r'<([a-z]+)>(.*?)</\1>', re.S | re.I)
print(p.findall(s))
# Группам можно дать имена, создав тем самым именованные группы. Для этого после открывающей круглой скобки в группе
# следует указать комбинацию символов ?P<Имя группы>.
# Для примера разберем e-mail на составные части:
email = 'test@mail.ru'
p = re.compile(r'''(?P<name>[a-z0-9_.-]+)  # Название ящика
    @                                      # Символ '@'
    (?P<host>(?:[a-z0-9-]+\.)+[a-z]{2,6})  # Домен
    ''', re.I | re.VERBOSE)
r = p.search(email)
print(r.group('name'))                     # Название ящика
print(r.group('host'))                     # Домен
# Чтобы внутри шаблона обратиться к фрагментам из именованных групп, используется следующий синтаксис: (?P=name).
# Для примера получим текст между одинаковыми парными тегами:
s = '<b>Text1</b>Text2<I>Text3</I>'
p = re.compile(r'<(?P<tag>[a-z]+)>(.*?)</(?P=tag)>', re.S | re.I)
print(p.findall(s))

# Кроме того, внутри круглых скобок могут быть расположены следующие конструкции:
# - (?#<Комментарий>) - комментарий. Текст внутри круглых скобок игнорируется;
# - (?=...) - положительный просмотр вперед. Выведем все слова, после которых расположена запятая:
s = 'text1, text2, text3 text4'
p = re.compile(r'\w+(?=[,])', re.S | re.I)
print(p.findall(s))
# - (?!...) - отрицательный просмотр вперед. Выведем все слова, после которых нет запятой:
s = 'text1, text2, text3 text4'
p = re.compile(r'[a-z]+[0-9](?![,])', re.S | re.I)
print(p.findall(s))
# - (?<=...) - положительный просмотр назад. Выведем все слова, перед которыми расположена запятая с пробелом:
s = 'text1, text2, text3 text4'
p = re.compile(r'(?<=[,][ ])[a-z]+[0-9]', re.S | re.I)
print(p.findall(s))
# - (?<!...) - отрицательный просмотр назад. Выведем все слова, перед которыми расположен пробел, но перед пробелом нет
# запятой:
s = 'text1, text2, text3 text4'
p = re.compile(r'(?<![,]) ([a-z]+[0-9])', re.S | re.I)
print(p.findall(s))
# - (?(<Номер>|<Имя>)<Шаблон 1>|<Шаблон 2>) - если группа с заданным номером или именем найдена, то должно выполняться
# условие из параметра <Шаблон 1>, в противном случае - условие из параметра <Шаблон 2>. Выведем все слова, которые
# расположены внутри апострофов. Если перед словом нет апострофа, то в конце слова должна быть запятая:
s = "text1 'text2' 'text3 text4, text5"
p = re.compile(r"(')?([a-z]+[0-9])(?(1)'|,)", re.S | re.I)
print(p.findall(s))
# - (?aiLmsux) - задает флаги у регулярного выражения. Буквы а, i, L, m, s, u, x имеют такое же назначение, что и
# одноименные флаги в функции compile( ).
# Перед буквами i, m, s, х можно указать дефис - в этом случае соответствующий флаг, заданный ранее при создании
# регулярного выражения или в предыдущей подобной языковой конструкции, перестанет действовать.
# Предположим, что необходимо получить все слова, расположенные после дефиса, причем перед дефисом и после слов должны
# следовать пробельные символы:
s = '-word1 -word2 -word3 -word4 -word5'
print(re.findall(r'\s\-([a-z0-9]+)\s', s, re.S | re.I))
# Мы получили только два слова вместо пяти. Первое и последнее слова не попали в результат, поскольку расположены в
# начале и в конце строки. Чтобы эти слова попали в результат, необходимо добавить альтернативный выбор (^|\s) - для
# начала строки и (\s|$) - для конца строки. Чтобы найденные выражения внутри круглых скобок не попали в результат,
# следует добавить символы ?: после открывающей скобки, например:
print(re.findall(r'(?:^|\s)\-([a-z0-9]+)(?:\s|$)', s, re.S | re.I))
# В этом случае в результат не попали слова word2 и word4. Чтобы понять причину, рассмотрим поиск по шагам. Первое слово
# успешно попадает в результат, т. к. перед дефисом расположено начало строки и после слова есть пробел. После поиска
# указатель перемещается, и строка для дальнейшего поиска примет следующий вид:
# '-word1 <Указатель>-word2 -word3 -word4 -word5'
# Обратите внимание, что перед фрагментом -word2 больше нет пробела и дефис не расположен в начале строки. Поэтому
# следующим совпадением окажется слово word3, и указатель снова будет перемещен:
# "-word1 -word2 -word3 <Указатель>-word4 -word5"
# Опять перед фрагментом -word4 нет пробела, и дефис не расположен в начале строки. Поэтому следующим совпадением
# окажется слово word5, и поиск будет завершен. Таким образом, слова word2 и word4 не попадают в результат, поскольку
# пробел до фрагмента уже был использован в предыдущем поиске. Чтобы этого избежать, следует воспользоваться
# положительным просмотром вперед (?=...), например:
print(re.findall(r'(?:^|\s)\-([a-z0-9]+)(?=\s|$)', s, re.S | re.I))
# Теперь все слова успешно попали в список совпадений.


# 7.2. Поиск первого совпадения с шаблоном
print('7.2. Поиск первого совпадения с шаблоном')
# Для поиска первого совпадения с шаблоном предназначены следующие методы, поддерживаемые объектом регулярного
# выражения:
# - match() - ищет фрагмент, соответствующий текущему регулярному выражению, в начале заданной строки. Формат метода:
# match(<Строка>[, <Начальная позиция>[, <Конечная позиция>]])
# Если соответствие найдено, возвращается объект класса Match, в противном случае - значение None:
p = re.compile(r'[0-9]+')
print('Найдено' if p.match('str123') else 'Нет')
print('Найдено' if p.match('str123', 3) else 'Нет')
print('Найдено' if p.match('123str') else 'Нет')
# Вместо метода match() можно воспользоваться функцией match(). Формат функции :
# re.match(<Шаблон>, <Строка>[, <Флаги>])
# В параметре <Шаблон> указывается строка с регулярным выражением или скомпилированное регулярное выражение. В параметре
# <Флаги> можно указать флаги, используемые в функции compile(). Если соответствие найдено, то возвращается объект
# match, в противном случае - значение None:
p = r'[0-9]+'
print('Найдено' if re.match(p, 'str123') else 'Нет')
print('Найдено' if re.match(p, '123str') else 'Нет')
p = re.compile(r'[0-9]+')
print('Найдено' if re.match(p, '123str') else 'Нет')

# - search() - ищет фрагмент, соответствующий текущему регулярному выражению, во всей заданной строке. Формат метода:
# search(<Строка>[, <Начальная позиция>[, <Конечная позиция>]])
# Если соответствие найдено, возвращается объект match, в противном случае - значение None:
p = re.compile(r'[0-9]+')
print('Найдено' if p.search('str123') else 'Нет')
print('Найдено' if p.search('123str') else 'Нет')
print('Найдено' if p.search('123str', 3) else 'Нет')
# Вместо метода search() можно воспользоваться функцией search() . Формат функции:
# rе.search(<Шаблон>, <Строка>[, <Флаги>])
# В параметре <Шаблон> указывается строка с регулярным выражением или скомпилированное регулярное выражение. В параметре
# <Флаги> можно указать флаги, используемые в функции compile(). Если соответствие найдено, возвращается объект match, в
# противном случае - значение None. Примеры:
p = r'[0-9]+'
print('Найдено' if re.search(p, 'str123') else 'Нет')
p = re.compile(r'[0-9]+')
print('Найдено' if re.search(p, 'str123') else 'Нет')

# - fullmatch() - проверяет, соответствует ли заданная строка текущему регулярному выражению целиком. Формат метода:
# fullmatch(<Строка>[, <Начальная позиция>[, <Конечная позиция>]])
# Если соответствие найдено, то возвращается объект match, в противном случае - значение None:
p = re.compile('[Pp]ython')
print('Найдено' if p.fullmatch('Python') else 'Нет')
print('Найдено' if p.fullmatch('py') else 'Нет')
print('Найдено' if p.fullmatch('PythonWare') else 'Нет')
print('Найдено' if p.fullmatch('PythonWare', 0, 6) else 'Нет')
# Вместо метода fullmatch() можно воспользоваться функцией fullmatch(). Формат функции:
# re.fullmatch(<Шаблон>, <Строка>[, <Флаги>])
# В параметре <Шаблон> указывается строка с регулярным выражением или скомпилированное регулярное выражение. В параметре
# <Флаги> можно указать флаги, используемые в функции compile(). Если строка полностью совпадает с шаблоном,
# возвращается объект Match, в противном случае - значение None. Примеры:
p = re.compile('[Pp]ython')
print('Найдено' if re.fullmatch(p, 'Python') else 'Нет')
print('Найдено' if re.fullmatch(p, 'py') else 'Нет')

# В качестве примера переделаем программу суммирования произвольного количества целых чисел, введенных пользователем, из
# test_00025.py таким образом, чтобы при вводе строки вместо числа программа не завершалась с фатальной ошибкой.
# Предусмотрим также возможность ввода отрицательных целых чисел test_00034.py.

# Объект класса Match, возвращаемый методами (функциями) match(), search() и fullmatch(), имеет следующие атрибуты и
# методы:
# - re - ссылка на сам шаблон регулярного выражения, поддерживающий следующие атрибуты:
#  - groups - количество групп в шаблоне;
#  - groupindex - словарь с именами групп и их номерами;
#  - pattern - исходная строка с шаблоном регулярного выражения;
#  - flags - комбинация флагов, заданных при создании регулярного выражения в функции compile(), и флагов, указанных в
#  самом регулярном выражении, в конструкции (?aiLmsux);

# - string - значение параметра <Строка> в методах (функциях) match(), search() и fullmatch();

# - pos - значение параметра <Начальная позиция> в методах match(), search() и fullmatch();

# - endpos - значение параметра <Конечная позиция> в методах match(), search() и fullmatch();

# - lastindex - номер последней группы или значение None, если поиск завершился неудачей;

# - lastgroup - имя последней группы или значение None, если эта группа не имеет имени или поиск завершился неудачей:
p = re.compile(r'(?P<num>[0-9]+)(?P<str>[a-z]+)')
m = p.search('123456string 67890text')
print(m)
print(m.re.groups, m.re.groupindex)
print(m.re.groups, m.re.groupindex['num'])
print(p.groups, p.groupindex)
print(p.groups, p.groupindex['str'])
print(m.string)
print(m.lastindex, m.lastgroup)
print(m.pos, m.endpos)

# - group([<Номер 1> 1 <Имя 1>[, . . ., <Номер n> 1 <Имя n>]]) - возвращает фрагменты, соответствующие группам. Если
# параметры не заданы или указано значение 0, возвращается фрагмент, полностью соответствующий шаблону. Если указан
# номер или имя группы, возвращается фрагмент, совпадающий с этой группой. Можно указать несколько номеров или имен
# групп - в этом случае возвращается кортеж, содержащий фрагменты, что соответствует группам. Если нет группы с
# указанным номером или именем, то возбуждается исключение IndexError. Примеры:
p = re.compile(r'(?P<num>[0-9]+)(?P<str>[a-z]+)')
m = p.search('123456string 67890text')
print(m.group(), m.group(0))                 # Полное соответствие шаблону
print(m.group(1), m.group(2))                # Обращение по индексу
print(m.group('num'), m.group('str'))        # Обращение по имени
print(m.group(1, 2), m.group('num', 'str'))  # Несколько параметров

# - groupdict([<Значение по умолчанию>]) - возвращает словарь, содержащий фрагменты из именованных групп. Можно указать
# значение по умолчанию, которое будет выводиться вместо None для групп, не имеющих совпадений. Примеры:
p = re.compile(r'(?P<num>[0-9]+)(?P<str>[a-z]+)')
m = p.search('123456string')
print(m.groupdict())
print(m.groupdict(''))

# - groups([<Значение по умолчанию>]) - возвращает кортеж, содержащий фрагменты из всех групп. Можно указать значение по
# умолчанию, которое будет выводиться вместо None для групп, не имеющих совпадений. Примеры:
p = re.compile(r'(?P<num>[0-9]+)(?P<str>[a-z]+)')
m = p.search('123456string')
print(m.groups())
print(m.groups(''))

# - start([<Номер или имя группы>]) - возвращает индекс начала фрагмента, соответствующего заданной группе. Если
# параметр не указан, возвращает индекс начала полного соответствия с шаблоном. Если соответствия нет, возвращается
# значение -1;

# - end([<Номер или имя группы>]) - возвращает индекс конца фрагмента, соответствующего заданной группе. Если параметр
# не указан, возвращает индекс конца полного соответствия с шаблоном. Если соответствия нет, возвращается значение -1;

# - span([<Номер или имя группы>]) - возвращает кортеж, содержащий начальный и конечный индексы фрагмента, который
# соответствует заданной группе. Если параметр не указан, возвращает индексы начала и конца полного соответствия с
# шаблоном. Если соответствия нет, возвращается значение (-1, -1). Примеры:
p = re.compile(r'(?P<num>[0-9]+)(?P<str>[a-z]+)')
s = 'str123456str'
m = p.search(s)
print(m.start(), m.end(), m.span())
print(m.start(1), m.end(1), m.start('num'), m.end('num'))
print(m.start(2), m.end(2), m.start('str'), m.end('str'))
print(m.span(1), m.span('num'), m.span(2), m.span('str'))
print(s[m.start(1):m.end(1)], s[m.start(2):m.end(2)])

# - expand(<Шаблон>) - производит замену в строке согласно заданному шаблону. Внутри последнего можно использовать
# обратные ссылки: \<Номер группы>, \g<Номер группы> и \g<Имя группы>. Содержимое не совпавших групп будет заменено на
# пустые строки. Для примера поменяем два тега местами:
p = re.compile(r'<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>')
m = p.search('<br><hr>')
print(m.expand(r'<\2><\1>'))              # \<Номер>
print(m.expand(r'<\g<2>><\g<1>>'))        # \g<Номер>
print(m.expand(r'<\g<tag2>><\g<tag1>>'))  # \g<Имя>
# В качестве примера использования метода search() проверим на соответствие шаблону введенный пользователем адрес
# электронной почты test_00035.py.
# Результат выполнения (введенное пользователем значение выделено полужирным шрифтом):
# Введите e-mail: user@mail.ru
# E-mail user@mail.ru соответствует шаблону
# ящик: user домен: mail.ru


# 7.3. Поиск всех совпадений с шаблоном
print('7.3. Поиск всех совпадений с шаблоном')
# Для поиска всех совпадений с шаблоном предназначены следующие методы, поддерживаемые объектом регулярного выражения:
# - findall() - ищет в заданной строке все совпадения с текущим регулярным выражением. Формат метода:
# findall(<Строка>[, <Начальная позиция>[, <Конечная позиция>]])
# Если соответствия найдены, возвращается список с фрагментами, в противном случае - пустой список. Если внутри шаблона
# есть более одной группы, то каждый элемент списка будет кортежем, а не строкой. Примеры:
p = re.compile(r'[0-9]+')
print(p.findall('2018, 2019, 2020, 2021, 2022'))
p = re.compile(r'[a-z]+')
print(p.findall('2018, 2019, 2020, 2021, 2022'))
p = re.compile(r'(([0-9]{3})-([0-9]{2})-([0-9]{2}))')
print(p.findall('322-77-20, 528-22-98'))
# Вместо метода findall() можно воспользоваться функцией findall(). Формат функции:
# re.findall(<Шаблон>, <Строка>[, <Флаги>])
# В параметре <Шаблон> указывается строка с регулярным выражением или скомпилированное регулярное выражение. В параметре
# <Флаги> можно указать флаги, используемые в функции compile(). Примеры:
print(re.findall(r'[0-9]+', '1 2 3 4 5 6'))
p = re.compile(r'[0-9]+')
print(re.findall(p, '1 2 3 4 5 6'))

# - finditer() - аналогичен методу findall(), но возвращает итератор, который на каждой итерации выдает объект класса
# Match. Формат метода:
# finditer(<Строка>[, <Начальная позиция>[, <Конечная позиция>]])
# Пример:
p = re.compile(r'[0-9]+')
for m in p.finditer('2018, 2019, 2020, 2021, 2022'):
    print(m.group(0), 'start:', m.start(), 'end:', m.end())
# Вместо метода finditer() можно воспользоваться функцией finditer(). Ее формат:
# re.finditer(<Шаблон>, <Строка>[, <Флаги>])
# В параметре <Шаблон> указывается строка с регулярным выражением или скомпилированное регулярное выражение. В параметре
# <Флаги> можно указать флаги, используемые в функции compile() . Получим содержимое между тегами:
p = re.compile(r'<b>(.+?)</b>', re.I | re.S)
s = '<b>Text1</b>Text2<b>Text3</b>'
for m in re.finditer(p, s):
    print(m.group(1))


# 7.4. Замена в строке
print('7.4. Замена в строке')
# Метод sub(), поддерживаемый регулярным выражением, ищет в указанной строке все совпадения с текущим регулярным
# выражением и заменяет их фрагментом, соответствующим заданному регулярному выражению. Содержимое не совпавших групп
# будет заменено на пустые строки. Если совпадения не найдены, возвращается исходная строка. Метод имеет следующий
# формат:
# sub(<Регулярное выражение, задающее замену>, <Строка>[, <Максимальное количество замен>])
# Внутри регулярного выражения, задающего замену, можно использовать обратные ссылки \<Номер группы>, \g<Номер группы> и
# \g<Имя группы>. Для примера поменяем два тега местами:
p = re.compile(r'<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>')
print(p.sub(r'<\2><\1>', 'Теги <br><hr>'))              # \<Номер>
print(p.sub(r'<\g<2>><\g<1>>', 'Теги <br><hr>'))        # \g<Номер>
print(p.sub(r'<\g<tag2>><\g<tag1>>', 'Теги <br><hr>'))  # \g<Имя>
# В первом параметре можно указать ссылку на функцию. В эту функцию будет передаваться объект класса Match,
# соответствующий найденному фрагменту. Результат, возвращаемый этой функцией, послужит заменяющим фрагментом. Для
# примера найдем все числа в строке и прибавим к ним 10 test_00036.py.
# Результат выполнения:
# 2029, 2030, 2031, 2032
# 2029, 2030, 2021, 2022
# Вместо метода sub() можно воспользоваться функцией sub() . Формат функции:
# re.sub(<Шаблон>, <Регулярное выражение, задающее замену>, <Строка>[, <Максимальное количество замен>[, flags=0]])
# В качестве параметров <шаблон> и <Регулярное выражение, задающее замену> можно указать строки с регулярными
# выражениями или скомпилированные регулярные выражения. В параметре flags можно указать флаги, используемые в функции
# compile(). Для примера поменяем два тега местами, а также изменим регистр букв test_00037.py.
# Результат выполнения:
# <HR><BR>
# Метод subn() аналогичен методу sub(), но возвращает кортеж из двух элементов: измененной строки и количества
# произведенных замен. Метод имеет следующий формат:
# subn(<Регулярное выражение, задающее замену>, <Строка>[, <Максимальное количество замен>])
# Заменим все числа в строке на 0:
p = re.compile(r'[0-9]+')
print(p.subn('0', '2019, 2020, 2021, 2022'))
# Вместо метода subn() можно воспользоваться функцией subn(). Формат функции:
# rе.subn(<Шаблон>, <Регулярное выражение, задающее замену>, <Строка>[, <Максимальное количество замен>[, flags=0]])
# В качестве параметров <Шаблон> и <Регулярное выражение, задающее замену> можно указать строки с регулярными
# выражениями или скомпилированные регулярные выражения. В параметре flags можно указать флаги, используемые в функции
# compile(). Примеры:
p = r'201[89]'
print(re.subn(p, '2022', '2019, 2020, 2021, 2018'))
# Для выполнения замен также можно использовать метод expand(<Шаблон>), поддерживаемый объектом Match. Внутри указанного
# шаблона можно использовать обратные ссылки:
# \<Номер группы>, \g<Номер группы> и \g<Имя группы>:
p = re.compile(r'<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>')
m = p.search('<br><hr>')
print(m.expand(r'<\2><\1>'))              # \<Номер>
print(m.expand(r'<\g<2>><\g<1>>'))        # \g<Номер>
print(m.expand(r'<\g<tag2>><\g<tag1>>'))  # \g<Имя>


# 7.5. Прочие функции и методы
print('7.5. Прочие функции и методы')
# Метод split(<Строка>[, <Лимит>]) разбивает заданную строку по шаблону текущего регулярного выражения и возвращает
# список подстрок. Если во втором параметре задано число, то в списке окажется указанное количество подстрок. Если
# подстрок больше указанного количества, то список будет содержать еще один элемент - с остатком строки. Примеры:
p = re.compile(r'[\s,.]+')
print(p.split('word1, word2\nword3\r\nword4.word5'))
print(p.split('word1, word2\nword3\r\nword4.word5', 2))
# Если разделитель в строке не найден, список будет состоять только из одного элемента, содержащего исходную строку:
p = re.compile(r'[0-9]+')
print(p.split('word, word\nword'))
# Вместо метода split() можно воспользоваться функцией split(). Формат функции:
# re.split(<Шаблон>, <Строка>[, <Лимит>[, flags=O]])
# В качестве параметра <Шаблон> можно указать строку с регулярным выражением или скомпилированное регулярное выражение.
# В параметре flags можно указать флаги, используемые в функции compile(). Примеры:
p = re.compile(r'[\s,.]+')
print(re.split(p, 'word1, word2\nword3'))
print(re.split(r'[\s,.]+', 'word1, word2\nword3'))
# Функция escape (<Строка>) экранирует все специальные символы в заданной строке, после чего ее можно безопасно
# использовать в составе регулярного выражения:
print(re.escape(r'[]().*'))
# Функция purge() очищает кеш, в котором хранятся промежуточные данные, используемые при выполнении регулярных
# выражений. Ее рекомендуется вызывать после обработки большого количества регулярных выражений. Результата эта функция
# не возвращает. Пример:
re.purge()

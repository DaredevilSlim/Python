#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import builtins
from sys import stdout  # Подключаем из модуля sys содержащийся в нем объект stdout

# ГЛАВА 1
print('ГЛАВА 1')
# 1.4. Принципы написания Python-программ
print('1.4. Принципы написания Python-программ')
# Программа, написанная на Python, представляет собой обычный текстовый файл с расширением ру (будет исполнен обычным
# интерпретатором python.exe) или pyw (будет исполнен 'оконным' интерпретатором pythonw.exe).
# Для написания Python-программ, как уже ранее отмечалось, можно использовать, помимо IDLE, любой подходящий текстовый
# редактор: стандартный Блокнот, Notepad++ (https://notepad-plus-plus.org/), Visual Studio Code
# (https://code.visualstudio.com/) и др.
# Также существует ряд специализированных текстовых редакторов, предназначенных именно для Python-программистов, в
# частности PyCharm' (https://www.jetbrains.com/ru-ru/pycharm/).
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
# Если загрузить файл Python-программы по протоколу FTP в бинарном режиме, то символ \r вызовет фатальную ошибку. По
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
# - Короткие инструкции можно записать в одной строке, разделив их символами точки с запятой ';':
x = 15 + 20 + 30; print(x)
# После точки с запятой не возбраняется ставить пробел - для улучшения читаемости кода.
# - Блоки (наборы из произвольного количества инструкций, входящие в состав более сложных инструкций) формируются
# отступами слева. Такие отступы должны формироваться исключительно пробелами и быть одинаковой длины (т. е. содержать
# одинаковое количество пробелов). Символы табуляции в отступах не допускаются и при выполнении программы вызывают
# возникновение ошибки.
# Код программы, выводящей последовательно числа от 1 до 10, которые разделяются тремя дефисами (test_00004.py).
# Первая строка содержит сложную инструкцию - цикл, который выполняется десять раз. При каждом исполнении он заносит в
# переменную i очередное число в диапазоне от 1 до 10 и выполняет блок, входящий в его состав. Этот блок состоит из
# двух инструкций, записанных во второй и третьих строках: первая инструкция выводит в консоли число из переменной i, а
# вторая - строку из трех дефисов. Обе инструкции, входящие в блок, имеют одинаковый отступ слева, содержащий 4 пробела.
# Числа, перебираемые циклом (и, соответственно, количество выполнений, или итераций, цикла), указываются в функции
# range() (первая инструкция в test_00004.py). Первый параметр задает начальное число перебираемого диапазона, второй -
# конечное число плюс 1.
# При вводе инструкции, содержащей блок, в интерпретаторе, который работает в интерактивном режиме, интерпретатор
# предваряет выражения, входящие в блок, приглашением в виде трех точек (...) и сам вставляет отступы. Чтобы завершить
# ввод блока, следует, занеся последнее входящее в него выражение, нажать клавишу <Enter> (при этом в набранном коде
# появится пустая строка с приглашением в виде трех точек).
# - Если блок содержит одну короткую инструкцию, и сам блок, и сложную инструкцию, в состав которой он входит, можно
# записать в одну строку. При этом интерпретатор посчитает, что ввод блока продолжится после нажатия клавиши <Enter>, и
# выведет приглашение в виде трех точек. Чтобы завершить ввод инструкции, следует снова нажать <Enter>. Пример
# программы, выводящей в консоли числа от 1 до 10:


# 1.4.1. Комментарии и строки документирования
print('1.4.1. Комментарии и строки документирования')
# Комментарий - это произвольное пояснение, вставленное в код программы, предназначенное исключительно программисту и
# полностью игнорируемое интерпретатором. Внутри комментария может располагаться любой текст.
# Комментарий в языке Python начинается с символа # и заканчивается концом строки:
# Выводим числа от 1 до 10
for i in range(1, 11):
    print(i)
# Комментарий может располагаться после собственно инструкции:
print('Bce, числа закончились')  # Сообщаем об окончании чисел
# Если символ # разместить перед инструкцией, то она не будет выполнена (закомментированная инструкция):
# print('Привет, мир!') Эта инструкция выполнена не будет
# Если требуется разместить комментарий из нескольких строк, перед каждой из них придется ставить символ #:
# Это наша первая программа!
# Она выводит числа от 1 до 10
# Да, не впечатляет, но для начала неплохо...
for i in range(1, 11):
    print(i)
# Строки документирования Python обычно применяются для написания инструкций к программам и модулям. Однако их можно
# использовать и для комментирования кода.
# Строка документирования заключается в утроенные кавычки или апострофы:
"""
Это наша первая программа!
Она выводит числа от 1 до 10
Да, не впечатляет, но для начала неплохо...
"""
for i in range(1, 11):
    print(i)


# 1.4.2. Кодировки, поддерживаемые Python
print('1.4.2. Кодировки, поддерживаемые Python')
# Код Python-программы, написанный в IDLE, по умолчанию сохраняется в кодировке UTF-8 без BOM.
# ВОМ (Byte Order Mark) - метка порядка байтов. Указывает порядок, в котором записываются байты, кодирующие символы
# в UTF-8.
# Если программу следует сохранить в какой-либо другой кодировке (что может пригодиться, например, при переписывании
# старого Python-кода), в первой строке ее кода следует указать кодировку с помощью инструкции формата:
# -*- coding: <Обозначение кодировки>-*-
# Например, кодировка Windows-1251 указывается инструкцией:
# -*- coding: ср1251 -*-
# Встретив такую инструкцию в коде программы, IDLE при сохранении файла самостоятельно переведет программу в кодировку с
# заданным обозначением. При использовании других редакторов следует перевести программу в указанную кодировку вручную.
# Получить полный список поддерживаемых Python кодировок и их обозначения позволяет программа (test_00005.py).


# 1.4.3. Подготовка Python-программ для выполнения в UNIX
print('1.4.3. Подготовка Python-программ для выполнения в UNIX')
# Если программа предназначена для исполнения в операционных системах семейства UNIX, в первой строке кода программы
# необходимо указать путь к интерпретатору Python:
# #!/usr/bin/python
# В некоторых UNIХ-системах путь к интерпретатору выглядит по-другому:
# #!/usr/local/bin/python
# Иногда можно не указывать точный путь к интерпретатору, а передать название языка программе env:
# #!/usr/bin/env python
# В этом случае программа env произведет поиск интерпретатора Python в соответствии с настройками путей поиска.
# Если программа, исполняемая в UNIX, сохранена в кодировке, отличной от UTF-8, обозначение кодировки указывается во
# второй строке ее кода:
# #!/usr/bin/python
# # -*- coding: ср1251 -*-
# Также следует разрешить выполнять Python-программу, указав у ее файла права 755 (-rwxrxr-x).


# 1.6. Вывод данных
print('1.6. Вывод данных')
# Вывести заданные значения можно с помощью функции print():
# print([<Значения через запятую>][, sep=' '][, end='\n'][, file=sys.stdout][, flush=False])
# Указанные значения при необходимости преобразуются в строки и посылаются в стандартный поток вывода stdout. С помощью
# параметра file можно перенаправить вывод в другое место - например, в файл. При этом, если параметр flush имеет
# значение False, выводимые значения будут записаны в файл принудительно.
# Если выполняется вывод одного значения, автоматически добавляется символ перевода строки:
print('Строка 1')
print('Строка 2')
# Результат:
# Строка 1
# Строка 2
# Можно вывести несколько значений в одну строку, указав их в вызове функции print() отдельными параметрами,
# разделенными запятыми:
print('Строка 1', 'Строка 2')
# Результат:
# Строка 1 Строка 2
# Как видно из примера, между выводимыми значениями автоматически вставляется пробел. С помощью параметра sep можно
# указать другой разделяющий символ. Например, выведем строки без пробела между ними, указав в качестве разделителя
# пустую строку:
print('Строка 1', 'Строка 2', sep='')
# Результат:
# Строка 1Строка 2
# Ряд функций, встроенных в Python, поддерживают так называемые именованные параметры. В число таких параметров и входит
# sep. Обратим внимание, как задается его значение в приведенном примере. После вывода нескольких значений в одном
# вызове функции print() в конце добавляется символ перевода строки. Если необходимо произвести дальнейший вывод на той
# же строке, то в именованном параметре end следует указать другой символ:
print('Строка 1', 'Строка 2', end=' ')
print('Строка 3')
# Выведет: Строка 1 Строка 2 Строка 3
# Вызов функции print() без параметров выводит пустую строку:
for n in range(1, 5):
    print(n, end=' ')
print()
print('Это текст на новой строке')
# Результат выполнения:
# 1 2 3 4
# Это текст на новой строке
# Здесь мы использовали цикл, выполняющийся четыре раза. На каждой итерации он присваивает переменной n число от 1 до 4
# и выполняет блок, содержащий вызов функции print(), которая выводит число из переменной n. Не забываем вставить в
# выражение, входящее в блок, отступ слева.
# Как только цикл выполнится четыре раза, будут исполнены два следующих за ним выражения. В них отступы слева указывать
# не следует, поскольку эти выражения не должны входить в состав блока. Первое выражение выведет пустую строку, второе -
# надпись 'Это текст на новой строке'.
# Если необходимо вывести большой блок текста, его следует разместить между утроенными кавычками или утроенными
# апострофами. В этом случае текс, сохраняет свое форматирование:
print('''Строка 1
Строка 2
Строка 3''')
# В результате выполнения этого примера мы получим три строки:
# Строка 1
# Строка 2
# Строка 3
# Вместо функции print() можно использовать метод write() объекта stdout из модуля sys:
stdout.write('Строка\n')
# Модуль - это просто файл с Python-кодом. Однако модуль sys поставляется в составе Python и входит в стандартную
# библиотеку (набор модулей, содержащих полезные функции, объекты и др.) этого языка. Подключив этот модуль, мы можем
# использовать созданные в нем функции и объекты. В первой строке с помощью оператора import подключаем модуль sys, в
# котором объявлен объект stdout. Далее с помощью метода write() этого объекта выводим строку. Следует заметить, что
# метод не вставляет символ перевода строки, поэтому при необходимости следует добавить его самим с помощью символа \n:
stdout.write('Строка 1\n')
stdout.write('Строка 2\n')
# Метод write() возвращает результат - значение, полученное в процессе выполненных методом вычислений. Таковым
# результатом является количество символов в выведенной строке. Его можно присвоить какой-либо переменной и
# использовать в дальнейшем:
cnt = stdout.write('Привет, Python\n')
print('Символов в выведенной строке: ', cnt)
# Результат:
# Привет, Python
# Символов в выведенной строке: 15


# 1.7. Ввод данных
print('1.7. Ввод данных')
# Для ввода данных в Python предназначена функция input(), которая получает данные со стандартного потока ввода stdin.
# Функция имеет следующий формат:
# input([<Сообщение>])
# Введенное значение она возвращает в качестве результата. Этот результат следует присвоить какой-либо переменной
# посредством оператора =.
# Для примера переделаем программу так, чтобы она здоровалась не со всем миром, а только с нами (test_00006.py).
# В первой инструкции значение, введенное пользователем и полученное функцией input(), присваивается переменной name.
# Сохраняем программу в файле test_00006.py и запускаем на выполнение с помощью двойного щелчка. Откроется черное окно,
# в котором мы увидим надпись: Введите ваше имя: Вводим свое имя - например, Николай, и нажимаем клавишу <Enter>.
# В результате будет выведено приветствие: Привет, Николай.
# При использовании функции input() следует учитывать, что при достижении конца файла или при нажатии комбинации клавиш
# <Ctrl>+<Z>, а затем клавиши <Enter> генерируется исключение EOFError. Если не предусмотреть обработку исключения, то
# программа аварийно завершится. Обработать исключение можно следующим образом:
# try:
#   s = input('Введите данные: ')
#   print(s)
# except EOFError:
#   print('Обработали исключение EOFError')
# Если внутри блока try возникнет исключение EOFError, то управление будет передано в блок except. После исполнения
# инструкций в блоке except программа нормально продолжит работу.
# Передать данные можно в консоли, указав их после имени файла программы. Такие данные доступны через список argv из
# модуля sys. Первый элемент списка argv будет содержать имя файла запущенной программы, а последующие элементы -
# переданные данные. Для примера создадим файл test_00007.py в каталоге C:\book.
# Теперь запустим программу на выполнение из консоли, передав ей данные. Запустим консоль, для чего выберем в меню Пуск
# пункт Выполнить, в открывшемся окне наберем команду cmd и нажмем кнопку ОК. Откроется черное окно с приглашением для
# ввода команд. Перейдем в каталог C:\book, набрав команду:
# cd C:\book
# В консоли должно появиться приглашение:
# C:\book>
# Для запуска нашей программы вводим команду:
# test_00007.py uhud opk987
# В этой команде мы передаем имя файла (test_00007.py) и некоторые данные (-uNik и -р12З).
# Результат выполнения программы будет выглядеть так:
# test2.py
# uhud
# opk987


# 1.8. Утилита pip: установка дополнительных библиотек
print('1.8. Утилита pip: установка дополнительных библиотек')
# Интерпретатор Python поставляется с богатой стандартной библиотекой, реализующей, в частности, работу с файлами,
# шифрование, архивирование, обмен данными по сети и пр. Однако такие операции, как обработка графики, взаимодействие
# с базами данных SQLite, MySQL и многое другое, она не поддерживает, и для их выполнения нам придется устанавливать
# дополнительные библиотеки.
# Для установки дополнительных библиотек в Python достаточно воспользоваться имеющейся в комплекте поставки Python
# утилитой pip, которая самостоятельно найдет запрошенную библиотеку в интернет-хранилище (репозитории) PyPI (Python
# Package Index, реестр пакетов Python), загрузит дистрибутивный пакет с редакцией библиотеки, совместимый с
# установленной версией Python, и установит ее. Если инсталлируемая библиотека требует для работы другие библиотеки, они
# также будут установлены. Помимо этого, утилита pip позволяет просмотреть список уже установленных библиотек, получить
# сведения о выбранной библиотеке и удалить ненужную библиотеку. Для использования утилиты pip в консоли следует набрать
# команду следующего формата:
# pip <Команда и ее опции> <Универсальные опции>
# Параметр <Команда и ее опции> указывает, что должна сделать утилита: установить библиотеку, вывести список библиотек,
# предоставить сведения об указанной библиотеке или удалить ее. Параметр <Универсальные опции> задают дополнительные
# настройки для самой утилиты и действуют на все поддерживаемые ею команды. Далее приведен сокращенный список
# поддерживаемых утилитой pip команд вместе с их собственными опциями, а также наиболее востребованных универсальных
# опций. Полный список всех команд pip можно получить, воспользовавшись командой help и опцией -h.
# Итак, утилита pip поддерживает следующие наиболее полезные нам команды:
# install - установка указанной библиотеки. Формат этой команды таков:
# pip install [<Опции>] <Название библиотеки>
# Если в параметре <Опции> не указана ни одна из них (см. далее), утилита просто загрузит и установит библиотеку с
# указанным названием. Если такая библиотека уже установлена, ничего не произойдет. Вот пример установки библиотеки
# Pillow:
# pip install pillow
# Доступные опции:
# -u (или --upgrade) - обновление библиотеки с заданным названием до актуальной версии, имеющейся в репозитории PyPI.
# Обновляем библиотеку Pillow:
# pip install -U pillow
# --force-reinstall - выполняет полную переустановку заданной библиотеки. Обычно используется вместе с опцией -u;
# --compile - после установки библиотеки откомпилировать ее код. Позволяет ускорить запуск программ, использующих эту
# библиотеку.
# Если указано лишь название библиотеки, будет установлена наиболее актуальная версия этой библиотеки.
# Если нужно установить определенную версию библиотеки, в качестве параметра <Название библиотеки> также можно
# использовать конструкцию такого формата (кавычки обязательны):
# "<Название библиотеки><Оператор сравнения><Номер версии библиотеки>"
# Номер версии устанавливаемой библиотеки задается в формате:
# <Номер старшей версии>.<Номер младшей версии>[.<Номер модификации>]
# Все номера указываются в виде целых чисел.
# Пример установки библиотеки Pillow версии 8.4.0:
# pip install "pillow==8.4.0"
# Если номер модификации не указан, будет установлена версия с наиболее актуальной модификацией, имеющаяся в
# репозитории. Пример:
# pip install "pillow==8.4"
# Вместо любого из номеров, указываемых в составе версии, можно записать символ подстановки *. В таком случае будет
# установлена версия библиотеки, в которой соответствующий номер будет максимальным из присутствующих в репозитории.
# Пример установки библиотеки Pillow со старшей версией 7 и наиболее актуальной младшей:
# pip install "pillow=7.*"
# Поддерживаются следующие операторы сравнения:
# == - равно;
# < - меньше;
# > - больше;
# <= - не больше (меньше или равно);
# >= - не меньше (больше или равно);
# ~= - совместимо (будет описан позже).
# Пример установки библиотеки Pillow версии 5.0.0 или более новой:
# pip install "pillow>=5.0.0"
# После названия библиотеки можно указать несколько конструкций формата:
# <Оператор сравнения><Номер версии>
# разделив их запятыми (после которых можно поставить пробелы). Каждая из этих конструкций задаст одно условие, которому
# должна удовлетворять устанавливаемая версия библиотеки. Будет установлена версия, удовлетворяющая всем указанным
# условиям.
# Пример установки библиотеки Pillow версии не ниже 8.4.0 и меньше 8.6.0:
# pip install "pillow>=8.4.0, <8.6.0"
# Что касается оператора ~= (совместимо), то при его использовании будет установлена либо указанная версия библиотеки,
# либо, при отсутствии таковой:
#  - если модификация указана - библиотека с заданными номерами старшей, младшей версий и указанной или, если таковая
#  отсутствует, наиболее актуальной модификацией из имеющихся в репозитории;
# - если модификация не указана - библиотека с заданным номером старшей версии и указанными или, если таковые
# отсутствуют, наиболее актуальными младшей версией и модификацией.
# Примеры:
# pip install "pillow~=8.4.0"
# pip install "django~=З.1"
# list - вывод списка установленных библиотек и их версий. Формат команды:
# pip list [<Опции>]
# Пример:
# pip list
# У авторов было выведено:
# Package Version
# Pillow 8.4.0
# pip 21.2.4
# setuptools 58.1.0
# Единственная доступная здесь опция: --format=<Формат вывода>, задающая формат вывода. В качестве параметра <Формат
# вывода> можно указать columns (вывод в виде таблицы, как было показано в приведенном примере,- это формат по
# умолчанию), freeze (вывод в виде перечня) или json (вывод в формате JSON). Вот пример вывода списка установленных
# библиотек, оформленного в виде перечня:
# pip list --format=freeze
# У авторов было выведено:
# Pillow==8.4.0
# pip=21.2.4
# setuptools= 58.1.0
# Вывод в формате JSON:
# pip list --format=json
# У авторов получилось:
# [{"name": "Pillow", "version": "8.4.0"},
# {"name": "pip", "version": "21.2.4"},
# {"name": "setuptools", "version": "58.1.0"}]
# show - вывод сведений об указанной библиотеке. Формат команды:
# pip show [<Опции>] <Название библиотеки>
# выводятся название библиотеки, ее версия, краткое описание, интернет-адрес 'домашнего' сайта, имя разработчика, его
# адрес электронной почты, название лицензии, по которой распространяется библиотека, путь, по которому она установлена,
# список библиотек, требующихся ей для работы, и список библиотек, которым она требуется для работы (если таковые есть).
# Для примера посмотрим сведения о Pillow:
# pip show pillow
# Вывод:
# Name: Pillow
# Version: 8.4.0
# Summary: Python Imaging Library (Fork)
# Home-page: https://python-pillow.org
# Author: Alex Clark (PIL Fork Author)
# Author-email: aclark@python-pillow.org
# License: HPND
# Location: c:\python310\lib\site-packages
# Requires:
# Required-by:
# Единственная доступная опция: -f (или --files), которая указывает утилите pip дополнительно вывести список всех
# файлов, составляющих библиотеку. Вот пример вывода сведений о библиотеке Pillow, включая перечень составляющих ее
# файлов:
# pip show -f pillow
# uninstall - удаление указанной библиотеки. Формат команды:
# pip uninstall [<Опции>] <Название библиотеки>
# Сначала будет выведен перечень каталогов, в которых хранятся файлы удаляемой библиотеки, и вопрос, действительно ли
# пользователь хочет удалить ее. Чтобы подтвердить удаление, нужно ввести букву у, чтобы отменить его - n, после чего в
# любом случае нажать клавишу <Enter>. Вот пример удаления библиотеки Pillow:
# pip uninstall pillow
# Из всех доступных опций для нас будет полезна только -у (или --yes), подавляющая вывод вопроса на удаление библиотеки.
# Пример:
# pip uninstall -у pillow
# help - вывод справочных сведений об утилите pip, поддерживаемых ею командах и опциях. Формат команды:
# pip help [<Команда>]
# Если <Команда> не указана - будет выведен список всех поддерживаемых утилитой pip команд и универсальных опций:
# pip help
# Того же результата можно достичь, просто запустив в консоли утилиту pip безо всяких параметров.
# Если <Команда> указана - будет выведена справочная информация об этой команде и всех ее опциях, а также перечень
# универсальных опций. В качестве примера выведем описание команды install:
# pip help install
# Универсальные опции, поддерживаемые pip:
# --proxy - задает прокси-сервер, через который будет выполняться доступ к Интернету.
# Формат использования:
# --proxy=[<Имя пользователя>:<Пароль пользователя>@]<Интернет-адрес>:<Номер порта>
# Пример:
# pip install pillow --proxy=user123:pAsSwOrD@192.168.1.1:3128
# --no-cache-dir - отключает кеширование загруженных из репозитория библиотек на локальном диске. Работает только с
# командой install.
# -v (или --verbose) - вывод более подробных сведений о выполняемых утилитой pip действиях. Опция может быть указана
# один раз, дважды или трижды, тем самым задавая вывод все более и более подробных сведений:
# pip show pillow -v
# pip show pillow -v -v
# pip install pillow -v -v -v
# Дает эффект не со всеми командами pip.
# -q (или --quiet) - вывод менее подробных сведений о выполняемых утилитой pip действиях. Также может быть указана один
# раз, дважды или трижды, тем самым задавая вывод все менее и менее подробных сведений:
# pip uninstall, pillow -q
# pip install pillow -q -q
# pip install pillow -q -q -q
# Дает эффект не со всеми командами pip.
# -h (или --help) - вывод справочных сведений о заданной команде pip, всех ее опциях и универсальных опциях pip (т. е.
# дает эффект, аналогичный отдаче описанной ранее команды help с указанием команды, для которой нужно вывести справку).
# Для примера выведем сведения о команде uninstall:
# pip uninstall -h
# Все дополнительные библиотеки устанавливаются в каталог <Каталог установки Python>\Lib\site-packages.
# В составе некоторых библиотек присутствуют программы, запускаемые из консоли. Такие программы устанавливаются в
# каталог <Каталог установки Python>\Scripts. Путь к этому каталогу при установке Python добавляется в список путей из
# системной переменной РАТН, поэтому любую из записанных в этом каталоге программ можно запустить, просто набрав в
# консоли ее имя.
# Если Python был установлен в каталог c:\Program Files (х86) или c:\Program Files, дополнительные библиотеки будут
# устанавливаться по пути C:\Users\<Имя учетной записи>\AppData\Roaming\Python\Python<Номер версии>\site-packages, а
# программы, входящие в состав библиотек, - по пути
# с:\Users\<Имя учетной записи>\AppData\Roaming\Python\Python<Номер версии>\Scripts. Путь к каталогу программ не
# добавляется в список путей из переменной РАТН, и нам его придется добавить туда самостоятельно (или для запуска любой
# программы набирать полный путь к ней).


# 1.9. Доступ к документации
print('1.9. Доступ к документации')
# В составе Python поставляется документация по этому языку в формате СНМ. Чтобы открыть ее, в меню Пуск | Python 3.10
# нужно выбрать пункт Python 3.10 Manuals (32-bit) или Python 3.10 Manuals (64-bit).
# Если в меню Пуск | Python 3.10 выбрать пункт Python 3.10 Module Docs (32-bit) или Python 3.10 Module Docs (64-bit),
# запустится сервер документов pydoc. Это написанный на самом Python веб-сервер, выводящий в веб-браузере документацию
# по модулям стандартной библиотеки Python.
# Сразу после запуска pydoc откроется веб-браузер, в котором будет выведен список всех модулей стандартной библиотеки.
# Щелкнув на имени модуля, мы откроем страницу с описанием всех классов, функций и констант, объявленных в этом модуле.
# Чтобы завершить работу pydoc, следует переключиться в его окно, ввести в нем команду q (от quit, выйти) и нажать
# клавишу <Enter> - окно при этом автоматически закроется. А введенная там команда b (от browser, браузер) повторно
# выведет в браузере страницу со списком модулей.
# Документацию по различным языковым конструкциям Python можно получить, запустив интерпретатор в интерактивном режиме
# и вызвав функцию help(). В качестве примера отобразим документацию по встроенной функции input():
help(input)
# Результат выполнения:
# Help on built-in function input in module builtins:
# input(prompt=None, /)
# Read а string from standard input. The trailing newline is stripped. The prompt string, if given, is printed to
# standard output without а trailing newline before reading input. If the user hits EOF (*nix: Ctrl-D,
# Windows: Ctrl-Z+Return), raise EOFError. On *nix systems, readline is used if available.
# С помощью функции help() можно получить документацию не только по конкретной функции, но и по всему модулю сразу. Для
# этого необходимо предварительно подключить нужный модуль. Например, подключим модуль builtins, содержащий определения
# всех # встроенных функций и классов, а затем выведем документацию по нему:
help(builtins)
# Для комментирования кода часто используются строки документирования. Такая строка сохраняется в атрибуте _doc_.
# Функция help() при составлении документации получает информацию из этого атрибута.
# В качестве примера создадим файл test_00008.py.
# Теперь подключим этот модуль и выведем содержимое строк документирования, записанных в нем. Все эти действия выполняет
# код из test_00009.py.
# Запустим эту программу в окне IDLE Shell или щелчком мыши и получим, результат:
# Help on module test_00008:
# NAME
#     test_00008 - Это описание нашего модуля
# FUNCTIONS
#     func()
#         Это описание функции
# FILE
#     /test_00008.py
# Теперь получим содержимое строк документирования с помощью атрибута _doc_. Как это делается, показывает код из
# test_00010.py.
# Результат выполнения:
# Это описание нашего модуля
# Это описание функции
# Атрибут _doc_ можно использовать вместо функции help(). В качестве примера получим документацию по функции input():
print(input.__doc__)
# Результат выполнения:
# Read a string from standard input.  The trailing newline is stripped.
# The prompt string, if given, is printed to standard output without a trailing newline before reading input.
# If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError. On *nix systems, readline is used if
# available.
# Получить список всех идентификаторов внутри модуля позволяет функция dir(). Пример ее использования показывает код из
# test_00011.py.
# Результат выполнения:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'func']
# Теперь получим список всех встроенных идентификаторов:
print(dir(builtins))
# Будучи вызванной без параметров, функция dir() возвращает список идентификаторов из текущего модуля:
print(dir())
# Результат выполнения:
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'arr', 'builtins', 'cnt', 'i', 'n', 'stdout', 'x']


# 1.10 Компиляция Python-файлов
print('1.10 Компиляция Python-файлов')
# При запуске любой Python-программы, сохраненной в файле, интерпретатор предварительно выполняет ее компиляцию -
# преобразование кода программы в особое компактное внутреннее представление. Откомпилированный код сохраняется в
# оперативной памяти и запускается на исполнение. Код, прошедший компиляцию, занимает меньше места и быстрее
# выполняется.
# К сожалению, после завершения выполнения программы откомпилированный код удаляется из памяти. И при повторном запуске
# этой же программы ее компиляция выполняется заново, что замедляет запуск.
# Однако можно выполнить компиляцию указанного модуля (и даже всех модулей, хранящихся в указанном каталоге) с
# сохранением откомпилированного кода в файле. При запуске такого файла хранящаяся в нем программа запустится очень
# быстро, поскольку интерпретатору не придется выполнять предварительную компиляцию кода.
# Для компиляции Python-модулей следует набрать в консоли команду.
# python -m compileall <Путь к файлу>|<Путь к каталогу> <Опции>
# Можно указать либо путь к файлу модуля, который следует откомпилировать.
# python -m compileall c:\work\python\program1.py
# Либо путь к каталогу - в этом случае будут откомпилированы все модули, хранящиеся как в каталоге с указанным путем,
# так и во вложенных в него каталогах.
# python -m compileall c:\work\python\big_program
# Откомпилированные модули сохранятся в каталоге _pycache_, который создается в каталоге с исходными Python-модулями, в
# файлах с именами формата:
# <Имя исходного модуля>.сpython-<Номер версии Python>.pyc
# Например, откомпилированный код модуля test_00001.py будет сохранен в файле _pycache_\hello_world.cpython-31 О.рус.
# Расширение рус также ассоциируется с исполняющей средой Python, поэтому файлы с таким расширением можно запускать
# простым щелчком мышью. А при распространении Python-программы можно передать конечным пользователям только
# откомпилированные файлы, содержащие ее код.
# При повторной компиляции будут откомпилированы только те модули, чье содержимое изменилось после предыдущей
# компиляции. Python отслеживает изменение содержимого модулей по дате и времени последнего изменения файлов, в которых
# они хранятся.
# Команда компиляции поддерживает следующие полезные опции:
# -l - компилировать только модули, непосредственно находящиеся в каталоге с указанным путем. Модули во вложенных
# каталогах компилироваться не будут;
# -f - принудительно перекомпилировать все модули в указанном каталоге, даже не изменившиеся после последней компиляции.
# Следует отметить, что при подключении какого-либо модуля с целью использовать созданные в нем функции и объекты он
# всегда компилируется с сохранением результирующего кода в файл. Это делается для ускорения запуска программ,
# использующих этот же модуль.

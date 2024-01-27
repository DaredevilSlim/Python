#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 7 Списки и кортежи
print('7 Списки и кортежи')
# 7.1 Последовательности
print('7.1 Последовательности')
# Последовательность — это объект, содержащий многочисленные значения, которые следуют одно за другим. Над
# последовательностью можно выполнять операции для проверки значений и управления хранящимися в ней значениями.
# Последовательность — это объект в виде индексируемой коллекции, который содержит многочисленные значения данных.
# Хранящиеся в последовательности значения следуют одно за другим. Python предоставляет разнообразные способы выполнения
# операций над значениями последовательностей.
# В Python имеется несколько разных типов объектов-последовательностей. В этой главе мы рассмотрим два фундаментальных
# типа: списки и кортежи. Списки и кортежи — это последовательности, которые могут содержать разные типы данных. Отличие
# списков от кортежей простое: список является мутируемой последовательностью (программа может изменять его содержимое),
# а кортеж — немутируемой последовательностью (т. е. после его создания его содержимое изменить невозможно).


# 7.2 Введение в списки
print('7.2 Введение в списки')
# Список — это объект, который содержит многочисленные элементы данных. Списки являются мутируемыми
# последовательностями, т. е. их содержимое может изменяться во время исполнения программы. Списки являются
# динамическими структурами данных, т. е. элементы в них могут добавляться или удаляться из них. Для работы со списками
# в программе можно применять индексацию, нарезку и другие разнообразные методы.
# Список — это объект, который содержит многочисленные элементы данных. Каждая хранящаяся в списке порция данных
# называется элементом. Ниже приведена инструкция, которая создает список целых чисел:
even_numbers = [2, 4, 6, 8, 10]
print(even_numbers)
names = ['Молли', 'Стивен', 'Уилл', 'Алисия', 'Адриана']
print(names)
# Список может содержать значения разных типов:
info = ['Алисия', 27, 1550.87]
print(info)
# Python также имеет встроенную функцию list(), которая может преобразовывать некоторые типы объектов в списки.
# Для преобразования в список итерируемого объекта с помощью функции range можно, в частности, применить приведенную
# ниже инструкцию:
numbers = list(range(5))
print(numbers)
# Во время исполнения этой инструкции происходит следующее:
# 1. Вызывается функция range, в которую в качестве аргумента передается число 5. Эта функция возвращает итерируемый
# объект, содержащий значения 0, 1, 2, 3, 4.
# 2. Итерируемый объект передается в качестве аргумента в функцию list(). Функция list() возвращает список
# [0, 1, 2, 3, 4].
# 3. Список [0, 1, 2, 3, 4] присваивается переменной numbers.
numbers = list(range(1, 10, 2))
print(numbers)
# При передаче в функцию range трех аргументов первым аргументом является начальное значение, вторым аргументом —
# конечный предел, третьим аргументом — величина шага. Эта инструкция присвоит переменной numbers список
# [1, 3, 5, 7, 9].

# Оператор повторения.
# Когда операнд слева от символа * является последовательностью (в частности, списком), а операнд справа — целым числом,
# он становится оператором повторения. Оператор повторения делает многочисленные копии списка и все их объединяет.
# Вот общий формат операции:
# список * n
# В данном формате список — это обрабатываемый список, n — число создаваемых копий.
numbers = [0] * 5
print(numbers)
numbers = [1, 2, 3] * 3
print(numbers)
# Большинство языков программирования позволяет создавать последовательные структуры, именуемые массивами, которые
# аналогичны спискам, но намного более ограничены в своих возможностях. В Python нельзя создать традиционные массивы,
# потому что списки служат той же цели и предоставляют гораздо больше встроенных возможностей.

# Последовательный обход списка в цикле for.
# Один из самых простых способов доступа к отдельным элементам в списке состоит в использовании цикла for.
# Вот общий формат:
# for переменная in список:
#   инструкция
#   инструкция
#   ...
# В общем формате переменная — это имя переменной, а список — это имя списка. Всякий раз, когда цикл повторяется,
# переменная будет ссылаться на копию элемента в списке, начиная с первого элемента. Мы говорим, что цикл перебирает,
# или прокручивает, элементы в списке.
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

# Индексация.
# Еще один способ доступа к отдельным элементам в списке реализован посредством индексации. Каждый элемент в списке
# имеет индекс, который определяет его позицию в списке.
# Индексация начинается с 0, поэтому индекс первого элемента равняется 0, индекс второго элемента равняется 1 и т. д.
# Индекс последнего элемента в списке на 1 меньше числа его элементов.
my_list = [10, 20, 30, 40]
index = 0
while index < 4:
    print(my_list[index])
    index += 1
# Для идентификации позиций элементов относительно конца списка можно также использовать отрицательные индексы. Для того
# чтобы определить позицию элемента, интерпретатор Python прибавляет отрицательные индексы к длине списка. Индекс –1
# идентифицирует последний элемент списка, –2 — предпоследний элемент и т. д.

# Функция len.
# Python имеет встроенную функцию len, которая возвращает длину последовательности, в частности, списка.
my_list = [10, 20, 30, 40]
size = len(my_list)
print(size)

# Использование цикла for для обхода списка по индексу.
# Вы можете использовать функцию len вместе с функцией range, чтобы получить индексы списка. Например, предположим, что
# у нас есть следующий список строковых литералов:
names = ['Дженни', 'Келли', 'Хлоя', 'Обри']
for index in range(len(names)):
    print(names[index])

# Списки как мутируемые последовательности.
# Списки в Python являются мутируемыми последовательностями, т. е. их элементы могут изменяться. Следовательно,
# выражение в форме список[индекс] может появляться слева от оператора присваивания.
# Когда для присвоения значения элементу списка применяется выражение индексации, следует использовать допустимый индекс
# существующего элемента, в противном случае произойдет исключение IndexError.
# В программе в файле sales_list.py приведен пример присвоения элементам списка вводимых пользователем значений.
# Пользователю нужно ввести суммы продаж, которые будут присвоены списку.

# Конкатенирование списков.
# Конкатенировать означает соединять две части воедино. Для конкатенирования двух списков используется оператор +.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)
girl_names = ['Джоанна', 'Карен', 'Лори']
boy_names = ['Крис', 'Джерри', 'Уилл']
all_names = girl_names + boy_names
print(all_names)
# Для того чтобы соединить два списка, можно воспользоваться расширенным оператором присваивания +=.
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1 += list2
print(list1)
girl_names = ['Джоанна', 'Карен', 'Лори']
girl_names += ['Дженни', 'Келли']
print(girl_names)
# Следует иметь в виду, что конкатенировать списки можно только с другими списками. Если попытаться присоединить к
# списку нечто, не являющееся списком, будет вызвано исключение.


# 7.3 Нарезка списка
print('7.3 Нарезка списка')
# Выражение среза извлекает диапазон элементов из последовательности.
# В Python можно составлять выражения, которые извлекают части последовательности, которые называются срезами.
# Срез — это диапазон элементов, которые извлекаются из последовательности. Для того чтобы получить срез списка, пишут
# выражение в приведенном ниже общем формате:
# имя_списка[начало:конец]
# В данном формате начало — это индекс первого элемента в срезе, конец — индекс, отмечающий конец среза. Это выражение
# возвращает список, содержащий копию элементов с начала до конца (но не включая последний).
# В качестве индексов в выражениях среза также можно использовать отрицательные числа, чтобы ссылаться на позиции
# относительно конца списка. Python прибавляет отрицательный индекс к длине списка, чтобы ссылаться на позицию по этому
# индексу.
# Недопустимые индексы в выражении среза исключений не вызывают. Например:
# - если индекс конца задает позицию за пределами конца списка, то Python вместо него будет использовать длину списка;
# - если индекс начала задает позицию до начала списка, Python вместо него будет использовать 0;
# - если индекс начала будет больше индекса конца, то выражение среза вернет пустой список.


# 7.4 Поиск значений в списках при помощи инструкции in
print('7.4 Поиск значений в списках при помощи инструкции in')
# Поиск значения в списке выполняется при помощи оператора in.
# В Python оператор in применяется для определения, содержится ли значение в списке. Вот общий формат выражения с
# оператором in для поиска значения в списке:
# значение in список
# В данном формате значение — это искомое значение, список — список, в котором выполняется поиск. Это выражение
# возвращает истину, если значение в списке найдено, и ложь в противном случае.

# 7.5 Методы обработки списков и полезные встроенные функции
print('7.5 Методы обработки списков и полезные встроенные функции')
# Списки имеют многочисленные методы, которые позволяют работать с содержащимися в них значениями. Python также
# предлагает несколько встроенных функций, которые широко используются для работы со списками.
# Списковые методы
# Метод                     Описание
# append(значение)          Добавляет значение в конец списка
# index(значение)           Возвращает индекс первого элемента, значение которого равняется значению. Если значение в
#                           списке не найдено, вызывается исключение ValueError
# insert(индекс, значение)  Вставляет значение в заданную индексную позицию в списке. Когда значение вставляется в
#                           список, список расширяется, чтобы разместить новое значение. Значение, которое ранее
#                           находилось в заданной индексной позиции, и все элементы после него сдвигаются на одну
#                           позицию к концу списка. Если указан недопустимый индекс, исключение не происходит. Если
#                           задан индекс за пределами конца списка, значение будет добавлено в конец списка. Если
#                           применен отрицательный индекс, который указывает на недопустимую позицию, значение будет
#                           вставлено в начало списка
# sort()                    Сортирует значения в списке, в результате чего они появляются в возрастающем порядке (с
#                           наименьшего значения до наибольшего)
# remove(значение)          Удаляет из списка первое появление значения. Если значение в списке не найдено, вызывается
#                           исключение ValueError
# reverse()                 Инвертирует порядок следования значений в списке, т. е. меняет его на противоположное

# Метод append().
# Метод append() обычно применяется для добавления значений в список. Значение, которое передается в качестве аргумента,
# добавляется в конец существующих элементов списка.

# Метод index().
# Ранее вы познакомились с тем, как оператор in можно применять для определения, находится ли значение в списке. Иногда
# необходимо знать не только, что значение находится в списке, но и где оно расположено. Метод index() используется как
# раз для таких случаев.
# В метод index() передается аргумент, и он возвращает индекс первого элемента в списке, который содержит это значение
# аргумента. Если значение в списке не найдено, то метод вызывает исключение ValueError.

# Метод insert().
# Метод insert() позволяет вставлять значение в список в заданной позиции. В метод insert() передаются два аргумента:
# индекс, задающий место вставки значения, и значение, которое требуется вставить.

# Метод sort().
# Метод sort() перестраивает элементы списка таким образом, что их значения появляются в возрастающем порядке (от самого
# малого значения до самого большого).
my_list = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
print('Первоначальный порядок:', my_list)
my_list.sort()
print('Отсортированный порядок:', my_list)
my_list = ['бета', 'альфа', 'дельта', 'гамма']
print('Первоначальный порядок:', my_list)
my_list.sort()
print('Отсортированный порядок:', my_list)

# Метод remove().
# Метод remove() удаляет значение из списка. Методу в качестве аргумента передается значение, и первый элемент, который
# содержит это значение, удаляется. Метод уменьшает размер списка на один элемент. Все элементы после удаленного
# элемента смещаются на одну позицию к началу списка. Если элемент в списке не найден, то вызывается исключение
# ValueError.

# Метод reverse().
# Метод reverse() просто инвертирует порядок следования значений в списке.
my_list = [1, 2, 3, 4, 5]
print('Первоначальный порядок:', my_list)
my_list.reverse()
print('Инвертированный порядок:', my_list)

# Инструкция del.
# Метод remove(), который вы видели ранее, удаляет заданное значение из списка, если это значение находится в списке.
# Некоторые ситуации могут потребовать удалить элемент из заданной индексной позиции, независимо от значения, которое
# хранится в этой индексной позиции. Это может быть выполнено при помощи инструкции del.
my_list = [1, 2, 3, 4, 5]
print('Перед удалением:', my_list)
del my_list[2]
print('После удаления:', my_list)

# Функции min и max.
# Python имеет две встроенные функции, min и max, которые работают с последовательностями. Функция min принимает в
# качестве аргумента последовательность, в частности список, и возвращает элемент, который имеет минимальное значение в
# последовательности.
my_list = [5, 4, 3, 2, 50, 40, 30]
print('Минимальное значение равняется', min(my_list))
# Функция max принимает в качестве аргумента последовательность, в частности список, и возвращает элемент, который имеет
# максимальное значение в последовательности.
my_list = [5, 4, 3, 2, 50, 40, 30]
print('Максимальное значение равняется', max(my_list))


# 7.6 Копирование списков
print('7.6 Копирование списков')
# Для создания копии списка необходимо скопировать элементы списка.


# 7.7 Обработка списков
print('7.7 Обработка списков')

# Использование элементов списка в математическом выражении.

# Суммирование значений в списке.

# Усреднение значений в списке.

# Передача списка в функцию в качестве аргумента.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

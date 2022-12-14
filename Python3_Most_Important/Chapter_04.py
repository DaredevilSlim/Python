#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Глава 4
# Условные операторы и циклы
print('Условные операторы и циклы:')
# Условные операторы позволяют в зависимости от значения логического выражения выполнить отдельный участок программы
# или, наоборот, не выполнить его. Логические выражения возвращают только два значения: True (истина) или False (ложь),
# которые ведут себя как целые числа 1 и 0 соответственно:
print(True + 2)  # Эквивалентно 1 + 2 = 3
print(False + 2)  # Эквивалентно 0 + 2 = 2
# Логическое значение можно сохранить в переменной:
x = True
y = False
print(x, y)
# Любой объект в логическом контексте может интерпретироваться как истина (True) или как ложь (False). Для определения
# логического значения можно использовать функцию bool().
# Значение True возвращает следующие объекты:
# Любое число, не равное нулю:
print('Любое число, не равное нулю:')
print(bool(1), bool(20), bool(-20))
print(bool(1.0), bool(0.1), bool(-20.0))
# Не пустой объект:
print('Не пустой объект:')
print(bool('0'), bool([0, None]), bool((None,)), bool({'x': 5}))
# Следующие объекты интерпретируются как False:
# Число равное нулю:
print('Число равное нулю:')
print(bool(0), bool(0.0))
# Пустой объект:
print('Пустой объект:')
print(bool(''), bool([]), bool(()))
# Значение None:
print('Значение None:')
print(bool(None))


# 4.1 Операторы сравнения
print('Операторы сравнения:')
# Операторы сравнения используются в логических выражениях.
# Операторы сравнения:
# == - Равно:
print('Равно:')
print(1 == 1, 1 == 5)
# != - Не равно:
print('Не равно:')
print(1 != 5, 1 != 1)
# < - Меньше:
print('Меньше:')
print(1 < 5, 1 < 0)
# > - Больше:
print('Больше:')
print(1 > 0, 1 > 5)
# <= - Меньше или равно:
print('Меньше или равно:')
print(1 <= 5, 1 <= 0, 1 <= 1)
# >= - Больше или равно:
print('Больше или равно:')
print(1 >= 0, 1 >= 5, 1 >= 1)
# in - Проверка на вхождение в последовательность:
print('Проверка на вхождение в последовательность:')
print('Строка' in 'Строка для поиска')  # Строки
print(2 in [1, 2, 3], 4 in [1, 2, 3])  # Списки
print(2 in (1, 2, 3), 4 in (1, 2, 3))  # Кортежи
# Оператор in можно также использовать для проверки существования ключа словаря:
print('Оператор in можно также использовать для проверки существования ключа словаря:')
print('x' in {'x': 1, 'y': 2}, 'z' in {'x': 1, 'y': 2})
# not in - Проверка на не вхождение в последовательность:
print('Проверка на не вхождение в последовательность:')
print('Строка' in 'Строка для поиска')  # Строки
print(2 not in [1, 2, 3], 4 not in [1, 2, 3])  # Списки
print(2 not in (1, 2, 3), 4 not in (1, 2, 3))  # Кортежи
# is - Проверка ссылаются ли две переменные на один и тот же объект. Если переменные ссылаются на один и тот же объект,
# то оператор is возвращает значение True:
print('Проверка ссылаются ли две переменные на один и тот же объект:')
x = y = [1, 2]
print(x is y)
x = [1, 2]
y = [1, 2]
print(x is y)
# В целях повышения эффективности интерпретатор производит кэширование малых целых чисел и небольших строк. Это
# означает, что если ста переменным присвоено число 2, то в этих переменных будет сохранена ссылка на один и тот же
# объект.
x = 2
y = 2
z = 2
print(x is y, y is z)
# is not - Проверка ссылаются ли две переменные на разные объекты. Если переменные ссылаются на разные объекты, то
# оператор is not возвращает значение True:
print('Проверка ссылаются ли две переменные на разные объекты:')
x = y = [1, 2]
print(x is not y)
x = [1, 2]
y = [1, 2]
print(x is not y)
# Значение логического выражения можно инвертировать с помощью оператора not:
print('Значение логического выражения можно инвертировать с помощью оператора not:')
x = 1
y = 1
print(x == y)
print(not (x == y), not x == y)
# Если переменные х и у равны, то возвращается значение True, но так как перед выражением стоит оператор nоt, выражение
# вернет False. Круглые скобки можно не указывать, поскольку оператор not имеет более низкий приоритет выполнения, чем
# операторы сравнения.
# В логическом выражении можно указывать сразу несколько условий:
print('В логическом выражении можно указывать сразу несколько условий:')
print(1 < x < 20, 11 < x < 20)
# Несколько логических выражений можно объединить в одно большое с помощью следующих операторов:
# and - Логическое И. Если x в выражении x and y интерпретируется как False, то возвращается x, в противном случае y:
print('Логическое И:')
print(1 < 5 and 2 < 5)  # True and True == True
print(1 > 6 and 2 < 5)  # False and True == False
print(10 and 20, 0 and 20, 10 and 0)
# or - Логическое ИЛИ. Если x в выражении x or y интерпретируется как False, то возвращается y, в противном случае x:
print('Логическое ИЛИ:')
print(1 < 5 or 2 < 5)  # True or True == True
print(1 < 5 or 2 > 5)  # True or False == True
print(1 > 5 or 2 < 5)  # False or True == True
print(1 > 5 or 2 > 5)  # False or False == False
print(10 or 20, 0 or 20, 10 or 0)
print(0 or '' or None or [] or 's')
# Следующее выражение вернет True только в случае, если оба выражения вернут True:
# x1 == x2 and x2 != x3
# А это выражение вернет True, если хотя бы одно из выражений вернет True:
# x1 == х2 or хЗ == х4
# Операторы сравнения в порядке убывания приоритета:
# 1. <, >, <=, >=, =, !=, <>, is, is not, in, not in.
# 2. not - логическое отрицание.
# 3. and - логическое И.
# 4. or - логическое ИЛИ.


# 4.2 Оператор ветвления if...else
print('Оператор ветвления if...else:')
# Оператор ветвления if...else позволяет в зависимости от значения логического выражения выполнить отдельный участок
# программы или, наоборот, не выполнить его. Оператор имеет следующий формат:
# if <Логическое выражение>:
#   <Блок, выполняемый, если условие истинно>
# [elif <Логическое выражение>:
#   <Блок, выполняемый, если условие истинно>]
# [else:
#   <Блок, выполняемый, если все условия ложны>]
# Как вы уже знаете, блоки внутри составной инструкции выделяются одинаковым количеством пробелов (обычно четырьмя).
# Концом блока является инструкция, перед которой расположено меньшее количество пробелов. В некоторых языках
# программирования логическое выражение заключается в круглые скобки. В языке Python это делать необязательно, но можно,
# т. к. любое выражение может быть расположено внутри круглых скобок. Тем не менее круглые скобки следует использовать
# только при необходимости разместить условие на нескольких строках.
# Для примера напишем программу, которая проверяет, является введенное пользователем число четным или нет
# (test_00017.py). После проверки выводится соответствующее сообщение.
# Совет - Знайте, что так сделать можно, но никогда на практике не пользуйтесь этим способом, поскольку подобная
# конструкция нарушает стройность кода и ухудшает его сопровождение в дальнейшем. Всегда размещайте инструкцию на
# отдельной строке, даже если блок содержит только одну инструкцию.
# Оператор ветвления if ... else позволяет проверить сразу несколько условий. Рассмотрим это на примере (test_00018.py).
# С помощью инструкции elif мы можем определить выбранное значение и вывести соответствующее сообщение. Обратите
# внимание на то, что логическое выражение не содержит операторов сравнения:
# elif not os:
# Такая запись эквивалентна следующей:
# elif os == '':
# Проверка на равенство выражения значению True выполняется по умолчанию. Поскольку пустая строка интерпретируется как
# False, мы инвертируем возвращаемое значение с помощью оператора not. Один условный оператор можно вложить в другой.
# В этом случае отступ вложенной инструкции должен быть в два раза больше (test_00019.py).
# Оператор if...else имеет еще один формат:
# <Переменная> = <Если истина> if <Условие> else <Если ложь>
print('Yes' if 10 % 2 == 0 else 'No')
s = 'Yes' if 10 % 2 == 0 else 'No'
print(s)
s = 'Yes' if 11 % 2 == 0 else 'No'
print(s)


# 4.3 Цикл for
print('Цикл for:')
# Циклы позволяют выполнить одни и те же инструкции многократно.
# Цикл for применяется для перебора элементов последовательности и имеет такой формат:
# for <Текущий элемент> in <Последовательность>:
#   <Инструкции внутри цикла>
# [else:
#   <Блок, выполняемый, если не использовался оператор break>]
# Здесь присутствуют следующие конструкции:
# - <Последовательность> - объект, поддерживающий механизм итерации (строка, список, кортеж, диапазон, словарь и др.);
# - <Текущий элемент> - на каждой итерации через этот параметр доступен текущий элемент последовательности или ключ
# словаря;
# - <Инструкции внутри цикла> - блок, который будет многократно выполняться;
# - если внутри цикла не использовался оператор break, то после завершения выполнения цикла будет выполнен блок в
# инструкции else. Этот блок не является обязательным. Пример перебора букв в слове приведен в (test_00020.py).
# Теперь выведем каждый элемент списка и кортежа на отдельной строке (test_00021.py).
# Цикл for позволяет также перебрать элементы словарей, хотя словари и не являются последовательностями.
# Вывод элементов словаря двумя способами.
# Первый способ использует метод keys (), возвращающий объект dict_keys, который содержит все ключи словаря.
# Второй способ просто указывается словарь в качестве параметра - на каждой итерации цикла будет возвращаться ключ, с
# помощью которого внутри цикла можно получить значение, соответствующее этому ключу.
print('Вывод элементов словаря двумя способами.')
print('Первый способ:')
arr = {'x': 1, 'y': 2, 'z': 3}
print(arr.keys())       # Вывод всех ключей словаря при помощи метода keys()
for key in arr.keys():  # Использование метода keys()
    print(key, arr[key])
print('Второй способ:')
for key in arr:  # Словари также поддерживают итерации
    print(key, arr[key])
# Для вывода элементов словаря в алфавитном порядке, следует отсортировать ключи с помощью функции sorted():
arr = {'x': 1, 'y': 2, 'z': 3}
for key in sorted(arr):
    print(key, arr[key])
# С помощью цикла for можно перебирать сложные структуры данных.
# Вывод элементов списка кортежей:
print('Вывод элементов списка кортежей:')
arr = [(1, 2), (3, 4)]  # Список кортежей
for a, b in arr:
    print(a, b)


# 4.4 Функции range() и enumerate()
print('Функции range() и enumerate():')
# Чтобы получить доступ к каждому элементу, можно воспользоваться функцией range() для генерации индексов.
print('Функция range():')
# Функция range() имеет следующий формат:
# range([<Начало>, ]<Конец> [, <Шаг>])
# Первый параметр задает начальное значение. Если параметр <Начало> не указан, то по умолчанию используется значение 0.
# Во втором параметре указывается конечное значение. Это значение не входит в возвращаемые значения. Если параметр <Шаг>
# не указан, то используется значение 1. Функция возвращает диапазон - особый объект, поддерживающий итерационный
# протокол. С помощью диапазона внутри цикла for можно получить значение текущего элемента.
# Умножение каждого элемента списка на 2:
# Сначала получаем количество элементов списка с помощью функции len() и передаем результат в функцию range(). В итоге
# функция range() возвращает диапазон значений от 0 до len(arr) - 1. На каждой итерации цикла через переменную i
# доступен текущий элемент из диапазона индексов. Чтобы получить доступ к элементу списка, указываем индекс внутри
# квадратных скобок. Умножаем каждый элемент списка на 2, а затем выводим результат с помощью функции print().
print('Умножение каждого элемента списка на 2:')
arr = [1, 2, 3]
print(arr)
for i in range(len(arr)):
    arr[i] *= 2
print(arr)
# Вывод чисел от 1 до 10:
print('Вывод чисел от 1 до 10:')
for i in range(1, 11):
    print(i)
# Вывод чисел от 10 до 1:
print('Вывод чисел от 10 до 1:')
for i in range(10, 0, -1):
    print(i)
# Вывод всех четных чисел от 1 до 10:
print('Вывод всех четных чисел от 1 до 10:')
for i in range(2, 11, 2):
    print(i)
# Создание списка чисел на основе диапазона:
print('Создание списка чисел на основе диапазона:')
obj = range(len([1, 2, 3]))
print(obj)
# Доступ по индексу:
print('Доступ по индексу:')
print(obj[0], obj[1], obj[2])
# Получение среза:
print('Получение среза:')
print(obj[0:2])
# Доступ с помощью итераторов:
print('Доступ с помощью итераторов:')
i = iter(obj)
print(next(i), next(i), next(i))
# Преобразование диапазона в список:
print('Преобразование диапазона в список:')
print(list(obj))
# Проверка вхождения значения:
print('Проверка вхождения значения:')
print(1 in obj, 7 in obj)
# Диапазон поддерживает два полезных метода:
print('Диапазон поддерживает два полезных метода:')
# - index(<Значение>) - возвращает индекс элемента, имеющего указанное значение. Если значение не входит в диапазон,
# возбуждается исключение valueError.
print('Метод - index():')
obj = range(1, 5)
print(obj.index(1), obj.index(4))
# - count(<Значение>) - возвращает количество элементов с указанным значением. Если элемент не входит в диапазон,
# возвращается значение 0.
print('Метод - count():')
obj = range(1, 5)
print(obj.count(1), obj.count(10))
print('Функция enumerate():')
# Функция enumerate(<Объект>[, start=O] ) на каждой итерации цикла for возвращает кортеж из индекса и значения текущего
# элемента. С помощью необязательного параметра start можно задать начальное значение индекса. Умножение на 2 каждого
# элемента списка, который содержит четное число (test_00022.py).
# Функция enumerate() не создает список, а возвращает итератор. С помощью функции next() можно обойти всю
# последовательность. Когда перебор будет закончен, возбуждается исключение Stopiteration:
arr = [1, 2]
obj = enumerate(arr, start=2)
print(next(obj))
print(next(obj))
# Кстати, цикл for при работе активно использует итераторы, но делает это незаметно для нас.


# 4.5 Цикл while
print('Цикл while:')
# Выполнение инструкций в цикле while продолжается до тех пор, пока логическое выражение истинно. Цикл while имеет
# следующий формат:
# <Начальное значение>
# while <Условие>:
#   <Инструкции>
#   <Приращение>
# [else:
#   <Блок, выполняемый, если не использовался оператор break>]
# Последовательность работы цикла while:
# 1. Переменной-счетчику присваивается начальное значение.
# 2. Проверяется условие и, если оно истинно, выполняются инструкции внутри цикла, иначе выполнение цикла завершается.
# 3. Переменная-счетчик изменяется на величину, указанную в параметре <Приращение>.
# 4. Переход к пункту 2.
# 5. Если внутри цикла не использовался оператор break, то после завершения выполнения цикла будет выполнен блок в
# инструкции else. Этот блок не является обязательным. Выведем все числа от 1 до 100, используя цикл while
# (test_00023.py).
# Если <Приращение> не указано, цикл будет бесконечным. Чтобы прервать бесконечный цикл, следует нажать комбинацию
# клавиш <Ctrl>+<C>. В результате генерируется исключение Keyboardinterrupt, и выполнение программы останавливается.
# Следует учитывать, что прервать таким образом можно только цикл, который выводит данные. Выведем все числа от 100 до
# 1 (test_00024.py).
# В следующем примере условие не содержит операторов сравнения. На каждой итерации цикла вычитается единица из значения
# переменной-счетчика. Как только значение будет равно 0, цикл остановится. Число 0 в логическом контексте эквивалентно
# значению False, а проверка на равенство выражения значению True выполняется по умолчанию.
# С помощью цикла while можно перебирать и элементы различных структур. Но в этом случае следует помнить, что цикл
# while работает медленнее цикла for. Умножение каждого элемента списка на 2 (test_00025.py).


# 4.6 Оператор continue: Переход на следующую итерацию цикла
print('Оператор continue: Переход на следующую итерацию цикла:')
# Оператор continue позволяет перейти к следующей итерации цикла до завершения выполнения всех инструкций внутри цикла.
# Вывод всех чисел от 1 до 100, кроме чисел от 5 до 10 включительно (test_00026.py).


# 4.7. Оператор break. Прерывание цикла
print('Оператор break. Прерывание цикла:')
# Оператор break позволяет прервать выполнение цикла досрочно. Вывод всех чисел от 1 до 10 еще одним способом
# (test_00027.py).
# Здесь в условии указано значение True. В этом случае выражения внутри цикла станут выполняться бесконечно. Однако
# использование оператора break прерывает выполнение цикла, как только будет напечатано 100 строк.
# Оператор break прерывает выполнение цикла, а не программы, т.е. далее будет выполнена инструкция, следующая сразу за
# циклом.
# Цикл while совместно с оператором break удобно использовать для получения неопределенного заранее количества данных
# от пользователя. В качестве примера просуммируем
# произвольное количество чисел (test_00028.py).

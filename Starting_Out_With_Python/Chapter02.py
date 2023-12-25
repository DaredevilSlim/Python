#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.3 Вывод данных на экран при помощи функции print
print('2.3 Вывод данных на экран при помощи функции print')
# Функция print используется для вывода на экран выходных данных в программе Python.
# Функция — это фрагмент заранее написанного кода, который выполняет некую операцию. Python имеет многочисленные
# встроенные функции, которые выполняют различные операции. Возможно, самой фундаментальной встроенной функцией является
# функция печати print, которая показывает выходные данные на экране. Вот пример инструкции, которая исполняет функцию
# print:
print('Привет, мир!')
# Когда программисты исполняют функцию, они говорят, что вызывают функцию.

# Строковые данные и строковые литералы.
print('Строковые данные и строковые литералы')
# В программном коде Python строковые литералы должны быть заключены в знаки кавычек. Как отмечалось ранее, знаки
# кавычек просто отмечают, где строковые данные начинаются и заканчиваются. В Python можно заключать строковые литералы
# в одинарные кавычки (') либо двойные кавычки ("). Если требуется, чтобы строковый литерал содержал одинарную кавычку
# (апостроф), то можно заключить строковый литерал в двойные кавычки.
# Python позволяет заключать строковые литералы в тройные кавычки (""" либо '''). Строки, которые заключены в тройные
# кавычки, внутри могут содержать одинарные и двойные кавычки. Тройные кавычки используются для заключения многострочных
# строковых данных, для которых одинарные и двойные кавычки не могут применяться.


# Комментарии
print('Комментарии')
# Комментарии — это описательные пояснения, которые документируют строки программы или ее разделы. Комментарии являются
# частью программы, но интерпретатор Python их игнорирует. Они предназначены для людей, которые, возможно, будут читать
# исходный код.
# В Python комментарий начинается с символа решетки #. Когда интерпретатор Python видит символ #, он игнорирует все, что
# находится между этим символом и концом строки кода.
# В своем коде программисты чаще всего используют концевые комментарии. Концевой комментарий — это комментарий, который
# появляется в конце строки кода. Он обычно объясняет инструкцию, которая расположена в этой строке.


# Переменные
print('Переменные')
# Переменная — это имя, которое представляет место хранения в памяти компьютера.

# Создание переменных инструкцией присваивания.
# Инструкция присваивания используется для создания переменной, которая будет ссылаться на порцию данных.
# Инструкция присваивания записывается в приведенном ниже общем формате:
# переменная = выражение
# Знак "равно" (=) называется оператором присваивания. В данном формате переменная — это имя переменной, а выражение —
# значение либо любая порция программного кода, которая в результате дает значение. После исполнения инструкции
# присваивания переменная, заданная слева от оператора =, будет ссылаться на значение, заданное справа от оператора =.
age = 25
print(age)
width = 10
print(width)
length = 5
print(length)
# В инструкции присваивания переменная, получающая присваиваемое значение, должна стоять с левой стороны от оператора =.
# В программе в файле variable_demo.py демонстрируется переменная. Строка 2 создает переменную с именем room (комната) и
# присваивает ей значение 503. Инструкции в строках 3 и 4 выводят сообщения. Обратите внимание, что строка 4 выводит
# значение, на которое ссылается переменная room.
# В программе в файле variable_demo2.py приведен пример кода, в котором используются две переменные. Строка 2 создает
# переменную с именем top_speed (предельная скорость), присваивая ей значение 160. Строка 3 создает переменную с именем
# distance (расстояние), присваивая ее значение 300.
# Переменную нельзя использовать, пока ей не будет присвоено значение. Если попытаться выполнить операцию с переменной,
# например напечатать ее, до того, как ей будет присвоено значение, то произойдет ошибка.
# Переменные в Python работают иначе, чем переменные в большинстве других языков программирования. Там переменная — это
# ячейка памяти, которая содержит значение. В этих языках,когда вы присваиваете значение переменной, оно сохраняется в
# выделенной для этой переменной ячейке памяти.
# В Python переменная — это ячейка памяти, которая содержит адрес другой ячейки памяти. Когда вы присваиваете значение
# переменной в Python, это оно хранится в отдельном от переменной месте. Переменная будет содержать адрес ячейки, в
# которой хранится значение. Вот почему в Python вместо того, чтобы говорить, что переменная "содержит" значение, мы
# говорим, что переменная "ссылается" на переменную.

# Правила именования переменных.
# Хотя разрешается придумывать переменным свои имена, необходимо соблюдать правила.
# - В качестве имени переменной нельзя использовать одно из ключевых слов Python.
# - Имя переменной не может содержать пробелы.
# - Первый символ должен быть одной из букв от a до z, от A до Z либо символом подчеркивания (_).
# - После первого символа можно использовать буквы от a до z или от A до Z, цифры от 0 до 9 либо символы подчеркивания.
# - Символы верхнего и нижнего регистров различаются. Это означает, что имя переменной ItemsOrdered (ЗаказаноТоваров) не
# является тем же, что и itemsordered (заказанотоваров).
# В дополнение к соблюдению этих правил также всегда следует выбирать имена переменных, которые дают представление о
# том, для чего они используются.
# Примеры имен переменных:
# Имя переменной   Допустимое или недопустимое
# units_per_day    Допустимое.
# dayOfWeek        Допустимое.
# 3dGraph          Недопустимое. Имена переменных не могут начинаться с цифры.
# June1997         Допустимое.
# Mixture#3        Недопустимое. В именах переменных могут использоваться только буквы, цифры или символы подчеркивания.

# Вывод нескольких значений при помощи функции print.
# Python позволяет выводить несколько значений одним вызовом функции print. Мы просто должны отделить значения друг от
# друга запятыми, как показано в программе в файле variable_demo3.py.

# Повторное присваивание значений переменным.
# Переменные называются так потому, что во время работы программы они могут ссылаться на разные значения. Когда
# переменной присваивается значение, она будет ссылаться на это значение до тех пор, пока ей не будет присвоено другое
# значение. Например, в программе в файле variable_demo4.py инструкция в строке 3 создает переменную с именем roubles и
# присваивает ей значение 2.75. Затем инструкция в строке 8 присваивает переменной roubles другое значение — 99.95.
# Старое значение 2.75 по-прежнему находится в памяти компьютера, но оно больше не может использоваться, потому что на
# него переменная не ссылается. Когда переменная больше не ссылается на значение в памяти, интерпретатор Python
# автоматически его удаляет из памяти посредством процедуры, которая называется сборщиком мусора.

# Числовые типы данных и числовые литералы.
# Поскольку разные типы чисел хранятся и обрабатываются по-разному, в Python используются типы данных с целью
# классификации значений в оперативной памяти. Когда в оперативной памяти хранится целое число, оно классифицируется как
# int, а когда в памяти хранится вещественное число, оно классифицируется как float.
# Когда интерпретатор Python считывает числовой литерал в коде программы, он определяет его тип данных согласно
# следующим правилам:
# - числовой литерал, который записан в виде целого числа без десятичной точки, имеет целочисленный тип int, например 7,
# 124 и -9;
# - числовой литерал, который записан с десятичной точкой, имеет вещественный тип float, например 1.5, 3.14159 и 5.0.
# В числовых литералах запрещено использовать обозначения денежных единиц, пробелов или запятых.

# Хранение строковых данных с типом str.
# В дополнение к целочисленным типам данных int и вещественным типам данных float Python имеет тип данных str, который
# используется для хранения в оперативной памяти строковых данных. В программе в файлах string_variable.py показано, как
# строковые данные присваиваются переменным.

# Повторное присвоение переменной значения другого типа.
# Следует учитывать, что в Python переменная — это просто имя, которое ссылается на порцию данных в оперативной памяти.
# Этот механизм упрощает вам, программисту, хранение и получение данных. Интерпретатор Python отслеживает создаваемые
# вами имена переменных и порции данных, на которые эти имена переменных ссылаются. Всякий раз, когда необходимо
# получить одну из этих порций данных, просто используется имя переменной, которое на эту порцию ссылается.
# Переменная в Python может ссылаться на значения любого типа. После того как переменной присвоено значение одного типа,
# ей можно заново присвоить значение другого типа.


# 2.6 Чтение входных данных с клавиатуры
print('2.6 Чтение входных данных с клавиатуры')
# Программы должны уметь считывать входные данные, набираемые пользователем на клавиатуре. Для этих целей мы будем
# использовать функции Python.
# Функция input читает порцию данных, которая была введена с клавиатуры, и возвращает эту порцию данных в качестве
# строкового значения назад в программу. Функцию input обычно применяют в инструкции присваивания, которая соответствует
# приведенному ниже общему формату:
# переменная = input(подсказка)
# В данном формате подсказка — это строковый литерал, который выводится на экран. Его предназначение — дать пользователю
# указание ввести значение. А переменная — это имя переменной, которая ссылается на данные, введенные на клавиатуре.
# В программе в файле string_input.py представлен законченный код, который использует функцию input для чтения двух
# строковых значений с клавиатуры.
# Мы помещаем пробел в конец каждого строкового значения, потому что функция input не выводит пробел автоматически после
# подсказки. Когда пользователь начинает набирать символы, они появляются на экране сразу после подсказки. Добавление в
# конец подсказки символа пробела позволяет визуально отделять подсказку на экране от вводимых пользователем данных.

# Чтение чисел при помощи функции input.
# Функция input всегда возвращает введенные пользователем данные как строковые, даже если пользователь вводит числовые
# значения. Например, предположим, что вы вызываете функцию input, набираете число 72 и нажимаете клавишу <Enter>.
# Возвращенное из функции input значение будет строковым, '72'. Может возникнуть проблема, если вы захотите использовать
# это значение в математической операции. Математические операции могут выполняться только с числовыми значениями, а не
# строковыми.
# Функции преобразования данных
# Функция           Описание
# int(значение)     В функцию int() передается аргумент, и она возвращает значение аргумента, преобразованное в
#                   целочисленный тип int
# float(значение)   В функцию float() передается аргумент, и она возвращает значение аргумента, преобразованное в
#                   вещественный тип float
# В программе в файле input.py представлен законченный код, в котором используется функция input() для чтения значений
# строкового str, целочисленного int и вещественного float типов в качестве вводимых с клавиатуры данных.


# 2.7 Выполнение расчетов
print('2.7 Выполнение расчетов')
# Python имеет много операторов, которые используются для выполнения математических расчетов.
# Математические операторы Python
# Символ    Операция                Описание
# +         Сложение                Складывает два числа
# −         Вычитание               Вычитает одно число из другого
# *         Умножение               Умножает одно число на другое
# /         Деление                 Делит одно число на другое и выдает результат в качестве числа с плавающей точкой
# //        Целочисленное деление   Делит одно число на другое и выдает результат в качестве целого числа
# %         Остаток от деления      Делит одно число на другое и выдает остаток от деления
# **        Возведение в степень    Возводит число в степень
# Когда для вычисления значения используется математическое выражение, обычно мы хотим сохранить его результат в
# оперативной памяти, чтобы им снова можно было воспользоваться в программе. Это делается при помощи инструкции
# присваивания программа в файле simple_math.py.

# Вычисление процентов.
# Если вы пишете программу, которая работает с процентами, то прежде, чем выполнять любые математические расчеты с
# процентами, необходимо убедиться, что десятичная точка процентного значения находится в правильной позиции. Это в
# особенности верно в случае, когда пользователь вводит процентное значение в качестве входных данных.
# В программе в файле sale_price.py представлен весь код с примером вывода.

# Деление с плавающей точкой и целочисленное деление.
# Стоит отметить, что Python имеет два разных оператора деления. Оператор / выполняет деление с плавающей точкой,
# оператор // осуществляет целочисленное деление. Оба оператора делят одно число на другое. Разница между ними состоит в
# том, что оператор / выдает результат в качестве значения с плавающей точкой, а оператор // — результат в качестве
# целочисленного значения.
print(5 / 2)
print(5 // 2)
print(-5 // 2)

# Приоритет операторов.
# Ниже приведен приоритет математических операторов от самого высокого до самого низкого:
# 1. Возведение в степень: **.
# 2. Умножение, деление и остаток от деления: * / // %.
# 3. Сложение и вычитание: + −.
# Отметим, что операторы умножения (*), деления с плавающей точкой (/), целочисленного деления (//) и остатка от
# деления (%) имеют одинаковый приоритет. Операторы сложения (+) и вычитания (−) тоже имеют одинаковый приоритет. Когда
# два оператора с одинаковым приоритетом используют операнд совместно, они выполняются слева направо.
# Из правила вычисления слева направо есть исключение. Когда два оператора возведения в степень ** используют операнд
# совместно, операторы выполняются справа налево. Например, выражение 2 ** 3 ** 4 вычисляется как 2 ** (3 ** 4).
outcome = 12.0 + 6.0 / 3.0
print(outcome)

# Группирование при помощи круглых скобок.
# Части математического выражения можно группировать при помощи круглых скобок, чтобы заставить некоторые операции
# выполняться перед другими.

# Вычисление среднего арифметического значения.
# В программе в файле test_score_average.py представлен код.

# Оператор возведения в степень.
# В дополнение к элементарным математическим операторам сложения, вычитания, умножения и деления Python предоставляет
# оператор возведения в степень (**).
area = length ** 2
print(area)
print(4 ** 2)
print(5 ** 3)
print(2 ** 10)

# Оператор остатка от деления.
# В Python символ % является оператором остатка от деления. (Он также называется оператором деления по модулю.) Оператор
# остатка выполняет деление, но вместо того, чтобы вернуть частное, он возвращает остаток.
leftover = 17 % 3
print(leftover)
# Программа в файле time_converter.py получает от пользователя количество секунд и преобразует его в часы, минуты и
# секунды: 11 730 секунд в 3 часа 15 минут 30 секунд.

# Преобразование математических формул в программные инструкции.
# Из уроков алгебры вы, вероятно, помните, что выражение 2xy понимается как произведение 2 на x и на y. В математике
# оператор умножения не всегда используется. С другой стороны, Python, а также другие языки программирования, требует
# наличия оператора для любой математической операции.
# Алгебраические выражения:
# Алгебраическое выражение      Выполняемая операция        Программное выражение
# 6B                            Произведение 6 на B         6 * B
# 3 ⋅ 12                        Произведение 3 на 12        3 * 12
# 4xy                           Произведение 4 на x на y    4 * x * y
# Во время преобразования некоторых алгебраических выражений в программные выражения нередко приходится вставлять
# круглые скобки, которые отсутствуют в алгебраическом выражении.
# Алгебраические и программные выражения:
# Алгебраическое выражение      Инструкция на Python
# y = 3 * (x/2)                 y = 3 * x / 2
# z = 3bc + 4                   z = 3 * b * c + 4
# a = (x+2)/(b−1)               a = (x + 2) / (b - 1)

# Преобразование математической формулы в программную инструкцию.
# Программа в файле future_value.py демонстрирует этот алгоритм.

# Смешанные выражения и преобразование типов данных.
# Когда выполняется математическая операция с двумя операндами, тип данных результата будет зависеть от типа данных
# операндов. При вычислении математических выражений Python следует руководствоваться указанными ниже правилами.
# - Когда операция выполняется с двумя целочисленными значениями int, результатом будет int.
# - Когда операция выполняется с двумя вещественными значениями float, результатом будет float.
# - Когда операция выполняется с int и float, целочисленное значение int будет временно преобразовано в вещественное
# float, и результатом операции будет float. (Выражение, в котором используются операнды разных типов данных, называется
# смешанным выражением.)
my_number = 5 * 2.0
print(my_number)
fvalue = 2.6
print(fvalue)
ivalue = int(fvalue)  # Преобразование из типа float в тип int
print(ivalue)
fvalue = -2.9
print(fvalue)
ivalue = int(fvalue)  # Преобразование из типа float в тип int
print(ivalue)
ivalue = 2
print(ivalue)
fvalue = float(ivalue)  # Преобразование из типа int в тип float
print(fvalue)

# Разбиение длинных инструкций на несколько строк.
# Большинство программных инструкций пишут на одной строке. Однако если программная инструкция слишком длинная, то вы не
# сможете ее увидеть целиком в своем окне редактора, не используя горизонтальную прокрутку. Кроме того, если при
# распечатке программного кода на бумаге одна из инструкций окажется слишком длинной, чтобы уместиться на одной строке,
# то она продолжится на следующей строке и тем самым сделает ваш код неудобочитаемым.
# При помощи символа продолжения строки, в качестве которого используется обратная косая черта (\), Python позволяет
# разбивать инструкцию на несколько строк. Для этого просто нужно ввести символ обратной косой черты в точке, где
# следует прервать инструкцию, и затем нажать клавишу <Enter>.
# result = var1 * 2 + var2 * 3 + \
# var3 * 4 + var4 * 5
# Python позволяет разбивать на несколько строк любую часть инструкции, которая заключена в круглые скобки, не используя
# для этого символ продолжения строки.
# print("Продажи в понедельник составили", monday,
#       "во вторник они составили", tuesday,
#       "и в среду они составили", wednesday)
# Приведенный ниже фрагмент кода демонстрирует еще один пример:
# total = (value1 + value2 +
#           value3 + value4 +
#           value5 + value6)


# 2.8 Конкатенация строковых литералов
print('2.8 Конкатенация строковых литералов')
# Конкатенация строковых значений — это добавление одного строкового литерала в конец другого.
# Распространенной операцией, выполняемой на строковых литералах, является конкатенация, которая означает добавление
# одного строкового литерала в конец другого строкового литерала. В Python для конкатенирования строковых литералов
# применяют оператор +. Он создает строковый литерал, представляющий собой комбинацию двух строковых литералов,
# используемых в качестве его операндов.
message = 'Здравствуй, ' + 'мир'
print(message)
# Программа в файле concatenation.py демонстрирует конкатенацию строковых литералов подробнее.
# Конкатенация строковых литералов бывает полезной для разбиения строкового литерала, в результате чего длинный вызов
# функции print может охватывать несколько строк программы.

# Неявная конкатенация строковых литералов.
# Когда два или более строковых литерала записываются рядом друг с другом, разделенные только пробелами, символами
# табуляции или символами новой строки, Python неявно объединит их в строковый литерал.
my_str = 'один ' 'два ' 'три '
print(my_str)
print('Введите объем '
      'продаж за каждый день и '
      'нажмите Enter.')


# 2.9 Подробнее об инструкции print
print('2.9 Подробнее об инструкции print')

# Подавление концевого символа новой строки в функции print
# Функция print обычно показывает одну строку вывода.
print('Один')
print('Два')
print('Три')
# Каждая показанная выше инструкция выводит строковое значение и затем печатает символ новой строки. Сам символ новой
# строки вы не увидите, но когда он выводится на экран, данные выводятся со следующей строки.
# Если потребуется, чтобы функция print не начинала новую строку, когда заканчивает выводить на экран свои выходные
# данные, то в эту функцию можно передать специальный аргумент end=' ':
print('Один', end=' ')
print('Два', end=' ')
print('Три')
# Обратите внимание, что в первых двух инструкциях в функцию print передается аргумент end=' '. Он говорит о том, что
# вместо символа новой строки функция print должна в конце своих выводимых данных напечатать пробел.
# Иногда, возможно, потребуется, чтобы функция print в конце своих выводимых данных ничего не печатала, даже пробел.
# В этом случае в функцию print можно передать аргумент end='':
print('Один', end='')
print('Два', end='')
print('Три')
# Отметим, что в аргументе end='' между кавычками нет пробела. Он указывает на то, что в конце выводимых данных функции
# print ничего печатать не нужно.

# Задание символа-разделителя значений.
# Когда в функцию print передается много аргументов, они автоматически отделяются друг от друга пробелом при их выводе.
print('Один', 'Два', 'Три')
# Если потребуется, чтобы между значениями не печатался пробел, то в функцию print можно передать аргумент sep='':
print('Один', 'Два', 'Три', sep='')
# Этот специальный аргумент также можно применить, чтобы определить, какой именно символ будет разделять несколько
# значений:
print('Один', 'Два', 'Три', sep='*')
print('Один', 'Два', 'Три', sep='~~~')

# Экранированные символы
# Экранированный символ — это специальный символ в строковом литерале, которому предшествует обратная косая черта (\).
# Во время печати строкового литерала с экранированными символами (или экранированными последовательностями) они
# рассматриваются как специальные команды, которые встроены в строковый литерал.
# Например, \n — это экранированная последовательность новой строки. При ее печати она на экран не выводится. Вместо
# этого она переводит позицию печати на следующую строку.
print('Один\nДва\nТри')
# Некоторые экранированные последовательности Python
# Экранированная последовательность       Результат
# \n                                      Переводит позицию печати на следующую строку
# \t                                      Переводит позицию печати на следующую горизонтальную позицию табуляции
# \'                                      Печатает одинарную кавычку
# \"                                      Печатает двойную кавычку
# \\                                      Печатает обратную косую черту
print('Пн\tВт\tСр')
print('Чт\tПт\tСб')


# 2.10 Вывод на экран форматированного результата с помощью f-строк
print('2.10 Вывод на экран форматированного результата с помощью f-строк')
# F-строка — это особый тип строкового литерала, который позволяет форматировать значения различными способами.
# F-строки, или отформатированные строковые литералы, предоставляют простой способ отформатировать результат, который
# вы хотите показать на экране с помощью функции print. С помощью f-строки можно создавать сообщения, содержащие
# значения переменных, и форматировать числа различными способами.
# F-cтрока — это строковый литерал, заключенный в кавычки и снабженный префиксом, состоящим из буквы f.
print(f'Здравствуй, мир')
# Однако f-строки намного мощнее обычных строковых литералов. F-строка может содержать местозаполнители для переменных и
# других выражений.
name = 'Джонни'
print(f'Привет, {name}.')
# В первой инструкции мы присваиваем 'Джонни' переменной name. Во второй инструкции передаем f-строку функции print.
# Внутри f-строки {name} является местозаполнителем для переменной name. При выполнении инструкции местозаполнитель
# заменяется значением переменной name. В результате инструкция печатает 'Привет, Джонни'.
temperature = 45
print(f'Сейчас {temperature} градусов.')

# Выражения-местозаполнители.
# В предыдущих примерах f-строк мы использовали местозаполнители для вывода значений переменных на экран. В дополнение к
# именам переменных местозаполнители могут содержать любое допустимое выражение.
print(f' Значение равно {10 + 2}.')
val = 10
print(f'Значение равно {val + 2}.')

# Форматирование значений.
# Заполнители в f-строке могут содержать спецификатор формата, который приводит к форматированию значения
# местозаполнителя при его выводе на экран. Например, с помощью спецификатора формата можно округлять значения до
# заданного числа десятичных знаков и показывать числа с разделителями. Кроме того, с помощью спецификатора формата
# можно выравнивать значения по левому или правому краю либо по центру. На самом деле, вы можете использовать
# спецификаторы формата для управления многими способами вывода значений на экран.
# Вот общий формат для написания местозаполнителя со спецификатором формата:
# {местозаполнитель:спецификатор формата}
# Обратите внимание, что в общем формате местозаполнитель и спецификатор формата разделены двоеточием.

# Округление чисел с плавающей точкой.
# Возможно, вы не всегда будете довольны тем, как числа с плавающей точкой отображаются на экране. Когда функция print
# выводит число с плавающей точкой на экран, оно может содержать до 17 значащих цифр. Это показано в выводе программы
# в файле f_string_no_formatting.py.
# Поскольку эта программа выводит на экран денежную сумму, было бы неплохо, чтобы эта сумма была округлена до двух
# знаков после точки. Мы можем сделать это с помощью следующего спецификатора формата:
# .2f
# В спецификаторе формата .2 — это условное обозначение степени точности, указывающее на то, что число должно быть
# округлено до двух знаков после точки. Буква f является условным обозначением типа и указывает на то, что значение
# должно выводиться с фиксированным числом цифр после десятичной точки. Когда мы добавим этот спецификатор формата в
# местозаполнитель в строке 5 программы, он будет выглядеть следующим образом:
# {monthly_payment:.2f}
# Это приведет к тому, что значение переменной monthly_payment будет выводиться на экран как 416.67. Программа в файле
# f_string_rounding.py это демонстрирует.
pi = 3.1415926535
print(f'{pi:.3f}')
a = 2
b = 3
print(f'{a / b:.1f}')
# Условное обозначение типа с фиксированной точкой можно писать в нижнем регистре (f) либо в верхнем регистре (F).

# Вставка запятых в качестве разделителя.
# Вы можете использовать спецификатор формата для вставки запятых в число:
number = 1234567890.12345
print(f'{number:,}')
# А вот пример того, как можно объединить спецификаторы формата, чтобы одновременно округлять число и вставлять запятые
# в качестве разделителей:
number = 1234567890.12345
print(f'{number:,.2f}')
# В спецификаторе формата запятую нужно записывать перед (слева) условным обозначением точности. В противном случае при
# исполнении программного кода возникнет ошибка. Программа в файле dollar_display.py демонстрирует использование запятой
# как разделителя и точность до двух знаков после точки для форматирования числа в качестве суммы в валюте (или в
# денежном эквиваленте).

# Форматирование числа с плавающей точкой в процентах.
# Вместо того чтобы использовать символ f в качестве условного обозначения типа, можно указывать символ % для
# процентного форматирования числа с плавающей точкой. Символ % приводит к тому, что число умножается на 100 и выводится
# на экран со знаком % после него.
discount = 0.5
print(f'{discount:%}')  # Без округления
discount = 0.7
print(f'{discount:.2%}')  # Округление до двух знаков
discount = 0.7
print(f'{discount:.0%}')  # Округление до ноля знаков

# Форматирование в научной нотации.
# Если вы предпочитаете выводить на экран числа с плавающей точкой в научной нотации, то вместо f можете использовать
# букву e или E.
number = 12345.6789
print(f'{number:e}')
print(f'{number:.2e}')
# Первая инструкция просто форматирует число в научной нотации. Число выводится на экран с буквой e, обозначающей
# показатель степени. (Если в спецификаторе формата вы используете E в верхнем регистре, то результат будет содержать E
# в верхнем регистре.) Во второй инструкции дополнительно указывается точность в два знака после точки.

# Форматирование целых чисел.
# При написании спецификатора формата, который будет применяться для форматирования целого числа, следует иметь в виду
# две особенности.
# - Когда вам нужно использовать условное обозначение типа, следует записывать d или D. Эти буквы сообщают о том, что
# значение должно выводиться на экран в виде целого числа.
# - Условное обозначение точности вообще не используется.
number = 123456
print(f'{number:d}')
print(f'{number:,d}')

# Указание минимальной ширины поля.
# Спецификатор формата может также содержать минимальную ширину поля, т. е. минимальное число знаков, которые следует
# отвести для вывода значения на экран.
number = 99
print(f'Число равняется {number:10}')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


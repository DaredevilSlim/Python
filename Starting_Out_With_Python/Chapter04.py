#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 4 Структуры с повторением
print('4 Структуры с повторением')
# 4.1 Введение в структуры повторения
print('4.1 Введение в структуры повторения')
# Структура с повторением исполняет инструкции или набор инструкций многократно.

# Циклы с условием повторения и со счетчиком повторений.
# Цикл с условием повторений использует логическое условие со значениями истина/ложь, которое управляет количеством
# повторов цикла. Цикл со счетчиком повторений повторяется заданное количество раз. Для написания цикла с условием
# повторения в Python применяется инструкция while, для написания цикла со счетчиком повторений — инструкция for.


# 4.2 Цикл while: цикл c условием повторения
print('4.2 Цикл while: цикл c условием повторения')
# Цикл с условием повторения исполняет инструкции или набор инструкций повторно до тех пор, пока условие является
# истинным. В Python для написания цикла c условием повторения применяется инструкция while.
# Цикл while ("пока") получил свое название из-за характера своей работы: он выполняет некую задачу до тех пор, пока
# условие является истинным. Данный цикл имеет две части: условие, которое проверяется на истинность либо ложность, и
# инструкцию или набор инструкций, которые повторяются до тех пор, пока условие является истинным.
# Вот общий формат цикла с условием повторения в Python:
# while условие:
#   инструкция
#   инструкция
#   ...
# При исполнении цикла while проверяется условие. Если условие является истинным, то исполняются инструкции, которые
# расположены в блоке после выражения while, и цикл начинается сначала. Если условие является ложным, то программа
# выходит из цикла. В программе в файле commission.py показано, как можно применить цикл while для написания программы
# расчета комиссионного вознаграждения.

# Цикл while как цикл с предусловием.
# Цикл while также называется циклом с предусловием, а именно он проверяет свое условие до того, как сделает итерацию.
# Поскольку проверка осуществляется в начале цикла, обычно нужно выполнить несколько шагов перед началом цикла, чтобы
# гарантировать, что цикл выполнится как минимум однажды.
# Важная особенность цикла while: он никогда не исполнится, если его условие с самого начала будет ложным.

# Проектирование программы с циклом while.
# Проект, который в настоящее время осуществляется в компании "Химическая аналитика", требует, чтобы вещество в баке
# непрерывно поддерживалось в нагретом состоянии. Лаборант должен проверять температуру вещества каждые 15 мин. Если
# температура вещества не превышает 102,5 °C, лаборант ничего не делает. Однако если температура больше 102,5 °C, то он
# должен убавить нагрев с помощью термостата, подождать 5 минут и проверить температуру снова. Лаборант повторяет эти
# шаги до тех пор, пока температура не превысит 102,5 °C. Директор по разработке попросил вас написать программу,
# которая будет помогать лаборанту проходить этот процесс.
# Вот алгоритм:
# 1. Получить температуру вещества.
# 2. Повторять приведенные ниже шаги до тех пор, пока температура больше 102,5 °С:
# а) дать указание лаборанту убавить нагрев, подождать 5 минут и проверить температуру снова;
# б) получить температуру вещества.
# 3. После завершения цикла сообщить лаборанту, что температура приемлема, и проверить ее снова через 15 минут.
# Изучив этот алгоритм, вы понимаете, что шаги 2а и 2б не будут выполняться, если проверяемое условие (температура
# больше 102,5 °С) является ложным с самого начала. В этой ситуации цикл while сработает хорошо, потому что он не
# выполнится ни разу, если его условие будет ложным. В программе в файле temperature.py представлен соответствующий код.

# Бесконечные циклы.
# Всегда, кроме редких случаев, циклы должны содержать возможность завершиться. То есть в цикле что-то должно сделать
# проверяемое условие ложным. Если цикл не имеет возможности завершиться, он называется бесконечным циклом. Бесконечный
# цикл продолжает повторяться до тех пор, пока программа не будет прервана. Бесконечные циклы обычно появляются, когда
# программист забывает написать программный код внутри цикла, который делает проверяемое условие ложным. В большинстве
# случаев вам следует избегать применения бесконечных циклов.
# Программа в файле infinite.py демонстрирует бесконечный цикл.


# 4.3 Цикл for: цикл со счетчиком повторений
print('4.3 Цикл for: цикл со счетчиком повторений')
# Цикл со счетчиком повторений повторяется заданное количество раз. В Python для написания цикла со счетчиком повторений
# применяется инструкция for.
# Как упомянуто в начале этой главы, цикл со счетчиком повторений повторяется заданное количество раз. Циклы со
# счетчиком повторений находят широкое применение в программах.
# Для написания цикла со счетчиком повторений применяется инструкция for. В Python инструкция for предназначена для
# работы с последовательностью значений данных. Когда эта инструкция исполняется, она повторно выполняется для каждого
# значения последовательности. Вот ее общий формат:
# for переменная in [значение1, значение2, ...]:
#   инструкция
#   инструкция
#   ...
# В программе в файле simple_loop1.py приведен пример, в котором цикл for применяется для вывода чисел от 1 до 5.
# Например, в программе в файле simple_loop2.py применяется цикл for для вывода списка нечетных чисел. В списке всего
# пять чисел, и поэтому цикл повторяется пять раз, т. е. делает пять итераций.
# В программе в файле simple_loop3.py приведен еще один пример. Здесь цикл for выполняет последовательный обход списка
# строковых значений. Обратите внимание, что список (в строке 4) содержит три строковых значения: 'Мигнуть', 'Моргнуть'
# и 'Кивнуть'. В результате цикл сделает три итерации.

# Применение функции range с циклом for.
# Python предоставляет встроенную функцию range (диапазон), которая упрощает процесс написания цикла со счетчиком
# повторений. Функция range создает тип объекта, который называется итерируемым, т. е. пригодным для итеративной
# обработки в цикле. Итерируемый объект аналогичен списку. Он содержит последовательность значений, которые можно по
# порядку обойти на основе чего-то наподобие цикла.
# В программе в файле simple_loop4.py применяется функция range с циклом for для пятикратного вывода сообщения "Привет,
# мир!".
# Если передать функции range один аргумент, то этот аргумент используется в качестве конечного предела
# последовательности чисел. Если передать функции range два аргумента, то первый аргумент используется в качестве
# начального значения последовательности, второй аргумент — в качестве ее конечного предела.
# По умолчанию функция range создает последовательность чисел, которая увеличивается на 1 для каждого последующего числа
# в списке. Если передать функции range третий аргумент, то этот аргумент используется в качестве величины шага. Вместо
# увеличения на 1, каждое последующее число в последовательности увеличится на величину шага.

# Использование целевой переменной в цикле.
# В цикле for целевая переменная предназначена для того, чтобы ссылаться на каждое значение последовательности значений
# в ходе выполнения итераций цикла. Во многих ситуациях целесообразно использовать целевую переменную в расчетах или
# другой задаче внутри тела цикла.

# Проектирование цикла со счетчиком повторений на основе инструкции for.
# Ваша подруга Аманда только что получила в наследство европейский спортивный автомобиль от своего дяди. Аманда живет в
# США и боится, что будет оштрафована за превышение скорости, потому что спидометр автомобиля показывает скорость в
# километрах в час. Она попросила вас написать программу, которая выводит таблицу скоростей, где эти значения
# преобразованы в мили в час. Формула для преобразования KPH (kilometers per hour) в MPH (miles per hour):
# MPH = KPH × 0.6214.
# В данной формуле MPH — это скорость в милях в час, KPH — скорость в километрах в час. Таблица, которую ваша программа
# выводит, должна показать скорости от 60 до 130 км/ч с приращением 10 км вместе с их значениями, преобразованными в
# мили в час. В программе в файле speed_converter.py показан соответствующий код.

# Пользовательский контроль итераций цикла.
# В программе в файле user_squares2.py приведен пример, который разрешает пользователю определять начальное значение и
# конечный предел последовательности.

# Порождение итерируемой последовательности в диапазоне от максимального до минимального значения.
# В рассмотренных примерах функция range применялась для создания последовательности с числами, которые проходят от
# минимального до максимального значения. Как альтернативный вариант, функцию range можно применить для создания
# последовательностей чисел, которые проходят в обратном порядке от максимального до минимального значения.


# 4.4 Вычисление нарастающего итога
print('4.4 Вычисление нарастающего итога')
# Нарастающий итог — это сумма чисел, которая накапливается с каждой итерацией цикла.
# Переменная, которая используется для хранения нарастающего итога, называется накопителем.
# Программа в файле sum_numbers.py позволяет пользователю ввести пять чисел и выводит сумму введенных чисел.

# Расширенные операторы присваивания.
# Оператор  Пример использования    Эквивалент
# +=        x += 5                  x = x + 5
# -=        y -= 2                  y = y - 2
# *=        z *= 10                 z = z * 10
# /=        a /= b                  a = a / b
# %=        c %= 3                  c = c % 3
# //=       x //= 3                 x = x // 3
# **=       y **= 2                 y = y**2


# 4.5 Сигнальные метки
print('4.5 Сигнальные метки')
# Сигнальная метка — это специальное значение, которое отмечает конец последовательности значений.
# При обработке длинной последовательности значений при помощи цикла, вероятно, оптимальный прием состоит в
# использовании сигнальной метки. Сигнальная метка — это специальное значение, которое отмечает конец последовательности
# значений. Когда программа читает значение сигнальной метки, она знает, что достигла конца последовательности, и по
# этому цикл завершается.

# Применение сигнальной метки.
# Налоговая служба муниципального округа рассчитывает ежегодные налоги на имущество с использованием приведенной ниже
# формулы: налог на имущество = стоимость имущества × 0.0065.
# Каждый день сотрудник налоговой службы получает список имущественных объектов и должен вычислить налог для каждого
# объекта в списке. Вас попросили разработать программу, которую сотрудник сможет использовать для выполнения этих
# расчетов. В интервью с налоговым инспектором вы узнаете, что каждому имущественному объекту присваивается номер лота,
# и все номера лотов равны или больше 1. Вы решаете написать цикл, который использует в качестве значения сигнальной
# метки число 0. Во время каждой итерации цикла программа будет предлагать сотруднику ввести номер лота либо 0 для
# завершения. Соответствующий код показан в программе в файле property_tax.py.


# 4.6 Циклы валидации входных данных
print('4.6 Циклы валидации входных данных')
# Валидация входных данных — это процесс обследования данных, введенных в программу, с целью убедиться в их
# допустимости, прежде чем они будут использованы в вычислениях. Валидация входных данных обычно выполняется при помощи
# цикла, который повторяется до тех пор, пока входная переменная ссылается на плохие данные.
# Цикл валидации входных данных иногда называется ловушкой ошибок или обработчиком ошибок.

# Написание цикла валидации входных данных.
# Саманта владеет предприятием, которое занимается импортом, и она вычисляет розничные цены своих товаров при помощи
# приведенной ниже формулы:
# розничная цена = оптовая стоимость × 2.5.
# Для вычисления розничных цен она в настоящее время использует код, который представлен в программе в файле
# retail_no_validation.py.
# Вы решаете добавить в программу цикл валидации входных данных, который отклоняет любые отрицательные числа, которые
# вводятся в переменную wholesale. Программа в файле retail_with_validation.py иллюстрирует пересмотренный код с новым
# программным кодом валидации входных данных.


# 4.7 Вложенные циклы
print('4.7 Вложенные циклы')
# Цикл, который расположен внутри еще одного цикла, называется вложенным циклом.
# Вложенный цикл — это цикл, который расположен в еще одном цикле.

# Применение вложенных циклов для печати комбинаций символов.
# Один интересный способ узнать о вложенных циклах состоит в их использовании для вывода на экран комбинаций символов.
# Легко можно написать программу, которая предлагает пользователю ввести количество строк и столбцов, как показано в
# программе в файле rectangular_pattern.py.


# 4.8 Черепашья графика: применение циклов для рисования узоров
print('4.8 Черепашья графика: применение циклов для рисования узоров')
# Циклы можно применять для рисования графических изображений, которые различаются по сложности от простых фигур до
# изощренных узоров.
# Циклы с черепахой применяются для рисования как простых фигур, так и довольно сложных узоров. Например, приведенный
# ниже цикл for делает четыре итерации, чтобы нарисовать квадрат шириной 100 пикселов:
# for x in range(4):
#   turtle.forward(100)
#   turtle.right(90)
# А здесь цикл for делает восемь итераций, чтобы нарисовать восьмиугольник:
# for x in range(8):
#   turtle.forward(100)
#   turtle.right(45)
# В программе в файле concentric_circles.py приведен пример, в котором применяется цикл для рисования концентрических
# кругов.
# Программа в файле spiral_lines.py демонстрирует еще один пример. Она рисует последовательность 36 прямых линий для
# создания узора.

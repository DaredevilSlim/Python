#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Глава 2
# Обработка и формирование строк
print('Обработка и формирование строк')


# 2.1. КАК ИСПОЛЬЗОВАТЬ F-СТРОКИ ДЛЯ ИНТЕРПОЛЯЦИИ И ФОРМАТИРОВАНИЯ
print('2.1. КАК ИСПОЛЬЗОВАТЬ F-СТРОКИ ДЛЯ ИНТЕРПОЛЯЦИИ И ФОРМАТИРОВАНИЯ')


# 2.1.1. Форматирование строк до появления f-строк
print('2.1.1. Форматирование строк до появления f-строк')
# Класс str работает с текстовыми данными через свои экземпляры, которые мы будем называть строковыми переменными.
# Помимо строковых переменных, в текстовую информацию также часто включаются такие типы данных, как целые числа и числа
# с плавающей точкой. Теоретически мы могли бы преобразовать нестроковые данные в строки и соединить их для получения
# нужного текстового вывода, как показано в листинге test_0001.py.
# Методами обычно называются функции, определяемые в классах. В данном случае функция format определяется в классе str,
# поэтому этот метод вызывается для экземпляров str.


# 2.1.2. Использование f-строк для интерполяции переменных
print('2.1.2. Использование f-строк для интерполяции переменных')
# Форматирование строк часто подразумевает объединение строковых литералов и переменных разных типов (например, целых
# чисел и строк). При интеграции переменных в f-строку можно интерполировать эти переменные, чтобы они автоматически
# преобразовывались в строки нужного вида.
# Для начала рассмотрим, как использовать f-строки при создании вывода, представленного в листинге 2.1 (test_0001.py).
name = 'Homework'
urgency = 5
task_f = f'Name: {name}; Urgency Level: {urgency}'
assert task_f == 'Name: Homework; Urgency Level: 5'
# В этом примере переменная task_f создается с применением f-строк. Главное, на что следует обратить внимание, —
# фигурные скобки, в которые заключаются интерполируемые переменные. Так как f-строки интегрируют механизм строковой
# интерполяции, они также называются интерполируемыми строковыми литералами.
# Термин «строковая интерполяция» (string interpolation) не относится к специфике Python, этот механизм присутствует
# в большинстве основных современных языков (таких, как JavaScript, Swift и C#). В общем случае он предоставляет более
# компактный и удобочитаемый синтаксис для создания отформатированных строк, чем конкатенация строк и альтернативные
# способы их форматирования.
# Инструкция assert
# Ключевое слово Python assert используется для проверок (ассертов), которые вычисляют заданное условие. Если результат
# равен True, программа продолжает выполняться. Если же результат равен False, выполнение прерывается, а программа
# выдает ошибку AssertionError.
tasks = ['homework', 'laundry']
assert f'Tasks: {tasks}' == "Tasks: ['homework', 'laundry']"  # Интерполирует объект списка
task_hwk = ('Homework', 'Complete physics work')
assert f'Task: {task_hwk}' == "Task: ('Homework', 'Complete physics work')"  # Интерполирует объект кортежа
task = {'name': 'Laundry', 'urgency': 3}
assert f'Task: {task}' == "Task: {'name': 'Laundry', 'urgency': 3}"  # Интерполирует объект словаря


# 2.1.3. Использование f-строк для интерполяции выражений
print('2.1.3. Использование f-строк для интерполяции выражений')
# На более общем уровне f-строки также могут интерполировать выражения, что избавляет вас от необходимости создания
# промежуточных переменных. Например, при создании строкового вывода можно обратиться к элементу объекта dict или
# использовать результат вызова функции. В таких распространенных ситуациях можно включить эти выражения в f-строки, как
# показывает следующий фрагмент кода:
tasks = ["homework", "laundry", "grocery shopping"]
assert f"First Task: {tasks[0]}" == 'First Task: homework'  # Обращается к элементу списка
task_name = "grocery shopping"
assert f"Task Name: {task_name.title()}" == 'Task Name: Grocery Shopping'  # Вызывает функцию
number = 5
assert f"Square: {number * number}" == 'Square: 25'  # Прямые вычисления
# Эти выражения заключаются в фигурные скобки, чтобы f-строки напрямую вычислили их для получения нужного строкового
# вывода: {tasks[0]} -> "homework";
# {task_name.title()} -> "Grocery Shopping";
# {number * number} -> 25.
# В тексте часто встречается термин «выражение» (expression), относящийся к числу ключевых понятий программирования.
# Начинающие программисты могут путать его со связанным понятием — инструкцией (statement). Выражение обычно
# представляет собой одну строку кода (хотя может занимать несколько строк при заключении в тройные кавычки),
# результатом вычисления которой является значение объекта, например строки или экземпляра нестандартного класса. Из
# этого определения легко выводится, что переменные являются разновидностями выражений.
# С другой стороны, инструкции не создают никакого значения или объекта. Цель инструкции заключается в выполнении
# некоторого действия. Например, ключевое слово assert создает проверочную инструкцию (или команду), которая проверяет
# выполнение некоторого условия, прежде чем процесс продолжится. Мы не пытаемся получить логическое значение True или
# False, а проверяем условие.
# Различия между выражениями и инструкциями. Выражения представляют некие вычисления, в результате которых получается
# значение или объект, тогда как инструкция выполняет конкретные действия и не может вычисляться для получения значения.
# Хотя f-строки поддерживают интерполяцию выражений, эту возможность следует использовать с осторожностью, потому что
# любые сложные выражения в f-строках ухудшают читаемость вашего кода. Следующий пример демонстрирует злоупотребление
# f-строками, использующими сложные выражения:
summary_text = f'Your Average Score: {sum([95, 98, 97, 96, 97, 93]) / len([95, 98, 97, 96, 97, 93])}.'
print(summary_text)
# Существует хороший практический критерий оценки удобочитаемости вашего кода — определите, сколько времени потребуется
# читателю, чтобы разобраться в нем. Чтобы понять, что происходит в приведенном выше фрагменте, читателю понадобятся
# десятки секунд. Сравните со следующей переработанной версией:
scores = [95, 98, 97, 96, 97, 93]
total_score = sum(scores)
subject_count = len(scores)
average_score = total_score / subject_count
summary_text = f'Your Average Score: {average_score}.'
print(summary_text)
# В этой версии заслуживает внимания ряд обстоятельств. Во-первых, оценки сохраняются в объекте list, что позволяет
# избавиться от дублирования данных. Во-вторых, вычисления разбиты на несколько шагов, при этом каждый шаг представляет
# собой более простое вычисление. В-третьих, ключевым фактором для улучшения удобочитаемости становится использование на
# каждом шаге содержательного имени, обозначающего результат вычислений. Такой код хорошо читается без единого
# комментария, все понятно само по себе.
# Создайте необходимые промежуточные переменные с содержательными именами, чтобы наглядно обозначить каждый шаг ваших
# операций. Для простых операций вам даже не придется писать комментарии, потому что содержательные имена описывают
# смысл каждой операции.


# 2.1.4. Применение спецификаторов для форматирования f-строк
print('2.1.4. Применение спецификаторов для форматирования f-строк')
# Так как f-строки проектировались для форматирования строк, они предоставляют возможность задать спецификатор формата
# (начинающийся с двоеточия) для применения дополнительных правил форматирования к выражению в фигурных скобках.
# При интерполяции можно воспользоваться спецификатором формата — необязательным компонентом, который определяет, как
# должна форматироваться интерполированная строка выражения. F-строка может получать разные виды спецификаторов формата.

# Выравнивание строк для формирования визуальной структуры
# Для выравнивания текста в f-строках используются три символа: <, > и ^, включающие выравнивание текста по левому краю,
# по правому краю и по центру соответственно.
# Для определения режима выравнивания текста в спецификаторе формата используется синтаксис f"{expr:x<n}", где
# expr — интерполированное выражение, x — символ-заполнитель для выравнивания (если не указан, по умолчанию используется
# пробел), < — признак выравнивания по левому краю и n — целочисленный интервал, до которого расширяется вывод.
# Листинг 2.2 (test_0002.py) показывает, как создать две записи с выровненными полями для получения более наглядного
# вывода. В листинге 2.3 (test_0003.py) приведено возможное решение, в котором выделяется повторяющаяся
# часть — спецификатор формата. Для заполнения в приведенном примере используются пробелы, но можно использовать и
# другие символы.
task = "homework"
print(f'{task:*>10}')  # Выравнивание по правому краю, заполнитель *
print(f'{task:*<10}')  # Выравнивание по левому краю, заполнитель *
print(f'{task:*^10}')  # Выравнивание по центру, заполнитель *
print(f'{task:^10}')  # Выравнивание по центру, заполнитель — пробел

# Форматирование чисел
# Числа — неотъемлемые источники информации, которые часто включаются в текстовый материал. Существуют различные формы
# числовых значений: большие целые числа, числа с плавающей точкой, проценты и т. д.
# Множество простых чисел бесконечно. Обычный поиск в Google показывает, что наименьшее простое число, превышающее 1
# миллиард, равно 1 000 000 007. При выводе такого большого числа желательно разделять группы цифр, и чаще всего после
# каждых трех цифр вставляется запятая. Для назначения разделителей групп разрядов в целых числах в f-строке
# используется спецификатор формата xd, где x — разделитель, а d — спецификатор формата для целых чисел:
large_prime_number = 1000000007
print(f'Use commas: {large_prime_number:,d}')
# Числа с плавающей точкой, как и дробные числа вообще, встречаются почти в каждом научном или инженерном отчете. Как и
# следовало ожидать, у f-строк существуют спецификаторы формата, которые позволяют форматировать дробные числа в
# удобочитаемом виде.
decimal_number = 1.23456
print(f'Two digits: {decimal_number:.2f}')
print(f'Four digits: {decimal_number:.4f}')
# Если для целых чисел использовался спецификатор формата d, то для дробных значений используется спецификатор f. Хотя
# спецификатор f может использоваться автономно, чаще указывается, сколько цифр должно выводиться в дробной части:
# .2 для вывода двух цифр, .4 — для четырех цифр, и т. д.
# По аналогии с использованием f для дробных чисел, можно воспользоваться спецификатором формата e для экспоненциальной
# (научной) записи.
sci_number = 0.00000000412733
print(f'Sci notation: {sci_number:e}')
print(f'Sci notation: {sci_number:.2e}')
# Другая распространенная форма числовых значений — проценты. При выводе процентов используется спецификатор формата %.
# Как и в случае со спецификаторами e и f, мы можем использовать спецификатор % сам по себе или с указанием точности
# (например, .2 для вывода двух знаков в дробной части):
pct_number = 0.179323
print(f'Percentage: {pct_number:%}')
print(f'Percentage two digits: {pct_number:.2%}')
# Популярные спецификаторы при форматировании чисел с использованием f-строк
number = 15
point = 1.2345
# Целые числа:
print(f'{number:b}')  # Двоичный формат (запись по основанию 2)
print(f'{number:c}')  # Представление целого числа в Юникоде
print(f'{number:d}')  # Десятичный формат (запись по основанию 10)
print(f'{number:o}')  # Восьмеричный формат (запись по основанию 8)
print(f'{number:x}')  # Шестнадцатеричный формат (запись по основанию 16)
# Числа с плавающей точкой:
print(f'{point:.2e}')  # Научная запись
print(f'{point:.2f}')  # Запись с фиксированной точкой и двумя цифрами в дробной части
print(f'{point:.2g}')  # Общий формат с автоматическим применением e или f
print(f'{point:.2%}')  # Проценты с точностью 2 знака


# 2.1.5. Обсуждение
print('2.1.5. Обсуждение')
# Хотя с прямой интерполяцией выражений f-строками код становится более чистым, избегайте использования сложных
# выражений в f-строках — они могут запутать читателей вашего кода. Если выражения слишком сложные, создайте
# промежуточные переменные с содержательными именами. В Python все еще поддерживаются традиционные способы в стиле C и
# с использованием format, но реальной необходимости в их изучении нет (впрочем, они могут встретиться вам в старом
# коде). Каждый раз, когда вам потребуется создать строковый вывод, используйте f-строки. И не забывайте о выравнивании
# текста и форматировании числовых значений — это сделает текстовый вывод более понятным.


# 2.1.6. Задача
print('2.1.6. Задача')
# Джеймс работает в IT-отделе компании оптовой торговли и готовит шаблон для ценников. Допустим, данные товара
# сохраняются в объекте dict: {'name': 'Vacuum', 'price': 130.675}. Как Джеймсу записать f-строку, если нужно, чтобы в
# ценнике выводилась строка Vacuum: {130.68}? Обратите внимание: цена должна выводиться с точностью до двух знаков, а
# вывод включает фигурные скобки — символы, используемые для строковой интерполяции в f-строках.
# ПОДСКАЗКА Фигурные скобки являются специальными символами в f-строках. Если строковый литерал включает специальные
# символы, необходимо экранировать их, чтобы они не рассматривались как специальные символы. Для экранирования фигурных
# скобок включите дополнительную фигурную скобку: {{ означает {, а }} означает }.
template = {'name': 'Vacuum', 'price': 130.675}
print(f'{template['name']}: {{{template['price']}}}')


# 2.2. КАК ПРЕОБРАЗОВАТЬ СТРОКИ ДЛЯ ПОЛУЧЕНИЯ ПРЕДСТАВЛЯЕМЫХ ДАННЫХ
print('2.2. КАК ПРЕОБРАЗОВАТЬ СТРОКИ ДЛЯ ПОЛУЧЕНИЯ ПРЕДСТАВЛЯЕМЫХ ДАННЫХ')
# Хотя внешне строки являются текстовыми данными, фактически они могут представлять целые числа, словари и другие типы
# данных. Например, встроенная функция input предоставляет простейший способ получения пользовательского ввода с консоли
# Python:
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



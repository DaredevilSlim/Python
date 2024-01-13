#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 5 Функции
print('5 Функции')
# 5.1 Введение в функции
print('5.1 Введение в функции')
# Функция — это группа инструкций, которая существует внутри программы с целью выполнения определенной задачи.
# Вместо того чтобы писать большую программу как одну длинную последовательность инструкций, программист создает
# несколько небольших функций, каждая из которых выполняет определенную часть задачи. Эти небольшие функции затем могут
# быть исполнены в нужном порядке для выполнения общей задачи.

# Преимущества модуляризации программы на основе функций.
# В результате разбиения программы на функции она получает следующие преимущества.
# - Более простой код. Когда код программы разбит на функции, он проще и легче для понимания. Несколько небольших
# функций намного легче читать, чем одну длинную последовательность инструкций.
# - Повторное использование кода. Функции также уменьшают дублирование программного кода в программе. Если определенная
# операция в программе выполняется в нескольких местах, то для выполнения этой операции можно один раз написать функцию
# и затем ее исполнять в любое время, когда она понадобится. Это преимущество функций называется повторным
# использованием кода.
# - Более простое тестирование. Когда каждая задача в программе содержится в собственной функции, процессы тестирования
# и отладки становятся проще. Программисты могут индивидуально протестировать каждую функцию в программе и определить,
# выполняет ли она свою задачу правильно. Это упрощает процесс изолирования и исправления ошибок.
# - Более быстрая разработка. Предположим, что программист или команда программистов разрабатывают многочисленные
# программы. Они обнаруживают, что каждая программа выполняет несколько общих задач, таких как выяснение имени
# пользователя и пароля, вывод текущего времени и т. д. Многократно писать программный код для всех этих задач не имеет
# никакого смысла. Вместо этого для часто встречающихся задач пишут функции, и эти функции могут быть включены в состав
# любой программы, которая в них нуждается.
# - Упрощение командной работы. Функции также упрощают программистам работу в командах. Когда программа разрабатывается
# как набор функций, каждая из которых выполняет отдельную задачу, в этом случае разным программистам может быть
# поручено написание различных функций.

# Функции без возврата значения и с возвратом значения.
# В этой главе вы научитесь писать два типа функций: функции без возврата значения, или пустые функции (void function),
# и функции с возвратом значения. Когда вызывается функция без возврата значения, она просто исполняет содержащиеся в
# ней инструкции и затем завершается. Когда вызывается функция с возвратом значения, она исполняет содержащиеся в ней
# инструкции и возвращает значение в ту инструкцию, которая ее вызвала. Функция input является примером функции с
# возвратом значения. При вызове функции input она получает данные, которые пользователь вводит на клавиатуре, и
# возвращает эти данные в качестве строкового значения. Функции int() и float() — тоже примеры функций с возвратом
# значения. Вы передаете аргумент функции int(), и она возвращает значение этого аргумента, преобразованное в целое
# число. Аналогичным образом вы передаете аргумент функции float(), и она возвращает значение этого аргумента,
# преобразованное в число с плавающей точкой.
# Функция без возврата значения — это первый тип функции, которую вы научитесь писать.


# 5.2 Определение и вызов функции без возврата значения
print('5.2 Определение и вызов функции без возврата значения')
# Программный код функции называется определением функции. Для исполнения функции пишется инструкция, которая ее
# вызывает.
# Имена функциям назначаются точно так же, как назначаются имена используемым в программе переменным. Имя функции должно
# быть достаточно описательным, чтобы любой читающий ваш код мог обоснованно догадаться, что именно функция делает.
# Python требует, чтобы вы соблюдали такие же правила, которые вы соблюдаете при именовании переменных:
# - в качестве имени функции нельзя использовать одно из ключевых слов;
# - имя функции не может содержать пробелы;
# - первый символ должен быть одной из букв от a до z, от A до Z либо символом подчеркивания (_);
# - после первого символа можно использовать буквы от a до z или от A до Z, цифры от 0 до 9 либо символы подчеркивания;
# - символы в верхнем и нижнем регистрах различаются.

# Определение и вызов функции.
# Для того чтобы создать функцию, пишут ее определение. Вот общий формат определения функции в Python:
# def имя_функции():
#   инструкция
#   инструкция
#   ...
# Первая строка называется заголовком функции. Он отмечает начало определения функции. Заголовок функции начинается с
# ключевого слова def, после которого идет имя_функции, затем круглые скобки и потом двоеточие. Начиная со следующей
# строки, идет набор инструкций, который называется блоком. Блок — это просто набор инструкций, которые составляют одно
# целое. Эти инструкции исполняются всякий раз, когда функция вызывается. Обратите внимание, что в приведенном выше
# общем формате все инструкции в блоке выделены отступом для того, чтобы интерпретатор Python использовал их для
# определения начала и конца блока.

# Вызов функции.
# Определение функции говорит о том, что именно функция делает, но оно не исполняет функцию. Для того чтобы функцию
# исполнить, ее необходимо вызвать.
# Когда функция вызвана, интерпретатор перескакивает к этой функции и исполняет инструкции в ее блоке. Затем, когда
# достигнут конец блока, интерпретатор перескакивает назад к той части программы, которая вызвала эту функцию, и
# программа возобновляет исполнение в этой точке. Когда это происходит, мы говорим, что функция вернулась. Для того
# чтобы полностью продемонстрировать, как работает вызов функции, обратимся к программе в файле function_demo.py.
# Нередко программа имеет главную функцию main, которая вызывается, когда программа запускается. Функция main по мере
# надобности вызывает другие функции. Часто говорится, что функция main содержит стержневую логику программы, т.е. общую
# логику программы. В программе в файле two_functions.py приведен пример кода с двумя функциями: main и message.
# Когда программа вызывает функцию, программисты обычно говорят, что поток управления программы передается в эту
# функцию. Это просто означает, что функция берет исполнение программы под свой контроль.

# Выделение отступом в Python.
# В Python каждая строка в блоке должна быть выделена отступом. Последняя выделенная отступом строка после заголовка
# функции является последней строкой в блоке функции. Когда строки выделяются отступом, следует убедиться, что каждая
# строка начинается с одинакового количества пробелов. В противном случае произойдет ошибка.
# В редакторе существует два способа выделить строку отступом: во-первых, нажатием клавиши <Tab> в начале строки либо,
# во-вторых, при помощи клавиши <Пробел> для вставки пробелов в начале строки. При выделении строк отступом в блоке
# можно использовать либо табуляцию, либо пробелы, но не оба способа одновременно. В противном случае это может запутать
# интерпретатор Python и вызвать ошибку.
# Среда IDLE, а также большинство других редакторов Python автоматически выделяют строки блока отступом. При наборе
# двоеточия в конце заголовка функции все строки, набираемые позже, будут автоматически выделяться отступом. Для того
# чтобы выйти из автоматического выделения отступом, следует после набора последней строки блока нажать клавишу
# <Backspace>.
# Для выделения строк блока отступом программисты Python обычно используют четыре пробела. Вы можете использовать любое
# количество пробелов по вашему выбору, коль скоро все строки в блоке расположены с соразмерным отступом.
# Пустые строки, которые появляются в блоке, игнорируются.


# 5.3 Проектирование программы с использованием функций
print('5.3 Проектирование программы с использованием функций')
# Для разбиения алгоритма на функции программисты обычно пользуются приемом, который называется нисходящей разработкой
# алгоритма.

# Составление блок-схемы программы с использованием функций

# Нисходящая разработка алгоритма.
# Мы рассмотрели и продемонстрировали работу функций. Вы увидели, как при вызове функции поток управления программы
# передается в функцию и затем при завершении функции возвращается в ту часть программы, которая вызвала функцию. В этих
# механических аспектах функций очень важно хорошо разобраться.
# Не меньшее значение, чем понимание того, как работают функции, имеет понимание того, как разрабатывать программу,
# которая использует функции. Программисты чаще всего применяют метод под названием нисходящей разработки, который
# позволяет разбивать алгоритм на функции. Процесс нисходящей разработки алгоритма выполняется следующим образом:
# 1. Полная задача, которую должна выполнить программа, разбивается на серию подзадач.
# 2. Каждая подзадача исследуется с целью установления, можно ли ее разложить дальше на другие подзадачи. Этот шаг
# повторяется до тех пор, пока больше ни одной подзадачи невозможно идентифицировать.
# 3. После того как все подзадачи были идентифицированы, их пишут в программном коде.
# Этот процесс называется нисходящей разработкой, потому что программист начинает с того, что обращается к самому
# верхнему уровню выполняемых задач и затем разбивает эти задачи на подзадачи более низкого уровня.

# Иерархические схемы.

# Определение и вызов функций.

# Приостановка исполнения до тех пор, пока пользователь не нажмет клавишу <Enter>.

# Использование ключевого слова pass.
# Приступая к написанию программы, вы знаете имена функций, которые планируете использовать, но еще не представляете
# всех деталей кода, который будет в этих функциях. В этом случае вы можете использовать ключевое слово pass для
# создания пустых функций. Позже, когда детали кода будут известны, вы можете вернуться к пустым функциям и заменить
# ключевое слово pass содержательным кодом.
# Например, когда мы писали код для программы в файле acme_dryer.py, мы могли бы вначале написать определения пустых
# функций для функций step1, step2, step3 и step4, как показано ниже:
# def step1():
#   pass
# def step2():
#   pass
# def step3():
#   pass
# def step4():
#   pass
# Интерпретатор Python игнорирует ключевое слово pass, и в результате этот код создаст четыре функции, которые ничего не
# делают.
# Ключевое слово pass можно использовать в качестве местозаполнителя в любом месте программного кода Python. Например,
# его можно использовать в инструкции if, как показано ниже:
# if x > y:
#   pass
# else:
#   pass
# Вот пример цикла while, в котором используется ключевое слово pass:
# while x < 100:
#   pass


# 5.4 Локальные переменные
print('5.4 Локальные переменные')
# Локальная переменная создается внутри функции. Инструкции, которые находятся за пределами функции, к ней доступа не
# имеют. Разные функции могут иметь локальные переменные с одинаковыми именами, потому что функции не видят локальные
# переменные друг друга.
# Всякий раз, когда переменной внутри функции присваивается значение, в результате создается локальная переменная. Она
# принадлежит функции, в которой создается, и к такой переменной могут получать доступ только инструкции в этой функции.
# (Термин "локальный" указывает на то обстоятельство, что переменная может использоваться лишь локально внутри функции,
# в которой она создается.)
# Если инструкция в одной функции попытается обратиться к локальной переменной, которая принадлежит другой функции, то
# произойдет ошибка код такой программы описан в файле bad_local.py.

# Область действия и локальные переменные.
# Область действия переменной — это часть программы, в которой можно обращаться к переменной. Переменная видима только
# инструкциям в области действия переменной. Областью действия переменной является функция, в которой переменная
# создается. К локальной переменной не может обращаться программный код, который появляется внутри функции в точке до
# того, как переменная была создана.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from timeit import Timer

# Анализ
print('Анализ:')
# Что такое "анализ алгоритмов"?
print('Что такое "анализ алгоритмов"?')
# Студенты-первокурсники ИТ-специальностей очень часто сравнивают плоды своих трудов с другими. Вы могли замечать, что
# быть похожими друг на друга - общее свойство многих компьютерных программ, особенно простых. В связи с этим возникает
# интересный вопрос: если две программы решают одну и ту же задачу, но выглядят по разному, то как понять, что одна из
# них лучше?
# Чтобы на него ответить, нам нужно вспомнить о важном различии между собственно программой и алгоритмом, который она
# воплощает. Как мы говорили в главе 1, алгоритм - это универсальная пошаговая инструкция по решению задачи. Это метод
# для решения любого частного ее случая, который при заданных входных значениях всегда выдает требуемый результат. С
# другой стороны, программа - это то, как алгоритм переложен на некий язык программирования. Может существовать
# множество программ, реализующих один и тот же алгоритм в зависимости от программиста и языка, который он использует.
# Для дальнейшего исследования этого различия рассмотрим функцию которая решает всем знакомую задачу вычисления суммы
# первых n целых чисел. Алгоритм использует идею переменной-аккумулятора, которая инициализируется нулем. В процессе
# решения перебираются n чисел, каждое из которых прибавляется к аккумулятору.


def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
    return the_sum


print(sum_of_n(10))
# А сейчас посмотрите на функцию ниже. На первый взгляд она может показаться странной, но при более близком рассмотрении
# вы увидите, что здесь делается в точности то же самое, что и в предыдущей. Причина, по которой это не очевидно, в
# плохом качестве кода. Мы не используем понятные имена для идентификаторов, чтобы повысить читабельность, и делаем
# избыточное присваивание на шаге аккумуляции, что совершенно не является необходимым.


def foo(tom):
    fred = 0
    for bill in range(1, tom + 1):
        barney = bill
        fred = fred + barney
    return fred


print(foo(10))
# В заданном ранее вопросе мы спрашивали: как понять, что одна функция лучше другой? Ответ будет зависеть от выбранных
# критериев. Функция sumOf, естественно, лучше, чем foo, если вы беспокоитесь о читабельности. Фактически, вы, возможно,
# видели множество подобных примеров в ваших вводных курсах по программированию, поскольку одной из их целей является
# желание помочь вам научиться писать программы, которые легко читать и понимать. Однако, в этом курсе мы заинтересованы
# в том, чтобы охарактеризовывать алгоритм сам по себе. (Но мы все равно надеемся, что вы продолжите бороться за хорошо
# читаемый и понимаемый код.)
# Анализ алгоритмов основывается на сравнении затрачиваемых каждым из них объемов вычислительных ресурсов. Мы хотим быть
# готовыми взять два алгоритма и сказать, что один из них лучше другого, потому что он более эффективно использует
# имеющиеся ресурсы или, возможно, ему их просто меньше нужно. С этой точки зрения две функции выше выглядят очень
# похожими. Они обе используют один и тот же алгоритм для решения задачи суммирования.
# На данный момент становится важным поразмыслить над тем, что же мы подразумеваем под "вычислительными ресурсами".
# Существует два различных подхода к этому вопросу. Первый рассматривает объем пространства или памяти, требуемый
# алгоритму для решения задачи. Эта величина обычно зависит от ее конкретного частного случая. Однако, часто встречаются
# алгоритмы, имеющие специфические требования к объему, и тогда нам надо очень аккуратно подходить к объяснению
# вариантов.
# Альтернативой требований к пространству является анализ и сравнение алгоритмов по времени, которое необходимо им для
# вычислений. Эту величину иногда называют "временем выполнения" алгоритма. Одним из способов измерить время выполнения
# функции sum_of_n является проведение сравнительного анализа. Он подразумевает, что мы засечем реальное время,
# требуемое программе на вычисление результата. В Python можно проделать эту операцию, отметив время начала и время
# окончания работы программы относительно используемой нами системы. В модуле time есть функция time, которая возвращает
# текущее системное время в секундах, прошедшее с некоторого произвольно выбранного начального момента. Вызвав эту
# функцию дважды - в начале и в конце, - и затем посчитав разницу, мы получим точное количество секунд (дробное в
# большинстве случаев), затраченных на выполнение.


def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start


# Функция sum_of_n_2 демонстрирует оригинальную функцию sum_of_n с вызовами времени, встроенными до и после
# суммирования. Она возвращает кортеж, состоящий из результата и количества затраченного на вычисления времени (в
# секундах). Если мы выполним пять вызовов функции, в каждом из которых будет вычисляться сумма первых 10000 целых
# чисел, то мы получим следующее:
for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_2(1000))
# Мы выяснили, что результат хорошо повторяем и что на выполнение кода затрачивается примерно 0,0019 секунд. Что, если
# теперь мы сложим первые 100000 целых?
for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_2(10000))
# Снова времена, необходимые для каждого запуска, лежат близко друг к другу, но становятся длиннее - примерно в десять
# раз. Для n, равной 1000000 мы получим:
for i in range(5):
    print('Sum is %d required %10.7f seconds' % sum_of_n_2(100000))
# Среднее значение вновь выросло примерно в десять раз, по сравнению с предыдущим.
# А теперь рассмотрим функцию sum_of_n_3, демонстрирующий другой способ решения задачи суммирования. Эта функция,
# sum_of_n_3 использует преимущество замкнутой формулы ∑n i = 1 i = ((n) * (n + 1)) / 2 для вычисления суммы первых n
# целых без выполнения итераций.


def sum_of_n_3(n):
    return n * (n + 1) / 2


print(sum_of_n_3(10))
# Если мы проведем аналогичные контрольные замеры для sumOfN3, используя пять различных значений для n (10000, 100000,
# 1000000, 10000000 и 100000000), то получим следующие результаты:
# Sum is 50005000 required 0.00000095 seconds
# Sum is 5000050000 required 0.00000191 seconds
# Sum is 500000500000 required 0.00000095 seconds
# Sum is 50000005000000 required 0.00000095 seconds
# Sum is 5000000050000000 required 0.00000119 seconds
# Есть два важных момента, связанных с этими выходными данными, на которые стоит обратить внимание. Первый - затраченное
# время намного меньше, чем в любом из предыдущих примеров. И второй - все временные величины очень близки друг к другу,
# вне зависимости от значения n. Похоже, что sumOfN3 абсолютно все равно, сколько чисел ей требуется сложить.
# Но о чем этот тест говорит нам в действительности? Интуитивно мы догадываемся, что итеративное решение будет выполнять
# больше работы из-за повторения некоего набора программных шагов. Это, скорее всего, причина, по которой оно занимает
# больше времени. Так же похоже, что время, требуемое итеративному решению, возрастает при увеличении значения n. Тут,
# однако, возникает проблема. Если мы запустим одну и ту же функцию на разных компьютерах или используем различные языки
# программирования, то вполне вероятно, что получим разные результаты. Вычисление sumOfN3 займет тем больше времени, чем
# старше компьютер.
# Нам нужен более хороший способ характеризовать алгоритмы относительно времени выполнения. Тестовая методика вычисляет
# действительное время выполнения. Она не предоставляет нам действительного полезного результата измерений, поскольку
# он зависит от конкретной машины, программы, времени дня, компилятора и языка программирования. Вместо этого мы хотели
# бы иметь характеристику, независящую от программы или компьютера. Такое измерение было бы полезно для оценки алгоритма
# самого по себе, и его стало бы возможно использовать для сравнения алгоритмов в различных реализациях.


# Нотация "большое О"
print('Нотация "большое О":')
# При попытке охарактеризовать эффективность алгоритма в терминах времени выполнения независимо от конкретной программы
# или компьютера, очень важно оценить количество операций или шагов, которые ему потребуются. Если каждый из этих шагов
# принять за базовую единицу вычисления, то время выполнения алгоритма может быть выражено, как количество операций,
# требуемых для решения задачи. Принятие решение о том, что же является таким базовым блоком вычисления, может стать
# сложной задачей, зависящей от того, как алгоритм реализован.
# Хорошей базовой единицей вычисления для сравнения суммирующих алгоритмов, показанных ранее, может служить количество
# операций присваивания, используемых при подсчете суммы. В функции sum_of_n есть только таких присваиваний 1
# (the_sum = 0) плюс n (сколько раз мы вычисляем the_sum = the_sum + i). Эту величину можно обозначить T, где
# T(n) = 1 + n. Параметр n часто называют "размером задания", так что мы можем прочитать формулу как "T(n) - это время,
# необходимое для решения задачи, размером n, за 1+n шагов."
# В представленных выше функциях суммирования для обозначения размера задачи имеет смысл использовать количество
# слагаемых. Так мы сможем сказать, что суммирование первых 100 000 целых - задание большее, чем суммирование первой
# тысячи. Поэтому выглядит разумным положение, что время, требуемое на решение большего случая, будет больше, чем для
# меньшего случая. Таким образом, наша цель - показать, как время работы алгоритма изменяется в зависимости от размера
# задачи.
# Ученые-информатики при использовании такой техники анализа предпочитают идти на один шаг дальше. Выходит так, что
# точное количество операций не так важно, как определение доминирующей части функции T(n). Другими словами, когда
# задание становится больше, некая часть функции T(n), как правило, перекрывает все остальное. Эта доминирующая часть в
# итоге и используется при сравнении. Функция порядка величины описывает ту часть T(n), которая сильнее возрастает при
# росте n. Порядок величины часто называют нотацией "большое О" (от англ order - "порядок") и записывают как O(f(n)).
# Она предоставляет собой целесообразное приближение к действительному числу шагов в вычислении. Функция f(n) является
# простым представлением доминирующей части оригинальной T(n).
# В примере выше T(n)=1+n. Чем больше становится n, тем менее значима для конечного результата константа 1. При поиске
# приближения для T(n) мы можем отбросить 1 и просто сказать, что временем выполнения является O(n). Важно отметить, что
# 1 безусловно важна для T(n). Однако, при росте n наше приближение и без нее останется столь же точным.
# Еще один пример: предположим, что для некоего алгоритма точное число шагов T(n) = 5 * n^2 + 27 * n + 1005. При малых
# n (скажем, 1 или 2) константа 1005 выглядит доминирующей частью функции. Однако, с ростом n превалирующим становится
# слагаемое n2. Фактически, когда n действительно велико, то два других слагаемых перестают играть хоть какую-нибудь
# значимую роль в определении конечного результата. Еще раз, аппроксимируя T(n) с ростом n, мы можем игнорировать другие
# слагаемые и сфокусироваться только на 5 * n^2. Дополнительно, коэффициент 5 тоже становится неважным при увеличении n.
# Так что можно сказать, что функция T(n) имеет порядок величины f(n) = n^2, или просто O(n2).
# Хотя мы и не видим этого в примере с суммированием, иногда производительность алгоритма зависит от точных значений
# данных больше, чем от размера задачи. Для алгоритмов такого рода нужно характеризовать их эффективность с точки зрения
# наилучшего, наихудшего или усредненного случая. Производительность для худшего случая относится к определенному набору
# данных, на котором алгоритм выполняется особенно плохо. В то время как различные наборы данных для точно такого же
# алгоритма могут иметь необычайно хорошую производительность, в большинстве случаев алгоритм имеет производительность
# где-то по середине между этими двумя экстремумами (усредненный случай). Ученым-информатикам важно понимать эти
# различия, чтобы не впасть в заблуждение при рассмотрении одного конкретного случая.
# Некоторые функции порядка величины очень распространены и в процессе изучения алгоритмов будут попадаться вам вновь и
# вновь. Все они представлены ниже. Для того, чтобы увидеть, какая из них является доминирующей частью любой функции
# T(n), мы должны видеть, как они соотносятся друг с другом при возрастании n.
# Наиболее распространенные функции для "большого О"
print('Наиболее распространенные функции для "большого О":')
# 1       - Константная
# log n   - Логарифмическая
# n       - Линейная
# n log n - Линейно-логарифмическая
# n^2     - Квадратичная
# n^3     - Кубическая
# 2^n     - Экспоненциальная
# В качестве заключительного примера предположим, что у нас есть фрагмент кода на Python, показанный ниже. Несмотря на
# то, что на самом деле эта программа ничего не делает, полезно будет посмотреть, как мы можем взять существующий код и
# проанализировать его производительность.
# a = 5
# b = 6
# c = 10
# for i in range(n):
#    for j in range(n):
#        x = i * i
#        y = j * j
#        z = i * j
# for k in range(n):
#    w = a*k + 45
#    v = b*b
# d = 33
# Число операций присваивания представляет собой сумму из четырех слагаемых. Первое - константа 3, отражающая три
# присваивания в начале фрагмента. Второе - 3 * n^2, поскольку три присваивания выполняются n2 раз внутри вложенной
# итерации. Третье - 2 * n - два присваивания, повторяющиеся n раз. Наконец, четвертое слагаемое - константа 1,
# представляющая последний оператор присваивания. Все вместе это дает
# T(n) = 3 + 3 * n^2 + 2 * n + 1 = 3 * n^2 + 2 * n + 4.
# Глядя на степени, мы легко можем заметить, что слагаемое n^2 будет доминантой, и следовательно, этот фрагмент кода
# является O(n2). Обратите внимание, что прочие слагаемые (так же, как и коэффициенты) при возрастании n можно
# проигнорировать.


def min_elem_in_list(list_elem):
    min_elem = list_elem[0]
    for i in range(len(list_elem)):
        for j in list_elem:
            if min_elem > j:
                min_elem = j
    return min_elem


print(min_elem_in_list([5, 4, 2, 1, 0]))
print(min_elem_in_list([0, 1, 2, 3, 4]))


def min_elem_in_list_2(list_elem):
    min_elem = list_elem[0]
    for i in list_elem[1:]:
        if min_elem >= i:
            min_elem = i
    return min_elem


print(min_elem_in_list_2([5, 4, 2, 1, 0]))
print(min_elem_in_list_2([0, 1, 2, 3, 4]))


# Пример про определение анаграммы
print('Пример про определение анаграммы:')
# Хорошим примером для демонстрации алгоритмов с разным порядком величины является классическая задача для строк -
# определение, что слово является анаграммой. Одна строка будет анаграммой другой, если вторая получается простой
# перестановкой букв первой. Например, 'heart' и 'earth' - это анаграммы. Как и строки 'python' и 'typhon'. Для простоты
# будем полагать, что обе заданные строки одной длины и составлены из набора символов в 26 букв в нижнем регистре. Наша
# цель - написать булеву функцию, принимающую две строки и возвращающую ответ на вопрос, являются ли они анаграммами.
# Решение 1: Метки
print('Решение 1: Метки')
# Первое решение задачи про анаграмму будет проверять, входит ли каждый из символов первой строки во вторую. Если все
# символы будут "отмечены", то строки являются анаграммами. "Пометка" символа будет выполняться с помощью замены его на
# специальное значение Python None. Однако, поскольку строки в Python не изменяемы, первым шагом обработки станет
# конвертирование второй строки в список. Каждый символ из первой может быть сверен с элементами списка и, если будет
# найден, отмечен оговоренной заменой.


def anagram_solution_1(s1, s2):
    a_list = list(s2)
    pos_1 = 0
    still_ok = True
    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 += 1
        if found:
            a_list[pos_2] = None
        else:
            still_ok = False
        pos_1 += 1
    return still_ok


print(anagram_solution_1('abcd', 'dcba'))
# При анализе алгоритма нам стоит отметить, что каждый из n символов в s1 вызовет цикл по n символам списка, полученного
# из s2. Каждая из n позиций списка будет посещена единожды, чтобы проверить ее на соответствие s1. Количество таких
# посещений будет выражено через сумму целых чисел от 1 до n. Ранее мы уже говорили, что это может быть записано как
# ∑i = (n * (n+1)) / 2 = (1 / 2) * n^2 + (1 / 2) * n
# С увеличением n слагаемое n2 начнет доминировать, так что n и 12 можно проигнорировать. Таким образом, решение
# является O(n2)

# Решение 2: Сортируй и сравнивай
print('Решение 2: Сортируй и сравнивай')
# Следующее решение задачи про анаграммы будет использовать тот факт, что даже если s1 и s2 различны, они будут
# анаграммами только если состоят из одинаковых символов. Следовательно, если мы отсортируем каждую строку в алфавитном
# порядке от a до z, то в итоге получим одинаковые строки (если, конечно, s1 и s2 - анаграммы). Опять же, в Python мы
# можем использовать встроенный метод sort для списков, полученных в начале функции конвертацией каждой строки.


def anagram_solution_2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


print(anagram_solution_2('abcde', 'edcba'))
# В первый момент вы можете подумать, что этот алгоритм имеет O(n), поскольку у него есть всего одна простая итерация
# для сравнения n символов после сортировки. Однако, два вызова Python-метода sort не проходят даром. Как мы увидим в
# следующих главах, сортировка обычно имеет O(n2) или O(nlogn), так что эта операция доминирует над циклом. В итоге
# алгоритм будет иметь тот же порядок величины, что и сортировочные вычисления.

# Решение 3: Полный перебор
print('Решение 3: Полный перебор')
# Техника полного перебора для решения задач обычно используется, когда все другие возможности уже исчерпаны. Для задачи
# определения анаграммы мы можем просто сгенерировать список всех возможных строк из символов s1 и посмотреть, входит ли
# в него s2. Но в данном подходе есть одна закавыка: при генерации всех возможных строк из s1 есть n возможных первых
# символов, n − 1 возможных вторых символов и так далее. Отсюда общее количество строк-кандидатов будет
# n ∗ ( n − 1) ∗ (n − 2) ∗ ... ∗ 3 ∗ 2 ∗ 1,
# что есть n!. Несмотря на дублирование некоторых строк, программа об этом заранее знать не может, поэтому все равно
# сгенерирует n! различных вариантов.
# Решение n! с увеличением n возрастает быстрее, чем даже 2^n. Фактически, при длине s1 в 20 символов мы получим
# 20! = 2,432,902,008,176,640,000 возможных строк-кандидатов. Если мы будем обрабатывать одно вероятное сочетание каждую
# секунду, то на весь список уйдет 77 146 816 596 лет. Похоже, это совсем не хорошее решение.

# Решение 4: Подсчитывай и сравнивай
print('Решение 4: Подсчитывай и сравнивай')
# Наше последнее решения задачи про анаграммы воспользуется преимуществом того факта, что любые две анаграммы имеют
# одинаковое количество букв a, b и так далее. Для того, чтобы решить, являются ли строки анаграммами, мы сначала
# подсчитаем, сколько раз в них встречается каждый символ. Поскольку возможных букв 26, то мы можем использовать список
# из 26 счетчиков - по одному на каждый символ. Каждый раз, когда мы видим конкретную букву, мы увеличиваем
# соответствующий ей счетчик на единицу. В итоге, если оба списка счетчиков идентичны, то строки - анаграммы.


def anagram_solution_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok


print(anagram_solution_4('apple', 'pleap'))
# Решение вновь имеет некоторое количество циклов. Однако, в отличии от первого варианта, ни один из них не является
# вложенным. Два первых цикла, используемые для подсчета символов, базируются на n. Третий цикл - сравнение двух списков
# счетчиков - всегда состоит из 26 итераций (поскольку строки состоят из 26 возможных элементов). Складывая все вместе,
# получим T(n) = 2 * n + 26 шагов, что является O(n). Мы нашли алгоритм с линейным порядком величины для решения нашей
# задачи.
# До того, как закончить с этим примером, стоит сказать несколько слов о пространственных требованиях. Хотя последнее
# решение и работает за линейное время, оно достигает этого путем использования дополнительных хранилищ для двух списков
# счетчиков. Другими словами, этот алгоритм приносит в жертву пространство, чтобы выиграть время.
# Это очень распространенный случай. Очень часто вам придется делать выбор между временем и пространством. В данном
# случае объем места был не существенен. Однако, если основополагающий алфавит имеет миллионы символов, то это доставит
# больше проблем. При выборе алгоритма только от вас, как ученых-информатиков, будет зависеть определение наилучшего
# использования вычислительных ресурсов, выделенных под конкретную задачу.


# Производительность структур данных в Python
print('Производительность структур данных в Python:')
# Теперь, когда у вас есть общее представление о том, что же такое нотация "большое О" и в чем заключаются различия
# между разными функциями, наша цель в этом разделе - рассказать вам о производительности операций над списками и
# словарями в Python. Мы проведем несколько временн*ы*х экспериментов, чтобы продемонстрировать затраты и выгоды при
# использовании конкретных операций каждой из озвученных структур данных. Понимать эффективность этих структур - очень
# важно для вас, поскольку они являются строительными блоками, которые мы будем использовать при реализации других
# структур данных на протяжении оставшихся глав этой книги. В этом разделе мы не планируем объяснять, почему
# производительность такова, какова она есть. Позднее вы сами увидите возможные реализации списков и словарей, и как от
# этого зависит производительность.


# Списки
print('Списки:')
# Разработчики Python имели широкий выбор, когда реализовывали списки как структуру данных. Каждое их решение оказывает
# влияние на скорость выполнения операций со списками. Чтобы принять верное решение, они смотрели на то, для чего
# пользователи используют списки чаще всего, и оптимизировали реализацию таким образом, чтобы наиболее распространенные
# операции совершались очень быстро. Конечно, разработчики так же старались сделать быстрыми и менее используемые
# операции, но при поиске компромиссов производительность последних приносилась в жертву более распространенным.
# Двумя наиболее частыми операциями над списками являются индексация и присваивание на заданную позицию. Обе они
# занимают равное количество времени, вне зависимости от того, насколько велик список. Когда операции не зависят от
# размера списка (как названные выше), говорят, что они имеют O(1).
# Другим часто встречающимся программистским заданием является увеличение списка. Существует два способа продлить
# список. Вы можете использовать метод добавления или оператор конкатенации. Первый является O(1), но вот второй имеет
# O(k), где k - размер списка, который будет присоединен. Польза от этой информации в том, что она помогает сделать ваши
# программы более эффективными, выбирая правильный инструмент для работы.
# Давайте рассмотрим четыре разных способа сгенерировать список из n чисел, начинающийся с нуля. Сначала мы попробуем
# цикл for и создадим список с помощью конкатенации. Затем используем для этого метод append. Далее попытаемся создать
# список, используя генераторы списков. И, наконец, используем для этого, возможно, самый очевидный способ - функцию
# range, обернутую в конструктор списка.


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


# Чтобы получить время, требуемое для выполнения каждой функции, мы используем модуль Python timeit. Он разработан для
# того, чтобы разработчики могли делать кроссплатформенные синхронные измерения, запуская функции в согласованной среде
# и используя механизмы синхронизации, максимально схожие между собой для разных операционных систем.
# Чтобы использовать timeit, вам нужно создать объект Timer, чьими параметрами являются два оператора Python. Первый из
# них сообщает, что вам нужно время; второй - что тест будет проводиться один раз. Модуль timeit замерит время,
# необходимое для выполнения операции, несколько раз. По умолчанию он попытается запустить операцию один миллион раз.
# Когда это будет сделано, время вернется, как число с плавающей запятой, представляющее собой общее количество секунд.
# Однако, поскольку оператор вычислялся миллион раз, то вы можете прочитать результат, как количество микросекунд,
# затраченных на выполнение одного теста. Так же в timeit можно передать именованный параметр number, который позволит
# вам конкретизировать, сколько раз нужно запустить оператор. Следующий фрагмент показывает, как долго занимает запуск
# каждой тестовой функции тысячу раз.
t1 = Timer('test1()', 'from __main__ import test1')
print('concat', t1.timeit(number=1000), 'milliseconds')
t2 = Timer('test2()', 'from __main__ import test2')
print('append', t2.timeit(number=1000), 'milliseconds')
t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension', t3.timeit(number=1000), 'milliseconds')
t4 = Timer('test4()', 'from __main__ import test4')
print('list range', t4.timeit(number=1000), 'milliseconds')
# В эксперименте выше мы замеряли время для функций test1(), test2() и так далее. Оператор начальной установки может
# показать вам очень необычным, так что давайте разберем детали. Возможно, вы хорошо знакомы с операторами from и
# import, но они обычно используются в начале файлов программ на Python. В этом случае, оператор from __main__ import
# test1 импортирует функцию test1 из пространства имен __main__ в пространство имен, где ставит свой временн*о*й
# эксперимент timeit. Это делается, чтобы запускать тесты в среде с отсутствующими бродячими переменными, которые вы
# могли ненароком создать и которые могут повлиять на производительность функции непредвиденным образом.
# Из эксперимента выше совершенно ясно, что операция append с 0.30 миллисекундами быстрее, чем конкатенация с ее 6.54
# миллисекундами. Также мы видим время, требуемое для двух дополнительных методов создания списков: использования
# конструктора списка с вызовом range и генератора списков. Интересно, что последний в два раза быстрее, чем цикл for с
# операцией append.
# Наше последнее наблюдение в этом маленьком эксперименте заключается в том, что все времена, которые вы видите выше,
# содержат некоторые издержки при фактическом вызове тестовой функции. Однако, мы можем предположить, что для всех
# четырех случаев эта величина одинакова, так что мы по-прежнему имеем адекватное сравнение операций. Поэтому правильно
# говорить не "конкатенация занимает 6.54 миллисекунд", а "тестовая функция конкатенации выполняется 6.54 миллисекунд".
# В качестве упражнения, вы можете провести временн*о*й тест для пустой функции и вычесть его результат из чисел выше.
# После того, как мы увидели, как конкретно может быть измерена производительность, вы можете посмотреть в таблицу ниже,
# чтобы узнать эффективность в терминах "большого О" для основных операций над списками. После вдумчивого размышления
# над ней, вы можете заинтересоваться двумя разными временами для pop. Когда этот метод вызывается для конца списка,
# это занимает O(1). Но когда pop вызывают для первого или любого другого элемента из середины списка, он имеет O(n).
# Причина кроется в том, как в Python выбрана реализация списков. Когда элемент берется из начала списка, то все прочие
# элементы смещаются на одну позицию вперед. Сейчас это может показаться вам глупым, но если вы посмотрите на таблицу
# ниже, то увидите, что эта же реализация позволяет операции индексации иметь O(1). Это один из тех компромиссов,
# которые разработчики Python сочли разумными.

# Эффективность операторов для списков в Python в терминах нотации "большое О"
print('Эффективность операторов для списков в Python в терминах нотации "большое О":')
# index[]                 - O(1)
# Присваивание по индексу - O(1)
# append                  - O(1)
# pop()                   - O(1)
# pop(i)                  - O(n)
# insert(i, item)         - O(n)
# оператор del            - O(n)
# итерирование            - O(n)
# вхождение (in)          - O(n)
# срез [x:y]              - O(k)
# удалить срез            - O(n)
# задать срез             - O(n+k)
# обратить                - O(n)
# конкантенация           - O(k)
# сортировка              - O(n log n)
# размножить              - O(nk)

# В качестве способа демонстрации этих различий в производительности, давайте проведём другой эксперимент с
# использованием модуля timeit. Нашей целью будет возможность проверки производительности операции pop на списке
# известного размера, когда программа выталкивает элемент из конца списка, и ещё раз - когда программа вталкивает
# элемент из начала списка. Мы также произведём замеры времени на списках разной длины. Что мы ожидаем увидеть, так это
# то, что временн*а*я зависимость у выталкивания из конца списка остаётся одинаковой при увеличении списка, в то время
# как выталкивание из начала списка будет расти вместе с его длиной.
# Как видно из первого примера, выталкивание с конца занимает 0.0003 миллисекунды, в то время как на выталкивание из
# начала требуется 4.82 миллисекунды. Для списка в два миллиона элементов коэффициент будет 16 000.
# Первое - это оператор from __main__ import x. Несмотря на то, что мы не определяли функцию, мы хотим иметь
# возможность использовать список-объект x в нашем тесте. Этот подход позволяет нам замерять время только для
# единственной pop-операции и получать для неё наиболее точное значение. Поскольку замеры повторяются тысячу раз, то
# также важно отметить, что список уменьшается в размерах на единицу за каждую итерацию. Но поскольку изначально в нём
# два миллиона элементов, то общий объём уменьшится примерно на 0.05%
popzero = Timer('x.pop(0)', 'from __main__ import x')
popend = Timer('x.pop()', 'from __main__ import x')
x = list(range(2000000))
print(popzero.timeit(number=1000))
x = list(range(2000000))
print(popzero.timeit(number=1000))
# Пока наш первый тест показывает, что pop(0) действительно медленнее pop(). Но он не подтверждает заявление, что pop(0)
# является O(n), в то время как pop() - O(1). Чтобы доказать это, нам нужно рассмотреть производительность обоих
# вызовов на диапазоне размеров списков.
popzero = Timer('x.pop(0)', 'from __main__ import x')
popend = Timer('x.pop()', 'from __main__ import x')
print('pop(0) pop()')
for i in range(100000, 1000001, 100000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print("%15.5f, %15.5f" % (pz, pt))
# Вы можете видеть, как список становится всё длиннее и длиннее, а время, необходимое для pop(0) - больше и больше,
# тогда как график для pop остаётся плоским. Это в точности то, что мы ожидали увидеть от алгоритмов с O(n) и O(1).
# Некоторым источником ошибок в нашем маленьком эксперименте стал тот факт, что на компьютере запущены и другие
# процессы, которые могут замедлять код. Несмотря на то, что мы старались минимизировать влияние прочих происходящих в
# компьютере вещей, с ними связаны некоторые флуктуации времён. Именно поэтому цикл выполняет тест тысячу раз - в первую
# очередь, чтобы статистически собрать достаточно информации для утверждения о надёжности измерений.


# Словари
print('Словари:')
# Второй основной структурой данных в Python является словарь. Как вы наверное помните, словари отличаются от списков
# тем, что в них доступ к элементу получают по ключу, а не по позиции. Позднее в этой книге вы увидите множество
# способов реализации словаря. Сейчас же наиболее важно отметить, что операции получения и записи элемента в словарь
# имеют O(1). Другой важной операцией со словарями является определение принадлежности ему элемента. Проверка, есть ли
# с словаре данный ключ или нет, тоже O(1). Важное замечание в сторону относительно производительности словарей:
# эффективности, которые мы предоставляем в таблице, - это усреднённая производительность. В редких случаях
# принадлежность, получение или запись элемента могут деградировать до O(n). Мы встретимся с этим в одной из последующих
# глав, когда будем говорить о различных способах, которыми можно реализовать словарь.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



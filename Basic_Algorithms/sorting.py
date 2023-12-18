#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://ru.hexlet.io/courses/basic-algorithms/lessons/sorting/theory_unit


# Алгоритмы сортировки.
# В программировании часто встречаются задачи, которые трудно решить «в лоб». Представим, что нам нужно избавиться от
# повторяющихся элементов в массиве. Попробуем найти все числа, которые встречаются здесь больше, чем один раз:
# 7, 3, 1, 9, 10, 2, 3, 6, 9, 4, 7, 5, 5, 4, 2, 8, 4, 7
# Чтобы это сделать, нужно написать сложный алгоритм. Можно упростить задачу и отсортировать массив. В нем повторяющиеся
# элементы находятся рядом, поэтому их легко обнаружить, сравнивая соседние числа:
# 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9, 10
# Не удивительно, что одной из самых полезных задач в программировании считается сортировка - перестановка элементов в
# массиве так, чтобы они располагались в убывающем или возрастающем порядке.


# Чем полезна сортировка.
# Познакомимся с сортировкой поближе и выясним, где она встречается в практических задачах программиста.
# Посмотрим на любой интернет-магазин. В каждом разделе встречаются сотни и тысячи товаров, из которых так сложно
# выбрать подходящий. Чтобы пользователям было удобнее, магазин предлагает сортировку товаров по цене, по рейтингу или
# по популярности.
# При этом покупатели выбирают сортировку по своим целям:
# - По возрастанию цены в поисках выгодных предложений.
# - По убыванию цены, если готовы на дорогую покупку.
# Чтобы интернет-магазин умел сортировать одни и те же записи по-разному, необходима универсальная функция сортировки, о
# которой поговорим в конце урока.


# Три алгоритма сортировки.
# Существуют десятки алгоритмов сортировки, но изучать все слишком долго. Чтобы не останавливаться на этой теме, мы
# выбрали три фундаментальных алгоритма:
# - Пузырьковая сортировка
# - Сортировка выбором
# - Быстрая сортировка
# Все три алгоритма сортируют исходный массив, меняя местами его элементы и не требуя дополнительного пространства.
# Эти алгоритмы помогут понять, как работает сортировка. На их примере вы изучите, какие техники программисты применяют
# при разработке алгоритмов.
# При реализации алгоритмов мы должны помнить о вырожденных случаях - массивах, в которых один или ноль элементов.
# Сортировка их не меняет, но наши алгоритмы должны обрабатывать эти случаи - иначе программа завершится с ошибкой.


# Пузырьковая сортировка.
# Один из самых простых методов - пузырьковая сортировка. Это название произошло от ассоциации с воздухом в воде: на дне
# пузырьки совсем маленькие, но постепенно поднимаются к поверхности, собирают кислород и увеличиваются.
# Похожий принцип работает и с элементами массива при такой сортировке. Посмотрите на этот рисунок:
# Мы идем по массиву и перемещаем вправо самый большой элемент из просмотренных. Так мы находим элемент со значением 10,
# который в итоге побеждает во всех сравнениях и оказывается в правом конце массива.
# Рассмотрим механизм работы данной сортировки на реальном примере. Возьмем массив и сравним элементы попарно от начала
# к концу: первый со вторым, второй с третьим, третий с четвертым и так далее.
# Если два соседних элемента находятся в неправильном порядке, меняем их местами. После первого прохода самый большой
# элемент оказывается справа - его можно больше не сравнивать и не перемещать. Далее повторяем те же действия со всеми
# остальными числами.
# Пузырьковая сортировка реализуется в Python с помощью такой функции:
def bubble_sort(items: list) -> list:
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items


print(bubble_sort([7, 3, 1, 9, 10, 2, 3, 6, 9, 4, 7, 5, 5, 4, 2]))  # [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 9, 9, 10]
print(bubble_sort([2, 3, 4, 3, 1, 2, 4, 5, 1, 2]))  # [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
# Мы видим здесь два вложенных цикла. Внешний цикл ограничивает внутренний цикл на каждом проходе. Сначала он
# простирается до конца массива, но после первого прохода там оказывается максимальный элемент.
# Внутренний цикл на следующем проходе движется до предпоследнего элемента, а затем до пред-пред-последнего - и так до
# тех пор, пока не остается один элемент в левой части:
# for limit in range(len(items) - 1, 0, -1):
#     # ...
# Мы помним, что в Python элементы массива нумеруются с 0 - следовательно, индекс последнего элемента массива items
# равен len(items) - 1.
# В Python временная переменная, для обмена значений переменных, не требуется.
# items[i], items[i + 1] = items[i + 1], items[i]
# На каждом шаге мы находим наибольший элемент в массиве, а последний оставшийся неизбежно оказывается наименьшим - так
# мы получаем упорядоченный массив.
# При пузырьковой сортировке соседние элементы часто меняются местами, поэтому она работает довольно медленно. Чтобы
# сэкономить время, можно сократить количество перестановок. В этом поможет сортировка выбором.


# Сортировка выбором.
# Этот алгоритм сначала проводит операции сравнения и находит наименьший элемент, а только потом помещает его в начало
# массива. После первого прохода алгоритм исключает первый элемент из рассмотрения и ищет минимальный элемент в
# оставшейся части массива, а затем помещаем его на второе место:
# Этот алгоритм работает гораздо быстрее пузырьковой сортировки, потому что сравнений здесь столько же, а вот обмен
# всего один - в самом конце.
# Рассмотрим функцию, реализующую сортировку выбором в Python:
def selection_sort(items: list) -> list:
    for i in range(len(items) - 1):
        index_min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[index_min]:
                index_min = j
        items[i], items[index_min] = items[index_min], items[i]
    return items


print(selection_sort([7, 3, 1, 9, 10, 2, 3, 6, 9, 4, 7, 5, 5, 4, 2]))  # [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 9, 9, 10]
print(selection_sort([10, 2, 3, 4, 3, 1, 8, 2, 9, 4, 5, 1, 2]))  # [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 8, 9, 10]
# В реализации мы сохраняем не сам минимальный элемент, а его индекс в массиве. Это нужно потому, что в конце каждого
# прохода минимальный элемент записывается в начало массива. При этом элемент, который был там до этого, нужно вставить
# куда-то в неупорядоченную половину - легче всего просто поменять их местами.


# Быстрая сортировка.
# Можно сделать сортировку еще быстрее, если менять местами не соседние элементы, а элементы на самом большом расстоянии
# друг от друга.
# Возьмем для примера массив, отсортированный в порядке убывания - от больших к меньшим. Чтобы разместить элементы в
# порядке возрастания, надо попарно поменять их местами: первый и последний, потом второй и предпоследний, и так далее,
# как показано на схеме:
# Сортировки массива в обратном порядке реализуется так:
# left = 0
# right = len(items) - 1
# while left < right:
#     items[left], items[right] = items[right], items[left]
#     left += 1
#     right -= 1
# В примере выше мы создали две переменные-указателя. Переменная left указывает на следующий элемент для обмена слева, а
# переменная right - справа.
# В Python временная переменная не требуется.
# items[left], items[right] = items[right], items[left]
# На каждой итерации цикла после обмена мы увеличиваем левый указатель, сдвигая его вправо, и одновременно уменьшаем
# правый, сдвигая влево:
# left += 1
# right -= 1
# Похожий подход применяется в алгоритме быстрой сортировки. Он частично упорядочивает массив, перемещая в начало
# маленькие элементы, а в конец - большие.
# Частичное упорядочивание делается с помощью программы, похожей на пример выше. Для начала выбираем опорный элемент -
# это условный средний элемент, который помогает отличить маленькие элементы от больших. Затем устанавливаем два
# указателя на начало и конец массива.


# Принцип работы быстрой сортировки.
# Чтобы не запутаться в алгоритме быстрой сортировки, разберем его на схематичном примере. В самом начале наш массив
# выглядит так:
# 5, 4, 10, 1, 8, 2, 7, 9, 6, 3
# В качестве опорного элемента выбрано число 4. Левый указатель смотрит на 5, а правый - на 3.
# Далее двигаем левый указатель и пропускаем элементы меньше опорного, и ищем неправильный элемент слева. Затем двигаем
# правый указатель, пропуская элементы больше опорного.
# Таким образом мы ищем пару элементов, в которой левый больше правого. Когда пара найдена, меняем элементы местами.
# В нашем примере 5 и 3 находятся в неправильной позиции - их надо поменять:
# 3, 4, 10, 1, 8, 2, 7, 9, 6, 5
# Ищем следующую пару для обмена. Справа от 3 находится 4 - наш следующий кандидат для обмена. Обратите внимание, что 4
# - опорный элемент, но он тоже принимает участие в сравнениях и обменах.
# Слева от числа 5 находятся числа 6, 9 и 7. Они больше опорного элемента 4, поэтому указатель их пропускает. В итоге он
# останавливается на числе 2:
# Меняем их местами и ищем следующую пару. Следующие кандидаты - числа 10 и 1:
# 3, 2, 10, 1, 8, 4, 7, 9, 6, 5
# Меняем их местами и останавливаемся, потому что левый и правый указатели упираются друг в друга. Мы получили частично
# упорядоченный массив. Разбиваем его на две части там, где указатели встретились:
# 3, 2, 1, 10, 8, 4, 7, 9, 6, 5
# Продолжаем частичное упорядочивание левой и правой половин массива. Правая половина перед упорядочиванием показана на
# рисунке:
# 10, 8, 4, 7, 9, 6, 5
# Выбираем новый опорный элемент из подмассива. На этот раз это 7. Сдвигая указатели, меняем местами пары 10 и 5, а
# также 8 и 6. Числа 4 и 9 останутся на своих местах. Частично упорядоченный подмассив принимает такой вид:
# 5, 6, 4, 7, 9, 8, 10
# Левый и правый указатель встречаются посередине - на числе 7. Мы снова разбиваем массив на две половины и переходим к
# упорядочиванию левой и правой половин.


# Как реализовать быструю сортировку.
# Попробуем реализовать алгоритм на Python. Начнем с функции частичного упорядочивания:
def partition(items, left, right, pivot):
    while True:
        while items[left] < pivot:
            left += 1
        while items[right] > pivot:
            right -= 1
        if left >= right:
            return right + 1
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
# В качестве параметров функция получает:
# - Массив items.
# - Указатели на левую и правую часть подмассива left и right.
# - Опорный элемент для сравнения pivot.
# Сначала в цикле пропускаются элементы слева, которые меньше опорного:
# while items[left] < pivot:
#     left += 1
# Затем пропускаются элементы справа, которые больше опорного:
# while items[right] > pivot:
#     right -= 1
# Если указатели встретились или зашли друг за друга, мы завершаем цикл и возвращаем место встречи в качестве
# результата. Нам предстоит разбить массив на два подмассива, поэтому надо решить, что именно возвращать. Мы можем
# сказать, что граница - это место, где заканчивается левый подмассив, или место, где начинается правый. Большой разницы
# здесь нет.
# Решим, что функция partition возвращает индекс элемента, где начинается правый подмассив:
# if left >= right:
#     return right + 1
# Если указатели остановились, то они указывают на два элемента в неверном порядке. Левый указатель смотрит на элемент,
# который больше опорного. При этом правый указатель смотрит на элемент, который меньше опорного.
# Меняем местами и сдвигаем элементы, чтобы в следующей итерации продолжить поиск следующей неправильной пары:
# items[left], items[right] = items[right], items[left]
# left += 1
# right -= 1
# Обычно условие завершения цикла пишут в начале (оператор while) или в конце (оператор do…while). В функции partition()
# условие становится известно в середине цикла.
# В языках программирования нет специального синтаксиса для такой ситуации. Обычно программисты записывают бесконечный
# цикл с помощью конструкции while (true), а выход из цикла делают с помощью операторов break или return:
# while True:
#     # ...
#     if left >= right:
#         return right + 1
#     # ...
# Частично упорядоченный массив нельзя назвать полностью отсортированным. Чтобы закончить сортировку, мы должны
# рекурсивно повторить упорядочивание для левой и правой половин массива.
# Про рекурсию мы говорили на прошлом уроке. Так выглядит рекурсивный алгоритм быстрой сортировки. Он немного похож на
# рекурсивную функцию бинарного поиска:


def sort(items, left, right):
    length = right - left + 1
    if length < 2:
        return
    pivot = items[left]
    split_index = partition(items, left, right, pivot)
    sort(items, left, split_index - 1)
    sort(items, split_index, right)
# Для упорядочивания нужно не менее двух элементов. Поэтому мы остановим рекурсивный вызов, когда встретим пустой
# подмассив или подмассив с одним элементом:
# length = right - left + 1
# if length < 2:
#     return
# Функция partition возвращает индекс первого элемента в правом подмассиве. Это помогает функции sort корректно вызвать
# саму себя:
# split_index = partition(items, left, right, pivot)
# sort(items, left, split_index - 1)
# sort(items, split_index, right)
# Единственный код, который вызывает вопросы - выбор опорного элемента:
# pivot = items[left]
# Почему мы всегда выбираем самый левый элемент подмассива?
# Средний элемент должен находиться ровно посередине отсортированного массива. В таком случае его называют медианой.
# Чтобы узнать медиану, нужно иметь отсортированный массив, а чтобы отсортировать массив - знать медиану. Получается
# замкнутый круг.
# На практике необязательно делить массив ровно пополам - достаточно разбить массив на приблизительно равные части -
# алгоритм все равно будет работать быстро. Если элементы в массиве расположены в случайном порядке, то можно брать
# любой элемент по счету - в среднем массив будет всегда разбит пополам.
# Можно выбрать самый левый элемент в качестве опорного элемента - как видно на примере выше, это работает.
# Выше мы написали универсальную функцию, которая может сортировать отдельные подмассивы. Сложность в том, что такой
# функцией не очень удобно пользоваться - приходится передавать параметры left и right даже тогда, когда надо
# отсортировать массив целиком.
# Чтобы упростить себе жизнь, напишем вспомогательную функцию, которая всегда сортирует массив целиком:


def quicksort(items):
    sort(items, 0, len(items) - 1)
    return items


print(quicksort([57, 10, 52, 43, 55, 93, 34, 24, 99]))  # [10, 24, 34, 43, 52, 55, 57, 93, 99]
# Быстрая сортировка намного эффективнее сортировки выбором. Причем эта разница особенно видна на больших массивах. Если
# сортировать миллион элементов, сортировка выбором окажется медленнее в десятки тысяч раз.


# Универсальная функция сортировки.
# Мы реализовали три функции сортировки, каждая из которых упорядочивает в возрастающем порядке элементы простых типов:
# чисел, дат, строк.
# Вспомним пример с интернет-магазином, в котором мы сталкиваемся с более сложной задачей - сортировкой по разным
# атрибутам. Представим, что нам предстоит сортировать товары по трем атрибутам:
# - Название - name.
# - Цена - price.
# - Рейтинг - rating.
# Сам массив выглядит так:
products = [
  {"name": "Телевизор", "price": 100000, "rating": 9.1},
  {"name": "Холодильник", "price": 20000, "rating": 8.3},
  {"name": "Пылесос", "price": 14000, "rating": 7.5},
  {"name": "Стиральная машина", "price": 30000, "rating": 9.2},
  {"name": "Миелофон", "price": 200000, "rating": 8.7},
  {"name": "Микроволновка", "price": 7000, "rating": 8.2},
  {"name": "Проигрыватель", "price": 20000, "rating": 9.0},
  {"name": "Посудомоечная машина", "price": 80000, "rating": 7.8},
  {"name": "Мультиварка", "price": 5000, "rating": 7.1},
]
# Можно реализовать несколько функций сортировки, но есть и более эффективный способ. Интернет-магазину подойдет
# универсальная функция сортировки.
# Каждую из трех видов сортировок выше можно сделать универсальной - и тогда алгоритм сможет сортировать данные любого
# типа. Для этого надо добавить еще один параметр - функцию сравнения (компаратор). Универсальная функция сортировки
# вызывает компаратор каждый раз, когда требуется сравнить два элемента и определить, какой из них больше.
# У компаратора два параметра - два элемента массива, которые надо сравнить. Если первый больше второго, компаратор
# возвращает 1. Если первый меньше второго, компаратор возвращает -1. Если элементы равны, компаратор возвращает 0.
# Вот так будет выглядеть компаратор, сравнивающий элементы по цене:


def compare_by_price(item1, item2):
    if item1[price] < item2[price]:
        return -1
    elif item1[price] == item2[price]:
        return 0
    else:
        return 1


# А вот так - компаратор, сравнивающий элементы по рейтингу:
def compare_by_rating(item1, item2):
    if item1[rating] < item2[rating]:
        return -1
    elif item1[rating] == item2[rating]:
        return 0
    else:
        return 1


# Универсальная функция сравнивает два элемента, но не использует операторы «больше» или «меньше». Вместо этого она
# вызывает компаратор и проверяет результат. Так выглядит универсальная пузырьковая сортировка:
def bubble_sort(items, comparator):
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if comparator(items[i], items[i + 1]) > 0:
                items[i], items[i + 1] = items[i + 1], items[i]

# К окончанию доступ закрыт (((

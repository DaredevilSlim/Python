#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Преобразование в целое число:
print(int(5 / 2))
# Преобразование в вещественное(с плавающей точкой) число:
print(float(2 * 2))
# Объединение(конкатенация) строк:
print('Привет' + ' ' + 'Мир!')
# Преобразование числа в строку:
print('abc' + str(1))
# Повторение строки n раз:
print('abc' * 5)
# Вввод данных:
# name = input('Ведите Ваше имя: ')
# age = input('Сколько Вам лет? ')
# greet = 'Привет, {}. Тебе {} лет.'.format(name, age)
# Форматированная строка
# greet = f'Привет, {name}. Тебе {age} лет.'
# Примеры форматирования строк:
num_one = 2
num_two = 3
variant_one = str(num_one) + ' + ' + str(num_two) + ' = ' + str(num_one + num_two)
print(variant_one)
variant_two = '{} + {} = {}'.format(num_one, num_two, num_one + num_two)
print(variant_two)
variant_three = f'{num_one} + {num_two} = {num_one + num_two}'
print(variant_three)
# Площадь прямоугольника:
# w = input('Введите сторону прямоугольника: ')
# h = input('Введите другую сторону прямоугольника: ')
# w = int(w)
# h = int(h)
# s = f'Площадь прямоугольника {w} x {h} = {w + h}'

# Список
new_list = [1, 2, 3, 4, 5]
print(new_list)
# Добавление элемента в список
new_list.append(6)
print(new_list)

# Кортеж
new_tuple = (1, 2, 3, 4, 5)
print(new_tuple)

# Множество
new_set = {1, 2, 3, 4, 5, 4, 3, 2, 1}
print(new_set)

# Словарь
new_dictionary = {'a': 1, 'b': 2, 'c': 3}
print(new_dictionary)
# Обращение к элементу словаря по ключу
print(new_dictionary['c'])
print(new_dictionary.get('c'))
# Обращение к элементу словаря по ключу и возвращения другого значения в случае отсутствия указанного ключа
print(new_dictionary.get('a', 0))
print(new_dictionary.get('d', 0))
# Проверка наличия
print('a' in new_dictionary)
print('d' in new_dictionary)
# Вывод всех ключей и значений словаря
for k, v in new_dictionary.items():
    print(k, v)
# Вместо использования условных операторов if можно использовать словари
hello = {
    'ru': 'Добрый день!',
    'en': 'Good day!',
    'de': 'Guten tag!',
    'dk': 'God dag!',
    'default': 'Unknown language'
    }
# s = input('Введите код: ')
# greet = hello.get(s, hello['default'])
# print(greet)


# Функции
# Функция определения количества секунд в дне(по умолчанию) или днях(в случае задания параметра)
def count_of_seconds(days=1):
    return 24 * days * 60 * 60


print(count_of_seconds())


# Функция вычисления площади круга
def area_of_disk(radius):
    """Help on function

        area_of_disk(number) -> number
        Return area of disk by radius
    """
    return 3.14 * radius ** 2


# Функция определения площади бублика или пончика
def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)


# Функция получающая в качестве параметров неограниченное количество значений и помещающая их в кортеж
def function_put_in_tuple(*params):
    for p in params:
        print(p)


function_put_in_tuple(1, 2, 3, 4, 5)


# Функция получающая в качестве параметров неограниченное количество значений и помещающая их в словарь
def function_put_in_dictionary(**params):
    for p, m in params.items():
        print(p, m)


function_put_in_dictionary(John=100, Mike=200, Pete=300)
#
#
#
#
#
#
#
#
#
# 3 - 0:00:00
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

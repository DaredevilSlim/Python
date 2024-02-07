#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ГЛАВА 15
print('ГЛАВА 15')
# Итераторы, контейнеры и перечисления
print('Итераторы, контейнеры и перечисления')
# Python позволяет создавать классы особого назначения: итераторы, контейнеры и перечисления.


# 15.1. Итераторы
print('15.1. Итераторы')
# Итератор - это класс, который при каждом обращении выдает очередной элемент заданной последовательности. Объект такого
# класса можно перебрать в цикле перебора последовательности. Можно сказать, что итератор аналогичен функции-генератору
# (см. разд. 11.3), только является классом.
# Чтобы превратить класс в итератор, следует переопределить в нем два специальных метода:
# - __iter__(self) - служит признаком того, что класс является итератором. Должен возвращать текущий объект.
# Как правило, этот метод выполняет всевозможные предустановки.
# Если в классе определены методы __iter__() и __getitem__() (о последнем будет рассказано позже), предпочтение отдается
# первому методу;
# - __next__(self) - вызывается при выполнении каждой итерации и должен возвращать очередной элемент последовательности.
# Если последовательность закончилась, в этом методе следует сгенерировать исключение StopIteration, которое сообщит
# вызывающему коду о завершении перебора.
# Рассмотрим класс, хранящий строку и на каждой итерации возвращающий очередной ее символ, начиная с конца в
# test_00127.py.
# Также мы можем переопределить специальный метод __len()__, возвращающий размер последовательности, и специальные
# методы __str()__ и __repr()__, выдающие строковое представление объекта (были рассмотрены в разд. 13.5). Перепишем код
# нашего класса итератора, добавив в него определение методов __len()__ и __str()__ в test_00128.py.
# Теперь мы можем получить длину последовательности, хранящейся в объекте класса ReverseString, и его строковое
# представление:


# 15.2. Контейнеры
print('15.2. Контейнеры')
# Контейнер - это класс с функциональностью либо пронумерованной последовательности (контейнер-последовательность) с
# произвольным доступом к любому ее элементу по его индексу, либо отображения (контейнер-отображение).


# 15.2.1. Контейнеры-последовательности
print('15.2.1. Контейнеры-последовательности')
# Чтобы превратить класс в контейнер-последовательность, следует переопределить в нем следующие специальные методы:
# - __getitem__(self, <Индекс>) - вызывается при извлечении элемента последовательности с заданным индексом и должен
# возвращать этот элемент. Если индекс не является целым числом или срезом, метод должен генерировать исключение
# TypeError, а если такого индекса не существует,- исключение IndexError;
# - __setitem__(self, <Индекс>, <Значение>) - вызывается в случае присваивания нового значения элементу
# последовательности с заданным индексом. Не должен возвращать результата. В случае задания индекса недопустимого типа
# или отсутствия такого индекса в последовательности метод должен генерировать те же исключения, что и метод
# __getitem__();
# - __delitem__(self, <Индекс>) - вызывается в случае удаления элемента последовательности с заданным индексом.
# Не должен возвращать результата. В случае задания индекса недопустимого типа или отсутствия такого индекса в
# последовательности метод должен генерировать те же исключения, что и метод __getitem__();
# - __contains__(self, <Значение>) - вызывается при проверке существования в последовательности элемента с заданным
# значением. Должен возвращать True, если такой элемент есть, и False - в противном случае.
# В контейнере-последовательности можно дополнительно реализовать функциональность итератора (см. разд. 15.1),
# переопределив специальные методы __iter__(), __next__() и __len__(). Чаще всего так и поступают.
# Мы давно знаем, что строки в Python являются неизменяемыми. Напишем класс MutableString, представляющий строку,
# которую можно изменять теми же способами, что и список в test_00129.py.
# Проверим, как наш класс обрабатывает нештатные ситуации, обратившись по несуществующему индексу:


# 15.2.2. Контейнеры-отображения
print('15.2.2. Контейнеры-отображения')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 293


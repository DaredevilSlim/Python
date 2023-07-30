#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import localtime   # Подключение функции localtime() из модуля time

# Вывод текущих даты и времени
d = ['понедельник', 'вторник', 'среда', 'четверг',
     'пятница', 'суббота', 'воскресенье']
m = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
     'июля', 'августа', 'сентября', 'октября', 'ноября','декабря' ]
t = localtime()  # Получение текущего времени
print('Сегодня:\n%s %s %s %s %02d:%02d:%02d\n%02d.%02d.%02d' %
      (d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t[5], t[2], t[1], t[0]))
input()
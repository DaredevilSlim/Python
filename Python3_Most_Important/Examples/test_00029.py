#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random  # Подключаем модуль random


# Генератор паролей
def password_generator(count_char=8):
    arr = ['а', 'b', 'с', 'd', 'е', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'А', 'В', 'С', 'D', 'Е', 'F', 'G', 'Н', '!', 'J', 'К', 'L', 'М',
           'N', 'О', 'Р', 'Q', 'R', 'S', 'Т', 'U', 'V', 'W', 'Х', 'У', 'Z',
           '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    password = []
    for i in range(count_char):
        password.append(random.choice(arr))
    return ''.join(password)


# Вызываю функцию:
print(password_generator(10))  # Выведет что-то вроде ngODHEBJBx
print(password_generator())    # Выведет что-то вроде ZxcpkFSO

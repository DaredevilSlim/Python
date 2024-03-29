#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random                   # Подключаем модуль random


# Генератор паролей
def password_generator(count_char=8):
    arr = ['а', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'о', 'р', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'х', 'у', 'z', 'А', 'В', 'С', 'D', 'Е', 'F', 'G', 'Н', 'I', 'J', 'К', 'L', 'М', 'N', 'О', 'Р', 'Q', 'R',
           'S', 'Т', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', 'З', '4', '5', '6', '7', '8', '9', '0']
    password = []
    for i in range(count_char):
        password.append(random.choice(arr))
    return ''.join(password)


print(password_generator(10))  # Выведет что-то вроде eLSl5lD1Ql
print(password_generator())    # Выведет что-то вроде fnfwcGDm

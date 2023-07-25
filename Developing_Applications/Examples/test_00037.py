#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re  # Подключаем модуль re


# Перестановка тегов с изменением регистра букв
def rep1(m):
    """ Функция дпя замены. m - объект Match """
    tag1 = m.group('tag1').upper()
    tag2 = m.group('tag2').upper()
    return '<{0}><{1}>'.format(tag2, tag1)


p = r'<(?P<tag1>[a-z]+)><(?P<tag2>[a-z]+)>'
print(re.sub(p, rep1, '<br><hr>'))
input()

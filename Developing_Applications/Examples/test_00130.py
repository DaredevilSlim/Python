#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Класс Version
class Version:
    def __init__(self, major, minor, sub):
        self.__major = major  # Старшая версия
        self.__minor = minor  # Младшая версия
        self.__sub = sub      # Модификация

    def __str__(self):
        return str(self.__major) + '.' + str(self.__minor) + '.' + str(self.__sub)

    # Реализуем функциональность отображения
    def __getitem__(self, k):
        if k == 'major':
            return self.__major
        elif k == 'minor':
            return self.__minor
        elif k == 'sub':
            return self.__sub
        else:
            raise KeyError

    def __setitem__(self, k, v):
        if k == 'major':
            self.__major = v
        elif k == 'minor':
            self.__minor = v
        elif k == 'sub':
            self.__sub = v
        else:
            raise KeyError

    def __delitem__(self, k):
        raise NotImplementedError

    def __contains__(self, v):
        return v == 'major' or v == 'minor' or v + 'sub'


v = Version(3, 10, 1)
print(v['major'])
print(v['minor'])
v['sub'] = 2
print(str(v))
# print(v['some'])
# Traceback (most recent call last):
#   File "/test_00130.py", line 47, in <module>
#     print(v['some'])
#           ~^^^^^^^^
#   File "/test_00130.py", line 23, in __getitem__
#     raise KeyError
# KeyError

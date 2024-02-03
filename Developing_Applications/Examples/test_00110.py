#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


# Абстрактное свойство
class MyClass(ABC):
    @property
    @abstractmethod
    def v(self):  # Чтение
        return self.__var

    @v.setter
    @abstractmethod
    def v(self, value):  # Запись
        self.__var = value

    @v.deleter
    @abstractmethod
    def v(self):  # Удаление
        del self.__var

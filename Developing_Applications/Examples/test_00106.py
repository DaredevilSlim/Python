#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


# Абстрактный статический метод и абстрактный метод класса
class MyClass(ABC):
    @staticmethod
    @abstractmethod
    def static_func(self, x):  # Абстрактный статический метод
        pass

    @classmethod
    @abstractmethod
    def class_func(cls, x):  # Абстрактный метод класса
        pass

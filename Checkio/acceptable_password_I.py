#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вы начали серию задач связаную с паролями. Каждая следующая задача связана с предыдущей. Каждая следующая задача будет сложнее предыдущей.
# В этой задаче, Вам нужно создать функцию проверки пароля.
# Условия проверки:
# длина пароля должна быть больше 6.
# Входные данные: Строка.
# Выходные данные: Логический тип.
# Пример:
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False
# Для чего это нужно: Для проверки заполнения пароля. Кроме того, полезно будет научиться оценивать задачи.
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6


print(is_acceptable_password("short"))       # False
print(is_acceptable_password("muchlonger"))  # True
print(is_acceptable_password("ashort"))      # False

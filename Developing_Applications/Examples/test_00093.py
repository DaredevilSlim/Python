#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys  # Подключаем модуля sys
import test_00093  # Подключаем модуля sys


# Подключим этот модуль и выведем текушее значение переменной х:
x = 150
sys.path.append(r"C:\book")  # Добавляем путь к папке с модулем
# Подключаем модуль test_00093.ру
print(test_00093.x)  # Выводим текущее значение

# Не закрывая окна интерпретатора, изменим значение переменной х на 800, а затем попробуем заново импортировать модуль и
# вывести текущее значение переменной:
# Изменяем значение в модуле на 800
print(test_00093.x)  # Значение не изменилось

# Как видно из примера, значение переменной х не изменилось. Теперь перезагрузим модуль с помощью функции reload():
# from importlib import reload
# reload(test_00093)  # Перезагружаем модуль
print(test_00093.x)  # Значение изменилось

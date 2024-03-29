#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Джо Палука обладает такими толстыми пальцами, что всегда задевает клавишу “Caps Lock” когда пытается нажать кнопку
# “a”. (Правда когда Джо пытается напечатать заглавную версию “a”, требующую нажатия нескольких клавиш, он более
# внимателен, и всегда жмет [Shift] + [a] правильно). Ваша программа должна вернуть то, что получится у Джо при наборе
# переданного текста. “Caps Lock” влияет только на кнопки от “a” до “z”, и не оказывает эффекта на другие клавиши. Перед
# набором текст “Caps Lock” выключен.
# В клавиатуре Джо Caps Lock всегда выводит буквы в верхнем регистре. Это значит, что если Caps Lock нажат и Джо
# нажимает Shift + 'b', он получил 'B' (в верхнем регистре)
# Входные данные: Строка. Текст, который печатает Джо.
# Выходные данные: Строка. Текст, который получится у Джо после набора.
# Миссия позаимствована на Python CCPS 109 Осень 2018. Она преподается Илккой Коккаринен в Школе непрерывного
# образования Раймонда Чанга
def caps_lock(text: str) -> str:
    t = text.split('a')
    return ''.join(t[i].upper() if i % 2 != 0 else t[i] for i in range(len(t)))


print(caps_lock("Why are you asking me that?"))     # "Why RE YOU sking me thT?"
print(caps_lock("Always wanted to visit Zambia."))  # "AlwYS Wnted to visit ZMBI."
print(caps_lock("Aloha from Hawaii"))               # "Aloh FROM HwII"

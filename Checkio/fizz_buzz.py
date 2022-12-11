#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.
# Вы должны написать функцию, которая принимает положительное целое число и возвращает:
# "Fizz Buzz" , если число делится на 3 и 5;
# "Fizz" , если число делится на 3;
# "Buzz" , если число делится на 5;
# Число , как строку для остальных случаев.
# Входные данные: Число, как целочисленное (int).
# Выходные данные: Ответ, как строка (str).
# Как это используется: Здесь вы можете научиться как писать простейшую функцию и работать с if-else.
# Предусловия: 0 < number ≤ 1000
def checkio(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0:
        return 'Fizz Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    return str(number)
    # second solution
    # t = number % 3 == 0
    # f = number % 5 == 0
    # s = ['Fizz', 'Buzz']
    # return ' '.join(s) if t and f else s[0] if t else s[1] if f else str(number)

print(checkio(15))  # "Fizz Buzz"
print(checkio(6))   # "Fizz"
print(checkio(10))  # "Buzz"
print(checkio(7))   # "7"

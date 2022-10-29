#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Речевой модуль Стефана сломался. Этот модуль отвечал за произношение чисел. Для него сейчас большая проблема
# произносить составные числа. Помогите нашему Роботу заговорить правильно и освоить хотя бы первую тысячу. Стефан
# должен говорить на английском, так что вам нужно знать правила составления чисел в английском языке. Все слова в
# строковом представлении числа должны быть разделены одним пробелом. Будьте осторожны с пробелами -- очень сложно
# увидеть двойной пробел, но это критично для компьютера.
# Вх. данные: Число, как целочисленное (int).
# Вых. данные: Текстовое написание числа, как строка (str).
# Примеры:
# checkio(4)=='four'
# checkio(143)=='one hundred forty three'
# checkio(12)=='twelve'
# checkio(101)=='one hundred one'
# checkio(212)=='two hundred twelve'
# checkio(40)=='forty'
# Как это используется: Эта концепция будет полезна для программного обеспечения по синтезу речи или автоматических
# систем отчетности. Также это может пригодиться при написании простого бота для чата, который будет уметь составлять
# числа.
# Предусловия: 0 < number < 1000

numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
           10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16:'sixteen',
           17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
           50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: ' hundred'}


def checkio(number):
    if number < 20:
        return numbers[number]
    elif number < 100:
        n_mod = number % 10
        return numbers[number] if n_mod == 0 else numbers[number - n_mod] + ' ' + checkio(n_mod)
    hundred = numbers[number // 100] + numbers[100]
    n_mod = number % 100
    return hundred if n_mod == 0 else hundred + ' ' + checkio(n_mod)


print(checkio(4))    # 'four'
print(checkio(12))   # 'twelve'
print(checkio(40))   # 'forty'
print(checkio(44))   # 'forty-four'
print(checkio(133))  # 'one hundred thirty-three'
print(checkio(100))  # 'one hundred'
print(checkio(201))  # 'two hundred one'
print(checkio(999))  # 'nine hundred ninety-nine'

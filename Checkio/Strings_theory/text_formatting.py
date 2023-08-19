#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Вам предоставлена длинная строка (набранная моноширинным шрифтом), и вы должны разбить ее, чтобы соблюсти заданную
# ширину. После этого вам нужно отформатировать текст в соответствии с заданным стилем: "l" означает, что вы должны
# выровнять текст по левому краю - left, "c" - по центру - center, "r" - по правому краю - right, а "j" означает, что вы
# должны выровнять текст по ширине - justify. И, наконец, строки вывода не должны заканчиваться пробелами.
# Если вам нужно поместить суммарно непарное количество пробелов вокруг строки, чтобы отцентрировать ее, то поставьте
# парное количество пробелов вперед.
# Правила выравнивания текста:
# Поскольку мы не всегда можем поставить одинаковое количество пробелов между словами в строке, поместите большие блоки
# пробелов сначала. Например: X---X---X--X--X--X, когда вам нужно поместить 12 пробелов в 5 местах: 3-3-2-2-2.
# Не выравнивайте последнюю строку текста.
# Вам не нужно будет разбивать слово на две части, так как предоставленной ширины вполне достаточно.
# Входные данные: Текст (строка - str), ширина (целое число - int) и стиль (строка - str).
# Выходные данные: Отформатированный текст (строка - str).
# Предварительное условие:
# all(len(word) <= width for word in text.split());
# '\n' нету в тексте;
# варианты стиля в ("l", "c", "r", "j");
# 0 < len(text) <= 1000.
def text_formatting(text: str, width: int, style: str) -> str:
    text = list(map(str, text.split()))
    new_s = ''
    new_l = text[0]
    for i in text[1:]:
        if (len(new_l) + len(i) + 1) <= width:
            new_l += ' ' + i
        else:
            new_s += (s_format(new_l, width, style) if style in ['c', 'r', 'j'] else new_l) + '\n'
            new_l = i
        if i == text[-1]:
            new_s += s_format(new_l, width, style) if style in ['c', 'r'] else new_l
    return new_s


def s_format(t: str, w: int, s: str) -> str:
    if s == 'j':
        a = t.count(' ')
        b = w - len(t)
        c = b // a
        d = b % a
        e = list(map(str, t.split()))
        for i in range(a):
            e[i] += ' ' * c + ' ' * (1 if d > 0 else 0)
            d -= 1
        return ' '.join(e)
    return '{0:{2}{1}}'.format(t, w, '^' if s == 'c' else '>').rstrip(' ')


print(
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38, "l")
)  # "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."
print(
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30, "c")
)  # " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
print(
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50, "r")
)  # "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
print(
    text_formatting(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45, "j")
)  # "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."
print(text_formatting('Hi, my name is Alex and I am 18 years old.', 20,
                      'l'))  # 'Hi, my name is Alex\nand I am 18 years\nold.'

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
    # your code here
    return ""


print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        38,
        "l",
    ))  # "Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit. Iure\nharum suscipit aperiam aliquam ad,\nperferendis ex molestias reiciendis\naccusantium quos, tempore sunt quod\nveniam, eveniet et necessitatibus\nmollitia. Quasi, culpa."

print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        30,
        "c",
    ))  # " Lorem ipsum dolor sit amet,\nconsectetur adipisicing elit.\n Iure harum suscipit aperiam\n  aliquam ad, perferendis ex\n     molestias reiciendis\naccusantium quos, tempore sunt\n   quod veniam, eveniet et\n   necessitatibus mollitia.\n        Quasi, culpa."
print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        50,
        "r",
    ))  # "           Lorem ipsum dolor sit amet, consectetur\n     adipisicing elit. Iure harum suscipit aperiam\n   aliquam ad, perferendis ex molestias reiciendis\n       accusantium quos, tempore sunt quod veniam,\n eveniet et necessitatibus mollitia. Quasi, culpa."
print(text_formatting("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum suscipit aperiam aliquam ad, perferendis ex molestias reiciendis accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus mollitia. Quasi, culpa.",
        45,
        "j",
    ))  # "Lorem   ipsum  dolor  sit  amet,  consectetur\nadipisicing elit. Iure harum suscipit aperiam\naliquam    ad,   perferendis   ex   molestias\nreiciendis  accusantium  quos,  tempore  sunt\nquod   veniam,   eveniet   et  necessitatibus\nmollitia. Quasi, culpa."

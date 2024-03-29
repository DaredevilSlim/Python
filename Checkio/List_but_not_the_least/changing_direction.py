#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан список состоящий из целых чисел. Ваша задача выяснить сколько раз в нем меняется направление при переходе от
# одного числа к другому. Если числа равны, то направление не меняется. В случае, если следующий элемент отличается от
# предыдущего - необходимо определить в какую сторону поменялось направление.
# Давайте взглянем на схему:
# На ней изображено следующее:
# для фрагмента 1, 2, 2 - направление идет вверх;
# для фрагмента 2, 1 - идет вниз;
# для фрагмента 1, 2, 2 - снова возрастает.
# Так что в данном примере есть всего две точки смены направления:
# #1 - направление меняется с возрастающего на убывающее, и
# #2 - наоборот, начинает опять расти вверх.
# Входные данные: Список целых чисел.
# Выходные данные: Целое число.
# Preconditions:
# Список не может быть пустым;
# Все элементы в списке являются положительными целыми числами.
def changing_direction(elements: list[int]) -> int:
    new = ''
    for i in range(len(elements) - 1):
        if elements[i] < elements[i + 1]:
            new += '0'
        elif elements[i] > elements[i + 1]:
            new += '1'
    return sum(1 for i in range(len(new) - 1) if new[i] != new[i + 1])


print(changing_direction([0]))                                                # 0
print(changing_direction([1, 2, 3, 4, 5]))                                    # 0
print(changing_direction([1, 2, 3, 2, 1]))                                    # 1
print(changing_direction([1, 2, 2, 1, 2, 2]))                                 # 2
print(changing_direction([1, 2, 3, 5, 4, 2, 5, 7, 8, 3, 2, 1]))               # 3
print(changing_direction([5, 4, 9, 10, 10, 10, 10, 3, 8, 5, 1, 9, 9, 4, 1]))  # 6
print(changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]))      # 7

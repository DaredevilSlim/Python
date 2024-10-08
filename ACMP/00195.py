#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №195 - Эния
# (Время: 1 сек. Память: 16 Мб Сложность: 3%)
# Неспокойно сейчас на стапелях шестого дока межгалактического порта планеты Торна. Всего через месяц закончится
# реконструкция малого броненесущего корвета “Эния”. И снова этому боевому кораблю и его доблестной команде предстоят
# тяжелые бои за контроль над плутониевыми рудниками Сибелиуса. Работа не прекращается ни на секунду, лазерные
# сварочные аппараты работают круглые сутки. От непрерывной работы плавятся шарниры роботов-ремонтников. Но задержаться
# нельзя ни на секунду.
# И вот в этой суматохе обнаруживается, что термозащитные панели корвета вновь требуют срочной обработки сульфидом
# тория. Известно, что на обработку одного квадратного метра панели требуется 1 нанограмм сульфида. Всего необходимо
# обработать N прямоугольных панелей размером A на B метров. Вам необходимо как можно скорее подсчитать, сколько всего
# сульфида необходимо на обработку всех панелей “Энии”. И не забудьте, что панели требуют обработки с обеих сторон.
# Входные данные - Во входном файле INPUT.TXT содержатся 3 целых положительных числа N(N ≤ 100), A(A ≤ 100), B(B ≤ 100)
# Выходные данные - В выходной файл OUTPUT.TXT нужно вывести единственное число – вес необходимого для обработки
# сульфида тория в нанограммах.
n, a, b = map(int, input().split())
print(2 * n * (a * b))

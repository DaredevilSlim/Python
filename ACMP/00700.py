#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Мёд
# (Время: 1 сек. Память: 16 Мб Сложность: 23%)
# Все любят сладости и, в частности, мед. Винни-Пух тоже его любит. Каждый день он шел лакомиться медом, а по дороге
# домой заходил в гости к Кролику. Но приближалась зима, и Винни-Пух начал задумываться о запасах. Он решил в течении N
# дней не лакомиться медом, а собирать полный горшочек объемом V горстей и перекладывать его в бочку. В первый день
# своего собирательства он так и сделал. Терпения хватило на один день. А на следующий день он не смог устоять и по
# дороге домой съел K горстей меда из горшочка. В каждый следующий день из полного горшочка он съедал на K горстей
# больше.
# Необходимо определить объем меда, собранного Винни-Пухом на зиму.
# Входные данные
# Входной файл INPUT.TXT содержит три натуральных числа N (N ≤ 300), V (V ≤ 107) и K (K ≤ 1000). K – объем, на который
# Винни-Пух с каждым днем съедал больше меда.
# Выходные данные
# В выходной файл OUTPUT.TXT выведите два значения через пробел. Сначала идет строка «NO», если случилось, что Винни-Пух
# пришел к Кролику с пустым горшочком и «YES» в противном случае. Второе значение – объем меда, заготовленного
# Винни-Пухом на зиму.
a, b, c = map(int, input().split())
d = b
e = 0
f = 0
while a and d > 0:
    f += d
    e += c
    d = b - e
    a -= 1
print('NO' if a else 'YES', f)
# Или
a, b, c = map(int, input().split())
d = b
e = 0
f = 0
while a > 0 and d > 0:
    f += d
    e += c
    d = b - e
    a -= 1
print('YES' if a == 0 else 'NO', f)

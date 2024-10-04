#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ЗАДАЧА №648
# Азартный Шрэк
# (Время: 1 сек. Память: 16 Мб Сложность: 25%)
# Как-то раз Шрек решил посетить казино. Не будучи заядлым любителем азартных игр, Шрек обнаружил, что он не знает
# правил ни одной из игр, доступных в казино. Недолго думая, Шрек решил все-таки поиграть. Его взор привлекла игра с
# довольно незамысловатыми правилами.
# На игровом столе лежат N карточек. На каждой карточке написано целое положительное число. Игра проходит между игроком
# и крупье. Карточки лежат на столе числами вниз. Игра заключается в том, что игрок открывает ровно N/2 карточек. Сумма
# всех чисел, написанных на карточках открытых игроком, называется “суммой игрока”. Следующим ходом крупье открывает
# оставшиеся N/2 карточек. Сумма всех чисел, написанных на карточках открытых крупье, называется “суммой крупье”.
# Выигрыш игрока определяется разностью чисел между “суммой игрока” и “суммой крупье”. Очевидно, что полученная разность
# может быть отрицательным числом. Это свидетельствует о том, что игрок проиграл и должен казино соответствующую сумму.
# Все бы ничего, но Шрек обладает способностью видеть надписи сквозь бумагу любой плотности. Ваша задача определить
# максимальную сумму выигрыша, которую может получить Шрек с учетом того, что он видит все числа, написанные на
# карточках.
# Входные данные - Первая строка входного файла INPUT.TXT содержит одно четное натуральное число N (2 ≤ N ≤ 100). Вторая
# строка входного файла содержит ровно N чисел Ai(1 ≤ Ai ≤ 106) – числа, написанные на игральных карточках. Все числа в
# строке разделяются одиночными пробелами, Ai – число, написанное на i-й карточке. Карточки нумеруются последовательно,
# начиная с единицы.
# Выходные данные - Единственная строка выходного файла OUTPUT.TXT должна содержать ровно одно целое число –
# максимальный выигрыш, который может получить Шрек с учетом своей уникальной способности видеть числа, написанные на
# карточках.
a = int(input()) // 2
b = sorted(map(int, input().split()))
print(sum(b[a:]) - sum(b[:a]))
# Или
a = input()
b = sorted(map(int, input().split()))
print(sum(b[len(b) // 2:]) - sum(b[:len(b) // 2]))

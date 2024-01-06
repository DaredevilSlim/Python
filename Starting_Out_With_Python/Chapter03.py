#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3 Структуры принятия решения и булева логика
print('3 Структуры принятия решения и булева логика')
# 3.1 Инструкция if
print('3.1 Инструкция if')
# Инструкция if применяется для создания управляющей структуры, которая позволяет иметь в программе более одного пути
# исполнения. Инструкция if исполняет одну или несколько инструкций, только когда булево выражение является истинным.
# Управляющая структура — это логическая схема, управляющая порядком, в котором исполняется набор инструкций.
# Последовательная структура представляет собой набор инструкций, которые исполняются в том порядке, в котором они
# появляются.
# В Python для написания структуры принятия решения с единственным вариантом используется инструкция if. Вот общий
# формат инструкции if:
# if условие:
#   инструкция
#   инструкция
#   ...
# Для простоты мы будем называть первую строку условным выражением, или выражением if. Условное выражение начинается со
# слова if, за которым следует условие, т.е. выражение, которое будет вычислено, как истина либо ложь. После условия
# стоит двоеточие. Со следующей строки начинается блок инструкций. Блок — это просто набор инструкций, которые
# составляют одну группу. Обратите внимание, что в приведенном выше общем формате все инструкции блока выделены
# отступом. Такое оформление кода обязательно, потому что интерпретатор Python использует отступы для определения начала
# и конца блока. Во время исполнения инструкции if осуществляется проверка условия. Если условие истинное, то
# исполняются инструкции, которые появляются в блоке после условного выражения. Если условие ложное, то инструкции в
# этом блоке пропускаются.

# Булевы выражения и операторы сравнения.
# Как упоминалось ранее, инструкция if осуществляет проверку выражения, чтобы определить, является ли оно истинным или
# ложным. Выражения, которые проверяются инструкцией if, называются булевыми выражениями в честь английского математика
# Джорджа Буля.
# Как правило, булево выражение, которое проверяется инструкцией if, формируется оператором сравнения (реляционным
# оператором). Оператор сравнения определяет, существует ли между двумя значениями определенное отношение. Например,
# оператор больше (>) определяет, является ли одно значение больше другого. Оператор равно (==) — равны ли два значения
# друг другу.
# Операторы сравнения:
# Оператор  Значение
# >         Больше
# <         Меньше
# >=        Больше или равно
# <=        Меньше или равно
# ==        Равно
# !=        Не равно
# Булевы выражения с использованием операторов сравнения:
# Выражение Значение
# x > y     x больше y?
# x < y     x меньше y?
# x >= y    x больше или равно y?
# x <= y    x меньше или равно y?
# x == y    x равно y?
# x != y    x не равно y?

# Операторы >= и <=.
# Два следующих оператора, >= и <=, выполняют проверку более одного отношения. Оператор >= определяет, является ли
# операнд с левой стороны больше или равняется операнду с правой стороны. Оператор <= определяет, является ли операнд с
# левой стороны меньше или равняется операнду с правой стороны.

# Оператор ==.
# Оператор == определяет, равняется ли операнд с левой стороны операнду с правой стороны. Если значения, на которые
# ссылаются оба операнда, одинаковые, то выражение является истинным.

# Оператор !=.
# Оператор != является оператором неравенства. Он определяет, не равняется ли операнд с левой стороны операнду с правой
# стороны, т.е. противоположен оператору ==.


# 3.2 Инструкция if-else
print('3.2 Инструкция if-else')
# Инструкция if-else исполняет один блок инструкций, если ее условие является истинным, либо другой блок, если ее
# условие является ложным.
# Общий формат инструкции if-else:
# if условие:
#   инструкция
#   инструкция
#   ...
# else:
#   инструкция
#   инструкция
#   ...
# Когда эта инструкция исполняется, осуществляется проверка условия. Если оно истинное, то исполняется блок инструкций с
# отступом, расположенный после условного выражения, затем поток управления программы перескакивает к инструкции,
# которая следует за инструкцией if-else. Если условие ложное, то исполняется блок инструкций с отступом, расположенный
# после выражения else, затем поток управления программы перескакивает к инструкции, которая следует за инструкцией
# if-else.

# Выделение отступом в инструкции if-else.
# Когда вы пишете инструкцию if-else, при выделении отступами следует руководствоваться следующими принципами:
# - убедитесь, что выражение if и выражение else выровнены относительно друг друга;
# - выражение if и выражение else сопровождаются блоком инструкций. Убедитесь, что инструкции в блоках расположены с
# одинаковым отступом.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

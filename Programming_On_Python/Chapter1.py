#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Глава 1
# Списки
bob = ['Bob Smith', 42, 30000, 'software']
print(bob)
sue = ['Sue Jones', 45, 40000, 'hardware']
print(sue)
print(bob[0], sue[2])  # вывод имени и оклада
# Разбиение поля по пробельному символу.
print(bob[0].split()[-1])  # вывод фамилии Боба
# Повышение оклада Сью на 25%
sue[2] *= 1.25
print(sue)  # вывод измененного списка

# База данных в виде списка
# Включение предыдущих списков в новый список:
people = [bob, sue]  # ссылки в списке списков
for person in people:
    print(person)
# Можно извлекать отдельные записи в соответствии с их позициями в списке и обрабатывать их в цикле:
print(people[1][0])
for person in people:
    print(person[0].split()[-1])  # вывод фамилии
    person[2] *= 1.20             # увеличение оклада на 20%
# Проверить новый размер оклада
for person in people:
    print(person[2])
# Теперь можно организовать выборку значений полей записей с помощью более мощных инструментов итераций, таких как
# генераторы списков, функция map и выражения-генераторы:
pays = [person[2] for person in people]  # выбор всех окладов
print(pays)
pays = map((lambda x: x[2]), people)  # тоже самое, функция map возвращает генератор
print(list(pays))
print(sum(person[2] for person in people))  # выражение-генератор, sum - встроенная функция
# Для добавления новых записей можно использовать append и extend:
people.append(['Tom', 50, 0, None])
print(len(people))
print(people[-1][0])

# Обращение к полям по именам.
# Используя встроенную функцию range, которая генерирует набор последовательных целых чисел при использовании в
# контексте итераций(таких как операция присваивания последовательности ниже):
NAME, AGE, PAY = range(3)  # 0, 1 и 2
bob = ['Bob Smith', 42, 10000]
print(bob[NAME])
print(PAY, bob[PAY])
# Использование списка списков
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
# Не решает проблему так как всё равно необходимо использовать числовые индексы
for person in people:
    print(person[0][1], person[2][1])  # имя, оклад
print([person[0][1] for person in people])  # вывод имен
for person in people:
    print(person[0][1].split()[-1])  # вывод фамилии
    person[2][1] *= 1.10             # повышение оклада на 10%
for person in people:
    print(person[2])
# Можно просматривать имена полей в цикле, отыскивая необходимые
# Поиск требуемого поля
for person in people:
    for (name, value) in person:
        if name == 'name':
            print(value)


# Функция выполняющая вышеперечисленные действия за нас
def field(record1, label):
    for (fname, fvalue) in record1:
        if fname == label:
            return fvalue


print(field(bob, 'name'))
print(field(sue, 'pay'))
for rec in people:
    print(field(rec, 'age'))  # вывод возраста всех людей в БД


# Словари
# Встроенные объекты словарей:
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
# Теперь bob и sue - это объекты, автоматически отображающие имена полей и их значения
print(bob['name'], sue['pay'])
print(bob['name'].split()[-1])
sue['pay'] *= 1.10
print(sue['pay'])

# Другие способы создания словарей
# Создание словаря вызовом конструктора с именованными аргументами, при этом все ключи будут строками
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
print(sue)
# Объединение двух списков, содержащих имена и значения:
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
list(zip(names, values))
print(sue)
# Словари можно создавать из последовательностей ключей и необязательного начального значения для всех ключей(удобно
# использовать для инициализации пустых словарей):
fields = ('name', 'age', 'pay', 'job')
record = dict.fromkeys(fields, '?')
print(record)

# Списки словарей
# Для сбора словарей-записей в БД можно использовать список, при условии, что там не требуется обеспечить доступ по
# ключу на верхнем уровне:
print(bob)
print(sue)
people = [bob, sue]  # ссылки в списке
for person in people:
    print(person['name'], person['pay'], sep=', ')  # вывод всех имен и окладов
for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])  # вывод оклада Сью
name = [person['name'] for person in people]  # выбирает имена
print(name)
print(list(map((lambda x: x['name']), people)))  # тоже самое
print(sum(person['pay'] for person in people))  # сумма всех окладов
# Генераторы списков и выражения-генераторы, способны приблизится по своему удобству к запросам в языке SQL, с тем
# отличием, что они манипулируют объектами в памяти:
print([rec['name'] for rec in people if rec['age'] >= 45])  # SQL-подобный запрос
print([(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people])
G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))
G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())
# Так как словари являются обычными объектами, то доступ к ним возможен с использованием привычного синтаксиса.
for person in people:
    print(person['name'].split()[-1])  # фамилия
    person['pay'] *= 1.10              # повышение на 10%

# Вложенные структуры
bob2 = {'name': {'first': 'Bob', 'last': 'Smith'}, 'age': 42, 'job': ['software', 'writing'], 'pay': (40000, 50000)}
print(bob2['name'])  # полное имя Боба
print(bob2['name']['last'])  # фамилия Боба
print(bob2['pay'][1])  # верхний предел оклада Боба
for job in bob2['job']:
    print(job)  # все должности, занимаемые Бобом
print(bob2['job'][-1])  # последняя должность Боба
bob2['job'].append('janitor')  # Боб получает новую должность
print(bob2)

# Словари словарей
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
db = dict()
db['bob'] = bob  # ссылки на словари в словаре
db['sue'] = sue
print(db['bob']['name'])  # извлечь имя Боба
db['sue']['pay'] = 50000  # изменить оклад Сью
print(db['sue']['pay'])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

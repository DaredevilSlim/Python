#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class User(object):

    count = 0

    def __init__(self, name, login, password, *args):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__admin = args
        User.count += 1

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    name = property(get_name, set_name)

    # Или
    # @property
    # def name(self):
    #    return self.__name
    # @name.setter
    # def name(self, value):
    #    self.__name = value

    def get_login(self):
        return self.__login

    def set_login(self, value):
        raise AttributeError('Нельзя менять значение!')

    login = property(get_login, set_login)

    # Или
    # @property
    # def login(self):
    #    return self.__login
    # @login.setter
    # def login(self, value):
    #    raise AttributeError('Нельзя менять значение!')

    def get_password(self):
        return '********'

    def set_password(self, value):
        self.__password = value

    password = property(get_password, set_password)

    # Или
    # @property
    # def password(self):
    #    return '********'
    # @password.setter
    # def password(self, value):
    #    self.__password = value

    def show_info(self):
        print(f'Name: {self.__name}, Login: {self.__login}')


class SuperUser(User):

    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        SuperUser.count += 1
        User.count -= 1

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):
        super().show_info()
        print(f'Role: {self.__role}')


user_1 = User('Paul McCartney', 'paul', '1234')
user_2 = User('George Harrison', 'george', '5678')
user_3 = User('Richard Starkey', 'ringo', '8523')
admin = SuperUser('John Lennon', 'john', '0000', 'admin')

user_1.show_info()  # Name: Paul McCartney, Login: paul
admin.show_info()   # Name: John Lennon, Login: john

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

user_3.name = 'Ringo Starr'
print(user_3.name)

print(user_2.login)
# user_2.login = 'geo'

user_1.password = 'Pa$$w0rd'
print(user_2.password)

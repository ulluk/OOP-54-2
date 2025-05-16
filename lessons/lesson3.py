# # инкапсуляция
# import random
#
# class BankAccount:
#
#     def __init__(self, user, balance, password):
#         self.user = user # Открытый
#         self._balance = balance # Защищенный
#         self.__password = password # Приватный
#
#     def get_password(self):
#         return self.__password
#     def __generate_pass(self):
#         return random.randint(1, 100)
#     def reset_password(self):
#         self.__password = self.__generate_pass()
# john = BankAccount('John', 1000, "123321")
#
# print(dir(john))

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         return print(f'{self.name} Gaf gaf')
#     def move(self):
#         return print(f'{self.name} move')
#
# tuzik = Dog("tuzik")
#
# print(tuzik.name)
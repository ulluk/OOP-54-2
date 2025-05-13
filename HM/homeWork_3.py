# class Student:
#     def __init__(self, name):
#         self.__name = name
#         self.__grade = 0
#
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#             return print("Оценка поставлена")
#         else:
#             return print("Оценка должна быть от 0 до 100")
#
#     def get_grate(self):
#         return self.__grade
#
#     def get_info(self):
#         return print(f"Имя: {self.__name}, Оценка: {self.__grade}")
#
#
# Molly = Student('Molly')
#
# Molly.set_grade(20)
#
# print(Molly.get_grate())
#
# Molly.get_info()



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius * self.radius)

class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def area(self):
        return self.heigth * self.width


figure_1 = Circle(4)
print(figure_1.area())

figure_2 = Square(12, 3)
print(figure_2.area())


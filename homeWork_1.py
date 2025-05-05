class Person:
    def __init__(self,name,age,city):
        self.name = name.title()
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мой age {self.age}, мой city {self.city}")
    def is_adult(self):
        if self.age >= 18:
            print(f"{self.name} совершеннолетний!")
        else:
            print("Вы не совершеннолетний!")
Bob = Person(name='bob', age=20, city='London')
Lary = Person(name='lary', age=13, city='Paris')
Molly = Person(name='molly', age=18, city='Bishkek')
Molly.introduce()
Bob.introduce()
Lary.introduce()
Bob.is_adult()
Lary.is_adult()
Molly.is_adult()


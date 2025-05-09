import random

class Heroes :

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f'{self.name} совершает действие')

    def attack(self):
        print(f'{self.name} атакует\nHP = {self.hp}')

class Archer(Heroes) :

    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows <= 0:
            print("Нет стрел для атаки!")
            return

        self.arrows -= 1

        chance = random.random()

        if chance <= self.precision:
            print("Атака успешна!")
        else:
            print("Атака неудачна.")

    def rest(self):
        if self.arrows > 10:
            print(f'Колчан полон')
        else:
            self.arrows += 5

    def status(self):
        print(f"Имя - {self.name}\n"
              f"HP - {self.hp}\n"
              f"Стрелы - {self.arrows}\n"
              f"Точность - {self.precision}")

legolas = Archer("Legolas", 100, 0, 0.2)
legolas.status()
legolas.rest()
legolas.status()
legolas.attack()
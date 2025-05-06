# Верблюжья нотация WarriorHero
# Змеиная нотация   warrior_hero

# Родительский класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def introduce(self):
        return print(f"Я {self.name}, мой уровень {self.lvl}")

    def action(self):
        return print(f"{self.name} выполняет действие")


# Дочерний класс
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def cast_spell(self):
        return print("Кастую огонь")
    def action(self):
        return print(f"{self.name} ничего не делает")
mage_hero = MageHero("Маг",100,100,1000)
mage_hero.action()

class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        print(f"Базовое действие {self.name}")

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100 , 1000)

kirito.action()
asuna.action()

print(asuna.hp_1)
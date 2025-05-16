

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "я магический метод"

test = Vector(12, 13)

print(test)
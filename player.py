import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.treasures = 0

    def find_treasure(self):
        self.treasures += 1
        print(f"{self.name} нашел сокровище! Текущее количество сокровищ: {self.treasures}")

    def encounter_trap(self):
        self.health -= random.randint(10, 30)
        print(f"{self.name} попал в ловушку! Здоровье: {self.health}")

    def is_alive(self):
        return self.health > 0

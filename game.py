import random

class Game:
    def __init__(self, player):
        self.player = player

    def start(self):
        print(f"Добро пожаловать, {self.player.name}! Исследуйте пещеру и найдите сокровища.")
        while self.player.is_alive():
            action = input("Идти налево или направо? (л/п): ")
            outcome = random.choice(['treasure', 'trap'])
            if action.lower() in ['л', 'налево']:
                if outcome == 'treasure':
                    self.player.find_treasure()
                else:
                    self.player.encounter_trap()
            elif action.lower() in ['п', 'направо']:
                if outcome == 'treasure':
                    self.player.find_treasure()
                else:
                    self.player.encounter_trap()
            else:
                print("Неверный выбор. Попробуйте снова.")
            if not self.player.is_alive():
                print("Игра окончена. Вы погибли в поисках сокровищ.")
                break


import random
from player import Player
from game import Game

player_name = input("Введите ваше имя: ")
player = Player(player_name)
game = Game(player)
game.start()
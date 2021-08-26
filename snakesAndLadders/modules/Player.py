from random import randrange


class Player:

    def __init__(self, player_name, cell_number=0):
        self.player_name = player_name
        self.cell_number = cell_number

    def make_move(self, dice_number):
        self.cell_number += dice_number
        print(f"{self.player_name} has moved to {self.cell_number}")

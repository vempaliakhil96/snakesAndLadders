from collections import deque
from modules.entities.Board import Board
from modules.Player import Player
from random import randrange


class Game:

    def __init__(self, number_of_players=2, board_dimension=20):

        self.number_of_players = number_of_players
        self.board_dimension = board_dimension
        self.turn_queue = deque()
        self.winner_queue = deque()
        self.game_board = Board(self.board_dimension)
        self.initialize_game()

    def initialize_game(self):
        for player_number in range(1, self.number_of_players+1, 1):
            player_name = input(f"Please enter the name of Player {player_number} : ")
            self.turn_queue.append(Player(player_name))
        pass

    def run(self):
        while len(self.winner_queue) == 0:
            player = self.turn_queue.popleft()
            print("--"*50)
            input(f"Please roll the dice {player.player_name}")
            dice_number = randrange(1, 7)
            print(f"{player.player_name} has got {dice_number}")
            if player.cell_number == 0 and dice_number == 6:
                player.make_move(1)
            elif player.cell_number == 0 and dice_number != 6:
                player.make_move(0)
            elif player.cell_number+dice_number > self.board_dimension**2:
                player.make_move(0)
            else:
                player.make_move(dice_number)
            current_cell = self.game_board.game_board[player.cell_number]
            if current_cell.is_cell_special():
                player.cell_number = current_cell.end
                current_cell.print_a_move()
            if player.cell_number == self.board_dimension**2:
                self.declare_winner(player)
                continue
            self.turn_queue.append(player)

    def declare_winner(self, player):
        self.winner_queue.append(player)
        print(f"{player.player_name} has won the game of Snakes and Ladders!!!")




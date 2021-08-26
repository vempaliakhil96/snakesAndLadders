from modules.entities.Cell import Cell
from modules.entities.Snake import Snake
from modules.entities.Ladder import Ladder
from random import randrange

number_of_snakes = 5
number_of_ladders = 5


class Board:

    def __init__(self, board_dimension):
        self.board_dimension = board_dimension
        self.game_board = {}
        self.random_cells = [randrange(self.board_dimension, self.board_dimension**2) for k in range(number_of_snakes+number_of_ladders)]
        self.snake_cells = self.random_cells[:3]
        self.ladder_cells = self.random_cells[-3:]
        self.initialize_board()

    def initialize_board(self):
        number_of_cells = self.board_dimension**2
        for cell_number in range(number_of_cells+1):
            if cell_number in self.snake_cells:
                self.game_board[cell_number] = (Snake(cell_number, 1))
                continue
            if cell_number in self.ladder_cells:
                self.game_board[cell_number] = (Ladder(cell_number, self.board_dimension**2))
                continue
            self.game_board[cell_number] = (Cell(cell_number))
        self.print_game_board()

    def print_game_board(self):
        print("Here is the Board")
        current_cell = self.board_dimension**2
        while current_cell != 0:
            current_cell_object = self.game_board[current_cell]
            if current_cell_object.is_cell_special():
                print(f"{current_cell}(e:{current_cell_object.end})".rjust(10), end="\t")
            else:
                print(f"{current_cell}".rjust(10), end="\t")
            if current_cell%self.board_dimension-1 == 0:
                print("\n")
            current_cell -= 1
        print("\n")



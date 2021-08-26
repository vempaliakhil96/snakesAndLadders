from modules import BoardEntity


class Cell:

    def __init__(self, cell_number, cell_type=BoardEntity.NORMAL.value):
        self.cell_number = cell_number
        self.cell_type = cell_type

    def is_cell_special(self):
        if self.cell_type == BoardEntity.NORMAL.value:
            return False
        return True

    def print_a_move(self):
        pass

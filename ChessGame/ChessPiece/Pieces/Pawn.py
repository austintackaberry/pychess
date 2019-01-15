from ..ChessPiece import ChessPiece
from termcolor import colored


class Pawn(ChessPiece):
    def __init__(self, team, loc):
        ChessPiece.__init__(self, team, loc)
        self.moved = False

    def is_valid_move(self, new_loc, board):
        if not ChessPiece.is_valid_move(self, new_loc, board, True):
            return False

        dist = 1
        if self.moved == False:
            dist = 2
        if self.team == 'blue':
            return new_loc[0] - self.curr_loc[0] <= dist and new_loc[1] == self.curr_loc[1]
        return new_loc[0] - self.curr_loc[0] >= -1*dist and new_loc[1] == self.curr_loc[1]

    def move(self, new_loc):
        self.moved = True
        ChessPiece.move(self, new_loc)

    def __str__(self):
        return colored('P', self.team)

from ..ChessPiece import ChessPiece
from termcolor import colored


class Bishop(ChessPiece):
    def __init__(self, team, loc):
        ChessPiece.__init__(self, team, loc)

    def is_valid_move(self, new_loc, board):
        if not ChessPiece.is_valid_move(self, new_loc, board, True):
            return False
        return abs(self.curr_loc[0] - new_loc[0]) == abs(self.curr_loc[1] - new_loc[1])

    def __str__(self):

        return colored('B', self.team)

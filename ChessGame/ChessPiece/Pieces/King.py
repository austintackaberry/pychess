from ..ChessPiece import ChessPiece
from termcolor import colored


class King(ChessPiece):
    def __init__(self, team, loc):
        ChessPiece.__init__(self, team, loc)

    def is_valid_move(self, new_loc, board):
        if not ChessPiece.is_valid_move(self, new_loc, board, False):
            return False
        return (new_loc[0] - self.curr_loc[0] <= abs(1)) and (new_loc[1] - self.curr_loc[1] <= abs(1))

    def __str__(self):
        return colored('K', self.team)

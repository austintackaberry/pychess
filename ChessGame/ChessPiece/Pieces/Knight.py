from ..ChessPiece import ChessPiece
from termcolor import colored


class Knight(ChessPiece):
    def __init__(self, team, loc):
        ChessPiece.__init__(self, team, loc)

    def is_valid_move(self, new_loc, board):
        if not ChessPiece.is_valid_move(self, new_loc, board, False):
            return False
        return (abs(self.curr_loc[0] - new_loc[0]) == 2 and abs(self.curr_loc[1] - new_loc[1]) == 1) or (abs(self.curr_loc[0] - new_loc[0]) == 1 and abs(self.curr_loc[1] - new_loc[1]) == 2)

    def __str__(self):
        return colored('H', self.team)

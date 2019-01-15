from ..ChessPiece import ChessPiece
from termcolor import colored


class Knight(ChessPiece):
    def __init__(self, team, loc):
        ChessPiece.__init__(self, team, loc)

    def is_valid_move(self, new_loc):
        if not ChessPiece.is_valid_move(self, new_loc):
            return False
        return (self.curr_loc[0] - new_loc[0] == abs(2) and self.curr_loc[1] - new_loc[1] == abs(1)) or (self.curr_loc[0] - new_loc[0] == abs(1) and self.curr_loc[1] - new_loc[1] == abs(2))

    def __str__(self):
        return colored('K', self.team)

class ChessPiece:
    def __init__(self, team, loc):
        self.team = team
        self.curr_loc = loc

    def is_valid_move(self, new_loc, board):
        dest = board[new_loc[0]][new_loc[1]]
        if new_loc[0] < 0 or new_loc[0] > 7 or new_loc[1] < 0 or new_loc[1] < 7 or (dest and self.team == dest.team):
            return False
        return True

    def move(self, new_loc):
        self.curr_loc = new_loc

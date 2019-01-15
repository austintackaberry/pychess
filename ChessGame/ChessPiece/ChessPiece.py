class ChessPiece:
    def __init__(self, team, loc):
        self.team = team
        self.curr_loc = loc

    def is_valid_move(self, new_loc, board, cm):
        dest = board[new_loc[0]][new_loc[1]]
        if new_loc[0] < 0 or new_loc[0] > 7 or new_loc[1] < 0 or new_loc[1] > 7 or (dest != 'x' and self.team == dest.team):
            return False
        if cm:
            i = self.curr_loc[0]
            j = self.curr_loc[1]
            while i != new_loc[0] and j != new_loc[1]:
                if i != new_loc[0]:
                    i += (new_loc[0] - i) // \
                        abs(new_loc[0] - i)
                if j != new_loc[1]:
                    j += (new_loc[1] - j) // \
                        abs(new_loc[1] - j)
                if board[i][j] != 'x':
                    return False

        return True

    def move(self, new_loc):
        self.curr_loc = new_loc

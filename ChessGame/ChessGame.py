from .ChessPiece.ChessPiece import ChessPiece
from .ChessPiece.Pieces.Rook import Rook
from .ChessPiece.Pieces.Knight import Knight
from .ChessPiece.Pieces.Bishop import Bishop
from .ChessPiece.Pieces.Queen import Queen
from .ChessPiece.Pieces.King import King
from .ChessPiece.Pieces.Pawn import Pawn


class ChessGame:
    def __init__(self):
        self.teams = ('blue', 'green')
        self.index_team_turn = 0
        self.winner = False
        self.board = [8*['x'] for i in range(8)]
        self.board[0][0] = Rook(self.teams[0], [0, 0])
        self.board[0][1] = Knight(self.teams[0], [0, 1])
        self.board[0][2] = Bishop(self.teams[0], [0, 2])
        self.board[0][3] = King(self.teams[0], [0, 3])
        self.board[0][4] = Queen(self.teams[0], [0, 4])
        self.board[0][5] = Bishop(self.teams[0], [0, 5])
        self.board[0][6] = Knight(self.teams[0], [0, 6])
        self.board[0][7] = Rook(self.teams[0], [0, 7])
        self.board[1][0] = Pawn(self.teams[0], [1, 0])
        self.board[1][1] = Pawn(self.teams[0], [1, 1])
        self.board[1][2] = Pawn(self.teams[0], [1, 2])
        self.board[1][3] = Pawn(self.teams[0], [1, 3])
        self.board[1][4] = Pawn(self.teams[0], [1, 4])
        self.board[1][5] = Pawn(self.teams[0], [1, 5])
        self.board[1][6] = Pawn(self.teams[0], [1, 6])
        self.board[1][7] = Pawn(self.teams[0], [1, 7])

        self.board[6][0] = Pawn(self.teams[1], [6, 0])
        self.board[6][1] = Pawn(self.teams[1], [6, 1])
        self.board[6][2] = Pawn(self.teams[1], [6, 2])
        self.board[6][3] = Pawn(self.teams[1], [6, 3])
        self.board[6][4] = Pawn(self.teams[1], [6, 4])
        self.board[6][5] = Pawn(self.teams[1], [6, 5])
        self.board[6][6] = Pawn(self.teams[1], [6, 6])
        self.board[6][7] = Pawn(self.teams[1], [6, 7])
        self.board[7][0] = Rook(self.teams[1], [7, 0])
        self.board[7][1] = Knight(self.teams[1], [7, 1])
        self.board[7][2] = Bishop(self.teams[1], [7, 2])
        self.board[7][3] = Queen(self.teams[1], [7, 3])
        self.board[7][4] = King(self.teams[1], [7, 4])
        self.board[7][5] = Bishop(self.teams[1], [7, 5])
        self.board[7][6] = Knight(self.teams[1], [7, 6])
        self.board[7][7] = Rook(self.teams[1], [7, 7])

    def start(self):
        self.print_board()
        print('Welcome! If it is your turn, type the location of the piece you want to move and where you want to move it.')
        print('For example: "A1 B3"\n')
        while not self.winner:
            self.turn()
            self.print_board()
        print('Team ' + self.winner + " won!!!")

    def turn(self):
        team_turn = self.teams[self.index_team_turn]
        ans = input('It is team ' + team_turn + "'s turn: ")
        curr_loc, new_loc = map(convert, ans.split(' '))
        if curr_loc[0] < 0 or curr_loc[0] > 7 or curr_loc[1] < 0 or curr_loc[1] > 7 or new_loc[0] < 0 or new_loc[0] > 7 or new_loc[1] < 0 or new_loc[1] > 7:
            print('At least one of the two locations is outside of the board')
            return
        piece = self.board[curr_loc[0]][curr_loc[1]]
        if piece != 'x' and piece.is_valid_move(new_loc, self.board):
            piece.move(new_loc)
            dest_piece = self.board[new_loc[0]][new_loc[1]]
            if isinstance(dest_piece, King):
                self.winner = self.teams[self.index_team_turn]
            self.board[new_loc[0]][new_loc[1]] = piece
            self.board[curr_loc[0]][curr_loc[1]] = 'x'
            self.team_turn_index = (self.team_turn_index + 1) % 2

    def print_board(self):
        p_str = "    A  B  C  D  E  F  G  H\n  ________________________\n"
        for i in range(len(self.board)):
            p_str += str(len(self.board) - i) + " |"
            for j in range(len(self.board[i])):
                p_str += ' ' + str(self.board[i][j]) + " "
            p_str += '\n'
        print(p_str)


def convert(loc):
    return [8 - int(loc[1]), ord(loc[0]) - 65]

from .ChessPiece.ChessPiece import ChessPiece
from .ChessPiece.Pieces.Rook import Rook
from .ChessPiece.Pieces.Knight import Knight
from .ChessPiece.Pieces.Bishop import Bishop
from .ChessPiece.Pieces.Queen import Queen
from .ChessPiece.Pieces.King import King


class ChessGame:
    def __init__(self):
        self.team_turn = 'blue'
        self.board = [8*['x'] for i in range(8)]
        self.board[0][0] = Rook('blue', [0, 0])
        self.board[0][1] = Knight('blue', [0, 1])
        self.board[0][2] = Bishop('blue', [0, 2])
        self.board[0][3] = Queen('blue', [0, 3])
        self.board[0][4] = King('blue', [0, 4])
        self.board[0][5] = Bishop('blue', [0, 5])
        self.board[0][6] = Knight('blue', [0, 6])
        self.board[0][7] = Rook('blue', [0, 7])

        self.board[7][0] = Rook('green', [7, 0])
        self.board[7][1] = Knight('green', [7, 1])
        self.board[7][2] = Bishop('green', [7, 2])
        self.board[7][3] = Queen('green', [7, 3])
        self.board[7][4] = King('green', [7, 4])
        self.board[7][5] = Bishop('green', [7, 5])
        self.board[7][6] = Knight('green', [7, 6])
        self.board[7][7] = Rook('green', [7, 7])

    def start(self):
        self.print_board()

    def print_board(self):
        p_str = "    A  B  C  D  E  F  G  H\n  ________________________\n"
        for i in range(len(self.board)):
            p_str += str(len(self.board) - i) + " |"
            for j in range(len(self.board[i])):
                p_str += ' ' + str(self.board[i][j]) + " "
            p_str += '\n'
        print(p_str)

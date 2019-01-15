from .ChessPiece.ChessPiece import ChessPiece
from .ChessPiece.Pieces.Rook import Rook


class ChessGame:
    def __init__(self):
        self.team_turn = 'blue'
        self.board = [8*['x'] for i in range(8)]
        self.board[0][0] = Rook('blue', [0, 0])
        self.board[0][7] = Rook('blue', [0, 7])
        self.board[7][0] = Rook('green', [7, 0])
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

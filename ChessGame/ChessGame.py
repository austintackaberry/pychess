class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ChessGame:
    def __init__(self):
        self.team_turn = 'blue'
        self.board = [8*['x'] for i in range(8)]

    def start(self):
        self.print_board()

    def print_board(self):
        p_str = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                p_str += ' ' + self.board[i][j] + " "
            p_str += '\n'
        print(p_str)

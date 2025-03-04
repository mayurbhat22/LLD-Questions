from src.playingpiece import PlayingPiece

class Board:
    def __init__(self, size):
        self.size = size
        self.game_board = [[" " for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.game_board:
            print(" | ".join(cell.piece_type if isinstance(cell, PlayingPiece) else " " for cell in row))
            print("-" * (self.size * 4 - 1))  # Print horizontal separator

    def add_piece(self, piece, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        if self.game_board[row][col] != " ":
            return False
        
        self.game_board[row][col] = piece
        return True

    def check_winner(self, piece):
        for i in range(self.size):
            if all([self.game_board[i][j] == piece for j in range(self.size)]):
                return True
            if all([self.game_board[j][i] == piece for j in range(self.size)]):
                return True
        
        if all([self.game_board[i][i] == piece for i in range(self.size)]):
            return True
        if all([self.game_board[i][self.size - i - 1] == piece for i in range(self.size)]):
            return True
        
        return False
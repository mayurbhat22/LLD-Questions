from collections import deque
from src.board import Board
from src.player import Player
from src.pieceX import PieceX
from src.pieceO import PieceO

class TicTacToe:
    def __init__(self):
        self.players_list = deque()
        self.game_board = Board(3)
        self.initialize_game()
    
    def initialize_game(self):
        piecex = PieceX()
        pieceo = PieceO()

        player1 = Player("Player 1", piecex)
        player2 = Player("Player 2", pieceo)

        self.players_list.append(player1)
        self.players_list.append(player2)

    def game_start(self):
        print("Game Start!")

        no_winner = True

        while no_winner:
            self.game_board.print_board()
            current_player = self.players_list.popleft()

            print(f"{current_player.name}'s turn")
            s = input("Enter row, column: ")
            row, col = s.split(",")
            row = int(row)
            col = int(col)

            piece_added = self.game_board.add_piece(current_player.piece, row, col)
            if not piece_added:
                print("Invalid move. Try again.")
                self.players_list.appendleft(current_player)
                continue

            self.players_list.append(current_player)
            game_over = self.is_winner(current_player)
            if not game_over:
                continue
            else:
                print(f"{current_player.name} wins!")
                return
    
    def is_winner(self, current_player):
        return self.game_board.check_winner(current_player.piece)
    
    


        
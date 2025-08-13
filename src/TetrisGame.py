from src.Board import Board
from src.Game import Game
from src.Tetromino import Tetromino
import random


class TetrisGame(Game):
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.Tetromino = self.generate_tetromino()
        self.current_tetromino = random.choice(list(Tetromino))
        self.next_tetromino = random.choice(list(Tetromino))
        self.current_position = (width // 2, 0)
        self.score = 0

    def generate_tetromino(self):
        return random.choice(list(Tetromino))

    def result(self, state, move):
        """Return the state that results from making a move."""
        new_board = state.new({})
        new_board.place_tetromino(self.current_tetromino, move)
        cleared_rows = new_board.clear_rows()
        self.score += 50 * cleared_rows
        if cleared_rows > 1:
            self.score += int((cleared_rows * 0.1) * self.width * cleared_rows)
        self.current_tetromino = random.choice(list(Tetromino))
        self.current_position = (state.width // 2, 0)
        return new_board

    def move_tetromino(self, direction):
        """Move the current tetromino in the given direction."""
        new_position = (self.current_position[0] + direction[0], self.current_position[1] + direction[1])
        if not self.board.check_collision(self.current_tetromino, new_position):
            self.current_position = new_position
            return True
        return False

    def place_tetromino(self):
        """Place the current tetromino on the board and update the next piece."""
        for x, y in self.current_tetromino.value:
            board_x = self.current_position[0] + x
            board_y = self.current_position[1] + y
            self.board.set_cell(board_x, board_y, 1)

        self.current_tetromino = self.next_tetromino
        self.next_tetromino = random.choice(list(Tetromino))

        self.current_position = (self.width // 2, 0)
        self.score = self.score + 10

    def clear_rows(self):
        full_rows = [y for y in range(self.board.height) if
                     all(self.board.get_cell(x, y) == 1 for x in range(self.board.width))]

        for row in full_rows:
            for y in range(row, 0, -1):
                for x in range(self.board.width):
                    self.board.set_cell(x, y, self.board.get_cell(x, y - 1))
            # Clear the top row
            for x in range(self.board.width):
                self.board.set_cell(x, 0, 0)

        rows_cleared = len(full_rows)
        if rows_cleared > 0:
            base_score = rows_cleared * 100
            bonus = int(base_score * 0.1 * rows_cleared)
            self.score += base_score + bonus

    def is_game_over(self):
        for cell in self.board.grid[0]:
            if cell != 0:
                self.game_over = True
                return True
        return False
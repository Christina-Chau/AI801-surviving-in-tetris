import random

import pygame
from src.TetrisGame import TetrisGame
from src.Tetromino import Tetromino


class GameScreen:
    def __init__(self, game: TetrisGame, cell_size=10):
        self.game = game
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((game.width * cell_size, game.height * cell_size))
        pygame.display.set_caption("Tetris")

    def draw_board(self):
        for y in range(self.game.board.height):
            for x in range(self.game.board.width):
                color = (255, 255, 255) if self.game.board.get_cell(x, y) == 0 else (0, 255, 0)
                pygame.draw.rect(self.screen, color,
                                 (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
    def draw_tetromino(self):
        for x, y in self.game.current_tetromino.value:
            x += self.game.current_position[0]
            y += self.game.current_position[1]
            pygame.draw.rect(self.screen, (255, 0, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def play(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        fall_speed = 2

        while running:
            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.draw_tetromino()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.game.move_tetromino((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.game.move_tetromino((1, 0))
                    elif event.key == pygame.K_DOWN:
                        self.game.move_tetromino((0, 1))

            # Automatically move Tetromino down
            if not self.game.move_tetromino((0, 1)):
                self.game.place_tetromino()
                self.game.clear_rows()
                self.game.current_tetromino = random.choice(list(Tetromino))
                self.game.current_position = (self.game.width // 2, 0)
                if self.game.is_game_over():
                    print("Game Over! Final Score:", self.game.score)
                    running = False

            pygame.display.flip()
            clock.tick(fall_speed)

        pygame.quit()
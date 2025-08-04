from src.TetrisGame import TetrisGame
from src.GameScreen import GameScreen

if __name__ == "__main__":
    game = TetrisGame()
    screen = GameScreen(game)
    screen.play()
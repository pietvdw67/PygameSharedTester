import sys

import pygame

from game import game_state
from game.game_state import GameState
from game.game import Game
from constants import Constants

pygame.init()


class Main:
    def __init__(self):
        self.game_state = GameState()
        self.screen = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))


    def run(self):
        game = Game(self.screen, self.game_state)
        self.game_state.running = True
        game.run_loop()

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Main().run()

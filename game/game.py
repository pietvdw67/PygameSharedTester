import pygame
import os

from pygame_shared.utils.image_utils import ImageUtils
from constants import Constants
from pygame_shared.animation.animation_controller import AnimationController

pygame.init()



class Game:

    FONT = pygame.font.SysFont("Consolas", 60)

    def __init__(self, screen, game_state):
        self.screen = screen
        self.game_state = game_state
        self.player_animation_controller = AnimationController()
        self.load_animations()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.player_animation_controller.set_active_animation("idle")

                if event.key == pygame.K_2:
                    self.player_animation_controller.set_active_animation("run")

                if event.key == pygame.K_3:
                    self.player_animation_controller.set_active_animation("double_jump")

                if event.key == pygame.K_4:
                    self.player_animation_controller.set_active_animation("fall")


    def draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.player_animation_controller.get_image(),(100,100))


        pygame.display.flip()

    def run_loop(self):
        while self.game_state.running:
            dt = self.game_state.clock.tick(60)

            self.handle_events()

            self.draw()


    def make_number_frames(self):
        for i in range(0, 10):
            text = Game.FONT.render(str(i), 1, "white")
            number_surface = pygame.Surface((text.get_width(), text.get_height()), pygame.SRCALPHA, 32)
            print(f"number: {i} width: {text.get_width()} height: {text.get_height()}")
            number_surface.blit(text, (0, 0))
            pygame.image.save(number_surface, os.path.join("D:/", "tmp", f"{str(i)}.png"))

    def load_animations(self):
        sheet = os.path.join(Constants.ASSETS_PATH, "spritesheets", "run.png")
        images = ImageUtils.get_animation_frames_from_sprite_sheet(
            sheet_name=sheet,
            cols=12,
            rows=1,
            scale=3
        )
        self.player_animation_controller.load_animation("run", images, 4)

        sheet = os.path.join(Constants.ASSETS_PATH, "spritesheets", "idle.png")
        images = ImageUtils.get_animation_frames_from_sprite_sheet(
            sheet_name=sheet,
            cols=11,
            rows=1,
            scale=3
        )
        self.player_animation_controller.load_animation("idle", images, 5)

        sheet = os.path.join(Constants.ASSETS_PATH, "spritesheets", "double_jump.png")
        images = ImageUtils.get_animation_frames_from_sprite_sheet(
            sheet_name=sheet,
            cols=6,
            rows=1,
            scale=3
        )
        self.player_animation_controller.load_animation("double_jump", images, 7)

        sheet = os.path.join(Constants.ASSETS_PATH, "spritesheets", "fall.png")
        images = ImageUtils.get_animation_frames_from_sprite_sheet(
            sheet_name=sheet,
            cols=1,
            rows=1,
            scale=3
        )
        self.player_animation_controller.load_animation("fall", images)




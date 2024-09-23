import pygame

G_SCREEN_WIDTH = 800
G_SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((G_SCREEN_WIDTH, G_SCREEN_HEIGHT))

class Display:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.clock = pygame.time.Clock()

        self.background_surf = pygame.transform.scale(
            pygame.image.load("images/Tiles/Backgrounds/main_background.png").convert_alpha(),
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT - 100))
        self.background_rect = self.background_surf.get_rect(topleft = (0, 0))

        self.ground_surf = pygame.transform.scale(
            pygame.image.load("images/Tiles/second_new.png").convert_alpha(),
            (self.SCREEN_WIDTH, 100))
        self.ground_rect = self.ground_surf.get_rect(topleft = (0, 500))

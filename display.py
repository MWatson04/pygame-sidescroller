import pygame

# Pygame Display Information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Scroller")
clock = pygame.time.Clock()

background_surf = pygame.transform.scale(
    pygame.image.load("images/Tiles/Backgrounds/main_background.png").convert_alpha(),
    (SCREEN_WIDTH, SCREEN_HEIGHT - 100))
background_rect = background_surf.get_rect(topleft = (0, 0))

ground_surf = pygame.transform.scale(
    pygame.image.load("images/Tiles/second_new.png").convert_alpha(),
    (SCREEN_WIDTH, 100))
ground_rect = ground_surf.get_rect(topleft = (0, 500))

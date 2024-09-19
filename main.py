import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

background_surf = pygame.transform.scale(
    pygame.image.load("images/Tiles/Backgrounds/main_background.png").convert_alpha(),
    (SCREEN_WIDTH, SCREEN_HEIGHT - 100))
background_rect = background_surf.get_rect(topleft = (0, 0))

ground_surf = pygame.transform.scale(
    pygame.image.load("images/Tiles/second_new.png").convert_alpha(),
    (800, 100))
ground_rect = ground_surf.get_rect(topleft = (0, 500))

player_surf = pygame.image.load("images/Tiles/Characters/main_character.png").convert_alpha()
player_surf = pygame.transform.scale_by(player_surf, 3)
player_surf = pygame.transform.flip(player_surf, 180, 0)
player_rect = player_surf.get_rect(midbottom = (50, background_surf.get_height()))

font = pygame.font.Font('fonts/Modenine-2OPd.ttf', 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    screen.blit(background_surf, background_rect)
    screen.blit(ground_surf, ground_rect)
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(60)
    
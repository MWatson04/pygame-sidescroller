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
player_rect = player_surf.get_rect(midbottom = (75, background_surf.get_height()))
player_gravity = 0

walking_enemy_surf = pygame.transform.scale_by(
    pygame.image.load("images/Tiles/Characters/main_enemy.png").convert_alpha(),
    3)
walking_enemy_rect = walking_enemy_surf.get_rect(bottomright = (SCREEN_WIDTH, background_surf.get_height()))
walking_enemy_speed = 5

font = pygame.font.Font("fonts/Modenine-2OPd.ttf", 40)
score_surf = font.render("SCORE: 0", True, "Black")
score_rect = score_surf.get_rect(center = (125, 50))
start_game_surf = font.render("Press 'Space' to Start", True, "Black")
start_game_rect = start_game_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

in_start_menu = True
game_playing = False
in_game_over_menu = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if in_start_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                in_start_menu = False
                game_playing = True

        if game_playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == background_surf.get_height():
                    player_gravity -= 15
        elif in_game_over_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                walking_enemy_rect.left = SCREEN_WIDTH + 20
                game_playing = True

    if in_start_menu:
        screen.fill((0, 0, 0))

        screen.blit(background_surf, background_rect)
        screen.blit(ground_surf, ground_rect)
        screen.blit(start_game_surf, start_game_rect)

    if game_playing:
        screen.fill((0, 0, 0))

        screen.blit(background_surf, background_rect)
        screen.blit(ground_surf, ground_rect)

        player_gravity += 0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= background_surf.get_height():
            player_rect.bottom = background_surf.get_height()
            player_gravity = 0
        screen.blit(player_surf, player_rect)

        walking_enemy_rect.x -= walking_enemy_speed
        if walking_enemy_rect.right < -20:
            walking_enemy_rect.left = SCREEN_WIDTH + 20
        screen.blit(walking_enemy_surf, walking_enemy_rect)
        
        screen.blit(score_surf, score_rect)

        if player_rect.colliderect(walking_enemy_rect):
            game_playing = False
            in_game_over_menu = True
    elif in_game_over_menu:
        screen.fill("Blue")

    pygame.display.update()
    clock.tick(60)
    
import pygame
from sys import exit

pygame.init()

def update_score():
    current_score = (pygame.time.get_ticks() // 125) - score_start_time
    score_surf = main_font.render(f"SCORE: {current_score}", True, "Black")
    score_rect = score_surf.get_rect(center = (125, 50))
    screen.blit(score_surf, score_rect)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pixel Scroller')
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

main_font = pygame.font.Font("fonts/Modenine-2OPd.ttf", 40)
second_font = pygame.font.Font("fonts/Modenine-2OPd.ttf", 20)

start_game_surf = second_font.render("Press 'Space' to Start", True, "Black")
start_game_rect = start_game_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

instructions_surf = second_font.render("You can press 'Esc' at any time to pause the game", True, "Black")
instructions_rect = instructions_surf.get_rect(center = (SCREEN_WIDTH / 2, 380))

game_title_surf = main_font.render("PIXEL SCROLLER", True, "Black")
game_title_rect = game_title_surf.get_rect(center = (SCREEN_WIDTH / 2, 250))

restart_game_surf = second_font.render("Press 'Space' to Play Again", True, "Black")
restart_game_rect = start_game_surf.get_rect(center = (SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT / 2))

quit_game_surf = second_font.render("Press 'Q' to Exit", True, "Black")
quit_game_rect = quit_game_surf.get_rect(center = (SCREEN_WIDTH / 2, 340))

game_over_surf = main_font.render("GAME OVER", True, "Black")
game_over_rect = game_title_surf.get_rect(center = (SCREEN_WIDTH / 2 + 60, 250))

pause_menu_surf = main_font.render("PAUSE", True, "Black")
pause_menu_rect = pause_menu_surf.get_rect(center = (SCREEN_WIDTH / 2, 250))

resume_game_surf = second_font.render("Press 'Space' to Resume", True, "Black")
resume_game_rect = resume_game_surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

score_start_time = 0
in_start_menu = True
game_playing = False
in_pause_menu = False
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
                score_start_time = pygame.time.get_ticks() // 125
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()
        elif game_playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == background_surf.get_height():
                    player_gravity -= 15
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                game_playing = False
                in_pause_menu = True
        elif in_pause_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                in_pause_menu = False
                game_playing = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()
        elif in_game_over_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                walking_enemy_rect.left = SCREEN_WIDTH + 20
                game_playing = True
                score_start_time = pygame.time.get_ticks() // 125
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                exit()

    if in_start_menu:
        screen.fill((0, 0, 0))

        screen.blit(background_surf, background_rect)
        screen.blit(ground_surf, ground_rect)
        screen.blit(game_title_surf, game_title_rect)
        screen.blit(start_game_surf, start_game_rect)
        screen.blit(quit_game_surf, quit_game_rect)
        screen.blit(instructions_surf, instructions_rect)

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
        
        update_score()

        if player_rect.colliderect(walking_enemy_rect):
            game_playing = False
            in_game_over_menu = True
    elif in_pause_menu:
        screen.fill((0, 0, 0))

        screen.blit(background_surf, background_rect)
        screen.blit(ground_surf, ground_rect)
        screen.blit(pause_menu_surf, pause_menu_rect)
        screen.blit(resume_game_surf, resume_game_rect)
        screen.blit(quit_game_surf, quit_game_rect)
    elif in_game_over_menu:
        screen.fill((0, 0, 0))

        screen.blit(background_surf, background_rect)
        screen.blit(ground_surf, ground_rect)
        screen.blit(game_over_surf, game_over_rect)
        screen.blit(restart_game_surf, restart_game_rect)
        screen.blit(quit_game_surf, quit_game_rect)

    pygame.display.update()
    clock.tick(60)
    
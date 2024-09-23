import display
import player
import enemy
from sys import exit
from random import randint

display_obj = display.Display()
player_obj = player.Player()
walking_enemy_obj = enemy.WalkingEnemy()
flying_enemy_obj = enemy.FlyingEnemy()

class Engine:
    def __init__(self):
        self.score_reset = 0
        self.pause_start = 0
        self.pause_duration = 0
        self.in_start_menu = True
        self.game_playing = False
        self.in_pause_menu = False
        self.in_game_over_menu = False
        self.current_score = 0

        self.main_font = display.pygame.font.Font("fonts/Modenine-2OPd.ttf", 40)
        self.second_font = display.pygame.font.Font("fonts/Modenine-2OPd.ttf", 20)

        self.start_game_surf = self.second_font.render("Press 'Space' to Start", True, "Black")
        self.start_game_rect = self.start_game_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, display_obj.SCREEN_HEIGHT / 2))

        self.instructions_surf = self.second_font.render("You can press 'Esc' at any time to pause the game", True, "Black")
        self.instructions_rect = self.instructions_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 380))

        self.game_title_surf = self.main_font.render("PIXEL SCROLLER", True, "Black")
        self.game_title_rect = self.game_title_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 250))

        self.restart_game_surf = self.second_font.render("Press 'Space' to Play Again", True, "Black")
        self.restart_game_rect = self.start_game_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2 - 25, display_obj.SCREEN_HEIGHT / 2))

        self.quit_game_surf = self.second_font.render("Press 'Q' to Exit", True, "Black")
        self.quit_game_rect = self.quit_game_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 340))

        self.game_over_surf = self.main_font.render("GAME OVER", True, "Black")
        self.game_over_rect = self.game_title_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2 + 60, 250))

        self.pause_menu_surf = self.main_font.render("PAUSE", True, "Black")
        self.pause_menu_rect = self.pause_menu_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 250))

        self.resume_game_surf = self.second_font.render("Press 'Space' to Resume", True, "Black")
        self.resume_game_rect = self.resume_game_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, display_obj.SCREEN_HEIGHT / 2))

    # Poll for all events
    def event_catcher(self):
        for event in display.pygame.event.get():
            if event.type == display.pygame.QUIT:
                display.pygame.quit()
                exit()

            if self.in_start_menu:
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_SPACE:
                    self.in_start_menu = False
                    self.game_playing = True
                    self.score_reset = display.pygame.time.get_ticks() // 125
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_q:
                    display.pygame.quit()
                    exit()
            elif self.game_playing:
                if event.type == display.pygame.KEYDOWN:
                    if event.key == display.pygame.K_SPACE and player_obj.player_rect.bottom == display_obj.background_surf.get_height():
                        player_obj.player_gravity -= 15
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_ESCAPE:
                    self.game_playing = False
                    self.in_pause_menu = True
                    self.pause_start = display.pygame.time.get_ticks() // 125
            elif self.in_pause_menu:
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_SPACE:
                    self.in_pause_menu = False
                    self.game_playing = True
                    self.pause_duration += (display.pygame.time.get_ticks() // 125) - self.pause_start
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_q:
                    display.pygame.quit()
                    exit()
            elif self.in_game_over_menu:
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_SPACE:
                    walking_enemy_obj.walking_enemy_rect.left = display_obj.SCREEN_WIDTH + 20
                    flying_enemy_obj.flying_enemy_rect.left = display_obj.SCREEN_WIDTH + 50
                    self.game_playing = True
                    self.score_reset = display.pygame.time.get_ticks() // 125
                    self.pause_duration = 0
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_q:
                    display.pygame.quit()
                    exit()

    def update_score(self):
        current_score = (display.pygame.time.get_ticks() // 125) - self.score_reset - self.pause_duration
        score_surf = self.main_font.render(f"SCORE: {current_score}", True, "Black")
        score_rect = score_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 50))
        display_obj.screen.blit(score_surf, score_rect)

    def draw_background(self):
        display_obj.screen.blit(display_obj.background_surf, display_obj.background_rect)
        display_obj.screen.blit(display_obj.ground_surf, display_obj.ground_rect)

    def draw_start_menu(self):
        display_obj.screen.blit(self.game_title_surf, self.game_title_rect)
        display_obj.screen.blit(self.start_game_surf, self.start_game_rect)
        display_obj.screen.blit(self.quit_game_surf, self.quit_game_rect)
        display_obj.screen.blit(self.instructions_surf, self.instructions_rect)

    def draw_pause_menu(self):
        display_obj.screen.blit(self.pause_menu_surf, self.pause_menu_rect)
        display_obj.screen.blit(self.resume_game_surf, self.resume_game_rect)
        display_obj.screen.blit(self.quit_game_surf, self.quit_game_rect)

    def draw_game_over_menu(self):
        display_obj.screen.blit(self.game_over_surf, self.game_over_rect)
        display_obj.screen.blit(self.restart_game_surf, self.restart_game_rect)
        display_obj.screen.blit(self.quit_game_surf, self.quit_game_rect)

    def draw_characters(self):
        display_obj.screen.blit(player_obj.player_surf, player_obj.player_rect)
        display_obj.screen.blit(walking_enemy_obj.walking_enemy_surf, walking_enemy_obj.walking_enemy_rect)
        display_obj.screen.blit(flying_enemy_obj.flying_enemy_surf, flying_enemy_obj.flying_enemy_rect)

    def run_game(self):
        self.event_catcher()

        if self.in_start_menu:
            self.draw_background()
            self.draw_start_menu()
        elif self.game_playing:
            self.draw_background()

            player_obj.player_gravity += 0.5
            player_obj.player_rect.y += player_obj.player_gravity
            if player_obj.player_rect.bottom >= display_obj.background_surf.get_height():
                player_obj.player_rect.bottom = display_obj.background_surf.get_height()
                player_obj.player_gravity = 0

            walking_enemy_obj.walking_enemy_rect.x -= walking_enemy_obj.walking_enemy_speed
            if walking_enemy_obj.walking_enemy_rect.right < -20:
                walking_enemy_obj.walking_enemy_rect.left = display_obj.SCREEN_WIDTH + randint(1, 75)

        flying_enemy_obj.flying_enemy_rect.x -= flying_enemy_obj.flying_enemy_speed
        if flying_enemy_obj.flying_enemy_rect.right < - 20:
            flying_enemy_obj.flying_enemy_rect.left = display_obj.SCREEN_WIDTH + randint(100, 175)
        
        self.draw_characters()
        self.update_score()

        if player_obj.player_rect.colliderect(walking_enemy_obj.walking_enemy_rect):
            self.game_playing = False
            self.in_game_over_menu = True
        if player_obj.player_rect.colliderect(flying_enemy_obj.flying_enemy_rect):
            self.game_playing = False
            self.in_game_over_menu = True
        elif self.in_pause_menu:
            self.draw_background()
            self.draw_pause_menu()
        elif self.in_game_over_menu:
            self.draw_background()
            self.draw_game_over_menu()
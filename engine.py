import display
import player
import enemy
import score
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
        self.current_high_score = score.get_high_score()

        # Music
        # self.start_menu_music = display.pygame.mixer.Sound("sounds/arcade-party-173553.mp3")
        # self.start_menu_music.set_volume(0.5)
        self.game_playing_music = display.pygame.mixer.Sound("sounds/music-for-arcade-style-game-146875.mp3")
        self.game_playing_music.set_volume(0.5)
        self.game_playing_music.play(loops = -1)

        # All Fonts/Text Surfs/Rects------------------------------------------------------------------------------------
        self.main_font = display.pygame.font.Font("fonts/Modenine-2OPd.ttf", 50)
        self.second_font = display.pygame.font.Font("fonts/Modenine-2OPd.ttf", 23)

        self.start_game_surf = self.second_font.render("Press 'Space' to Start", True, "Black")
        self.start_game_rect = self.start_game_surf.get_rect(
            center = (display_obj.SCREEN_WIDTH / 2, display_obj.SCREEN_HEIGHT / 2))

        self.pause_instructions_surf = self.second_font.render(
            "You can press 'Esc' at any time to pause the game", True, "Black")
        self.pause_instructions_rect = self.pause_instructions_surf.get_rect(
            center = (display_obj.SCREEN_WIDTH / 2, 380))
        
        self.controls_instructions_surf = self.second_font.render(
            "Controls: Press the spacebar during the game to Jump", True, "Black")
        self.controls_instructions_rect = self.controls_instructions_surf.get_rect(
            center = (display_obj.SCREEN_WIDTH / 2, 415))

        self.game_title_surf = self.main_font.render("PIXEL SCROLLER", True, "Black")
        self.game_title_rect = self.game_title_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 250))

        self.restart_game_surf = self.second_font.render("Press 'Space' to Play Again", True, "Black")
        self.restart_game_rect = self.start_game_surf.get_rect(
            center = (display_obj.SCREEN_WIDTH / 2 - 25, display_obj.SCREEN_HEIGHT / 2))

        self.quit_game_surf = self.second_font.render("Press 'Q' to Exit", True, "Black")
        self.quit_game_rect = self.quit_game_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 340))

        self.game_over_surf = self.main_font.render("GAME OVER", True, "Black")
        self.game_over_rect = self.game_title_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2 + 80, 250))

        self.pause_menu_surf = self.main_font.render("PAUSE", True, "Black")
        self.pause_menu_rect = self.pause_menu_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 250))

        self.resume_game_surf = self.second_font.render("Press 'Space' to Resume", True, "Black")
        self.resume_game_rect = self.resume_game_surf.get_rect(
            center = (display_obj.SCREEN_WIDTH / 2, display_obj.SCREEN_HEIGHT / 2))
        
        self.high_score_surf = self.second_font.render(f"HIGH SCORE: {self.current_high_score}", True, "Black")
        self.high_score_rect = self.high_score_surf.get_rect(topleft = (25, 25))

    # Check for all events
    def event_catcher(self):
        for event in display.pygame.event.get():
            # General check to close game regardless of the state
            if event.type == display.pygame.QUIT:
                display.pygame.quit()
                exit()
            
            # Check to close game/make small changes depending on current game state
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
                    walking_enemy_obj.walking_enemy_rect.left = display_obj.SCREEN_WIDTH
                    flying_enemy_obj.flying_enemy_rect.left = display_obj.SCREEN_WIDTH + 300
                    self.game_playing = True
                    self.score_reset = display.pygame.time.get_ticks() // 125
                    self.pause_duration = 0
                if event.type == display.pygame.KEYDOWN and event.key == display.pygame.K_q:
                    display.pygame.quit()
                    exit()

    # Update Functions
    def update_score(self):
        current_score = (display.pygame.time.get_ticks() // 125) - self.score_reset - self.pause_duration
        score_surf = self.main_font.render(f"SCORE: {current_score}", True, "Black")
        score_rect = score_surf.get_rect(center = (display_obj.SCREEN_WIDTH / 2, 50))
        display.screen.blit(score_surf, score_rect)
        score.store_high_score(current_score)
        return current_score
    
    def update_high_score(self):
        new_high_score = score.get_high_score()
        self.high_score_surf = self.second_font.render(f"HIGH SCORE: {new_high_score}", True, "Black")

    def increase_enemy_speed(self, score):
        interval_one = 75
        interval_two = 150
        interval_three = 250
        interval_four = 375
        interval_five = 500

        if score > interval_one:
            walking_enemy_obj.walking_enemy_speed = 4
            flying_enemy_obj.flying_enemy_speed = 4
        elif score > interval_two:
            walking_enemy_obj.walking_enemy_speed = 5
            flying_enemy_obj.flying_enemy_speed = 5
        elif score > interval_three:
            walking_enemy_obj.walking_enemy_speed = 6
            flying_enemy_obj.flying_enemy_speed = 6
        elif score > interval_four:
            walking_enemy_obj.walking_enemy_speed = 7
            flying_enemy_obj.flying_enemy_speed = 7
        elif score > interval_five:
            walking_enemy_obj.walking_enemy_speed = 8
            flying_enemy_obj.flying_enemy_speed = 8

    # Draw Functions
    def draw_background(self):
        display.screen.blit(display_obj.background_surf, display_obj.background_rect)
        display.screen.blit(display_obj.ground_surf, display_obj.ground_rect)

    def draw_start_menu(self):
        display.screen.blit(self.game_title_surf, self.game_title_rect)
        display.screen.blit(self.start_game_surf, self.start_game_rect)
        display.screen.blit(self.quit_game_surf, self.quit_game_rect)
        display.screen.blit(self.pause_instructions_surf, self.pause_instructions_rect)
        display.screen.blit(self.controls_instructions_surf, self.controls_instructions_rect)
        display.screen.blit(self.high_score_surf, self.high_score_rect)

    def draw_pause_menu(self):
        display.screen.blit(self.pause_menu_surf, self.pause_menu_rect)
        display.screen.blit(self.resume_game_surf, self.resume_game_rect)
        display.screen.blit(self.quit_game_surf, self.quit_game_rect)

    def draw_game_over_menu(self):
        display.screen.blit(self.game_over_surf, self.game_over_rect)
        display.screen.blit(self.restart_game_surf, self.restart_game_rect)
        display.screen.blit(self.quit_game_surf, self.quit_game_rect)
        display.screen.blit(self.high_score_surf, self.high_score_rect)

    def draw_characters(self):
        display.screen.blit(player_obj.player_surf, player_obj.player_rect)
        display.screen.blit(walking_enemy_obj.walking_enemy_surf, walking_enemy_obj.walking_enemy_rect)
        display.screen.blit(flying_enemy_obj.flying_enemy_surf, flying_enemy_obj.flying_enemy_rect)

    def run_game(self):
        self.event_catcher()

        # Each if/elif statement represents what happens in each state of the game
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
            if flying_enemy_obj.flying_enemy_rect.right < - 50:
                flying_enemy_obj.flying_enemy_rect.left = display_obj.SCREEN_WIDTH + randint(100, 150)
        
            self.draw_characters()
            self.update_score()
            self.increase_enemy_speed(self.update_score())

            '''
            Used for constant calculation of mask offset
            Determines distance between player and enemy top left rect points
            Collision happens when offset.x is less than the combined width of the two images
            or when offset.y is less than the combined height of the two images
            '''
            plyr_walkenemy_offset = (walking_enemy_obj.walking_enemy_rect.x - player_obj.player_rect.x, 
                walking_enemy_obj.walking_enemy_rect.y - player_obj.player_rect.y)
            plyr_flyenemy_offset = (flying_enemy_obj.flying_enemy_rect.x - player_obj.player_rect.x, 
                flying_enemy_obj.flying_enemy_rect.y - player_obj.player_rect.y)
            
            if player_obj.player_mask.overlap(walking_enemy_obj.walking_enemy_mask, plyr_walkenemy_offset):
                self.update_high_score()
                self.game_playing = False
                self.in_game_over_menu = True
            if player_obj.player_mask.overlap(flying_enemy_obj.flying_enemy_mask, plyr_flyenemy_offset):
                self.update_high_score()
                self.game_playing = False
                self.in_game_over_menu = True
        elif self.in_pause_menu:
            self.draw_background()
            self.draw_pause_menu()
        elif self.in_game_over_menu:
            self.draw_background()
            self.draw_game_over_menu()

        display.pygame.display.update()
        display_obj.clock.tick(60)

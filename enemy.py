import display

display_obj = display.Display()

class WalkingEnemy:
    def __init__(self):
        self.walking_enemy_surf = display.pygame.transform.scale_by(
            display.pygame.image.load("images/Tiles/Characters/main_enemy.png").convert_alpha(), 3)
        self.walking_enemy_rect = self.walking_enemy_surf.get_rect(
            bottomright = (display_obj.SCREEN_WIDTH, display_obj.background_surf.get_height()))
        self.walking_enemy_speed = 5

class FlyingEnemy:
    def __init__(self):
        self.flying_enemy_surf = display.pygame.transform.scale_by(
            display.pygame.image.load("images/Tiles/Characters/second_enemy.png").convert_alpha(), 3)
        self.flying_enemy_rect = self.flying_enemy_surf.get_rect(bottomright = (display_obj.SCREEN_WIDTH + 200, 250))
        self.flying_enemy_speed = 4
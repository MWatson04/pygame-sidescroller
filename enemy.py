import display

# Set initial enemy data
class WalkingEnemy:
    def __init__(self):
        self.walking_enemy_surf = display.pygame.transform.scale_by(
            display.pygame.image.load("images/Tiles/Characters/main_enemy.png").convert_alpha(), 3)
        self.walking_enemy_rect = self.walking_enemy_surf.get_rect(
            bottomright = (display.SCREEN_WIDTH, display.background_surf.get_height()))
        self.walking_enemy_mask = display.pygame.mask.from_surface(self.walking_enemy_surf)
        self.walking_enemy_speed = 3

class FlyingEnemy:
    def __init__(self):
        self.flying_enemy_surf = display.pygame.transform.scale_by(
            display.pygame.image.load("images/Tiles/Characters/second_enemy.png").convert_alpha(), 3)
        self.flying_enemy_rect = self.flying_enemy_surf.get_rect(bottomright = (display.SCREEN_WIDTH + 200, 290))
        self.flying_enemy_mask = display.pygame.mask.from_surface(self.flying_enemy_surf)
        self.flying_enemy_speed = 3
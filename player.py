import display

display_obj = display.Display()

# Set initial player data
class Player:
    def __init__(self):
        self.player_surf = display.pygame.image.load("images/Tiles/Characters/main_character.png").convert_alpha()
        self.player_surf = display.pygame.transform.scale_by(self.player_surf, 3)
        self.player_surf = display.pygame.transform.flip(self.player_surf, 180, 0)
        self.player_rect = self.player_surf.get_rect(midbottom = (75, display_obj.background_surf.get_height()))
        self.player_mask = display.pygame.mask.from_surface(self.player_surf)
        self.player_gravity = 0


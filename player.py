import pygame
import display

display_obj = display.Display()

class Player:
    def __init__(self):
        self.player_surf = pygame.image.load("images/Tiles/Characters/main_character.png").convert_alpha()
        self.player_surf = pygame.transform.scale_by(self.player_surf, 3)
        self.player_surf = pygame.transform.flip(self.player_surf, 180, 0)
        self.player_rect = self.player_surf.get_rect(midbottom = (75, display_obj.background_surf.get_height()))
        self.player_gravity = 0


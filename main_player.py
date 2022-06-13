import pygame
from pygame.locals import *


class MainPlayer:

    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.width = 20
        self.height = 90
        self.color = pygame.Color(51, 204, 51)
        self.shape = None

    def configure_player(self, surface_height):
        self.position_y = surface_height / 2
        self.shape = pygame.Rect(self.position_x, self.position_y, self.width, self.height)

    def update_position(self, surface_height):
        key = pygame.key.get_pressed()
        if key[K_UP]:
            if self.position_y >= 0:
                self.position_y -= 5
                self.shape.move_ip(0, -5)

        elif key[K_DOWN]:
            if self.position_y + self.height <= surface_height:
                self.position_y += 5
                self.shape.move_ip(0, 5)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.shape)

    def get_current_position(self):
        player_borders_x = [0, self.width]
        player_borders_y = [self.position_y, self.position_y + self.height]

        return player_borders_x, player_borders_y

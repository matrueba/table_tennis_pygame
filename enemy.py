import pygame


class Enemy:

    def __init__(self):
        self.position_x = 0
        self.position_y = 0
        self.width = 20
        self.height = 90
        self.color = pygame.Color(255, 0, 0)
        self.shape = None

    def configure_enemy(self,  surface_width, surface_height):
        self.position_y = surface_height / 2
        self.position_x = surface_width - self.width
        self.shape = pygame.Rect(self.position_x, self.position_y, self.width, self.height)

    def update_position(self,  surface_width, surface_height, ball_position):

        quarter_screen = surface_width * 3 / 4

        if self.position_y <= 0:
            self.position_y += 2
            self.shape.move_ip(0, 2)
        if self.position_y + self.height >= surface_height:
            self.position_y -= 2
            self.shape.move_ip(0, -2)

        if ball_position[0] > quarter_screen:
            if ball_position[1] < self.position_y + self.height/2:
                self.position_y -= 5
                self.shape.move_ip(0, -5)
            elif ball_position[1] > self.position_y + self.height/2:
                self.position_y += 5
                self.shape.move_ip(0, +5)

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.shape)

    def get_current_position(self, surface_width):
        enemy_borders_x = [surface_width - self.width, surface_width]
        enemy_borders_y = [self.position_y, self.position_y + self.height]

        return enemy_borders_x, enemy_borders_y

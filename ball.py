import pygame
import random


class Ball:

    def __init__(self):
        self.center = (0, 0)
        self.radius = 10
        self.color = pygame.Color(153, 51, 255)
        self.shape = None
        self.first_move = False
        self.direction_y = 1
        self.direction_x = 1
        self.last_pos = []
        self.speed = 1
        self.player_collisions = 0
        self.touching_player = False

    def configure_ball(self, surface, surface_width, surface_height):
        half_width = surface_width / 2
        half_height = surface_height / 2
        self.last_pos = [half_width, half_height]
        self.center = (half_width, half_height)
        self.first_move = True
        self.shape = pygame.draw.circle(surface, self.color, self.center, self.radius)
        self.direction_y = 1
        self.direction_x = 1
        self.speed = 2

    def detect_collision(self, surface_height, main_player_pos, enemy_pos):
        self.touching_player = False

        if self.last_pos[1] - self.radius <= 0:
            self.direction_y = 1

        if self.last_pos[1] + self.radius >= surface_height:
            self.direction_y = -1

        if self.last_pos[0] - self.radius <= main_player_pos[0][1]:
            border_up = main_player_pos[1][0]
            border_down = main_player_pos[1][1]
            if (border_up <= self.last_pos[1] - self.radius) and \
                    (border_down >= self.last_pos[1] + self.radius):
                self.player_collisions += 1
                self.direction_x = 1
                self.touching_player = True

        if self.last_pos[0] + self.radius >= enemy_pos[0][0]:
            border_up = enemy_pos[1][0]
            border_down = enemy_pos[1][1]
            if (border_up <= self.last_pos[1] - self.radius) and \
                    (border_down >= self.last_pos[1] + self.radius):
                self.player_collisions += 1
                self.direction_x = -1
                self.touching_player = True

    def update_position(self):
        if self.first_move:
            self.direction_y = random.choice([-1, 1])
            self.direction_x = random.choice([-1, 1])
            self.first_move = False
        if self.direction_x == 1 and self.direction_y == 1:
            self.shape.move_ip(self.speed, self.speed)
            self.last_pos[0] += self.speed
            self.last_pos[1] += self.speed
        elif self.direction_x == -1 and self.direction_y == 1:
            self.shape.move_ip(-self.speed, self.speed)
            self.last_pos[0] -= self.speed
            self.last_pos[1] += self.speed
        elif self.direction_x == -1 and self.direction_y == -1:
            self.shape.move_ip(-self.speed, -self.speed)
            self.last_pos[0] -= self.speed
            self.last_pos[1] -= self.speed
        elif self.direction_x == 1 and self.direction_y == -1:
            self.shape.move_ip(self.speed, -self.speed)
            self.last_pos[0] += self.speed
            self.last_pos[1] -= self.speed

    def check_win_point(self, surface_width):
        if self.last_pos[0] < 0:
            return True, "enemy"
        elif self.last_pos[0] > surface_width:
            return True, "player"
        else:
            return False, ""

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.shape, border_radius=20)

    def get_current_position(self):
        return self.last_pos


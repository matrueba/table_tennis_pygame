import pygame
from pygame.locals import *
from main_player import MainPlayer
from ball import Ball
from enemy import Enemy


class App:

    def __init__(self):
        self.surface_width = 640
        self.surface_height = 400
        self.surface = None
        self.running = True
        self.main_player = None
        self.enemy = None
        self.ball = None
        self.match_counter = 0
        self.score = [0, 0]

    def initialize_app(self):
        pygame.init()
        self.running = True

    def configure_display(self):
        self.surface = pygame.display.set_mode((self.surface_width, self.surface_height))
        self.surface.fill(pygame.Color(0, 0, 0))
        pygame.display.set_caption("My first Game")
        pygame.display.init()

    def start_match(self):
        self.initialize_environment()
        print("Start new match")
        while self.running:
            self.surface.fill(pygame.Color(0, 0, 0))
            self.main_player.render(self.surface)
            for event in pygame.event.get():
                self.on_event(event)
            self.update_positions()
            self.update_render()
            if self.ball.player_collisions % 10 == 0 and self.ball.touching_player:
                print("Increase speed")
                self.ball.speed += 1
            win_point, winner = self.ball.check_win_point(self.surface_width)
            if win_point:
                if winner is "enemy":
                    self.score[1] += 1
                elif winner is "player":
                    self.score[0] += 1
                else:
                    print("error")
                pygame.time.delay(2000)
                print("Score: ")
                print("Main Player: ", self.score[0])
                print("Enemy: ", self.score[1])
                return
            pygame.display.update()
            pygame.time.delay(10)

    def initialize_environment(self):
        self.main_player = MainPlayer()
        self.main_player.configure_player(self.surface_height)
        self.enemy = Enemy()
        self.enemy.configure_enemy(self.surface_width, self.surface_height)
        self.ball = Ball()
        self.ball.configure_ball(self.surface, self.surface_width, self.surface_height)
        self.ball.player_collisions = 0

    def on_event(self, event):
        if event.type == QUIT:
            self.running = False

    def net_render(self):
        pygame.draw.line(self.surface, pygame.Color(255, 255, 255), (self.surface_width / 2, 0), (self.surface_width / 2, self.surface_height))

    def update_render(self):
        self.net_render()
        self.main_player.render(self.surface)
        self.enemy.render(self.surface)
        self.ball.render(self.surface)


    def update_positions(self):
        player_borders_x, player_borders_y = self.main_player.get_current_position()
        enemy_borders_x, enemy_borders_y = self.enemy.get_current_position(self.surface_width)
        ball_position = self.ball.get_current_position()

        self.main_player.update_position(self.surface_height)
        self.enemy.update_position(self.surface_width, self.surface_height, ball_position)
        self.ball.update_position()
        self.ball.detect_collision(self.surface_height, (player_borders_x, player_borders_y), (enemy_borders_x, enemy_borders_y))

    def end_app(self):
        pygame.quit()

    def run(self):
        while self.match_counter < 10:
            self.start_match()
        self.end_app()





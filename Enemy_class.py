import pygame
import random
from pygame import Vector2
directions = ["left","right", "up", "down"]

class ENEMY:
    def __init__(self):
        self.pos = Vector2(0,0)
        self.speed = None
        self.direction = None
        self.size = 10
        self.enemy_rect = pygame.Rect(self.pos.x - self.size / 2, self.pos.y - self.size / 2, self.size, self.size)

    def draw_enemy(self, win):
        self.enemy_rect = pygame.Rect(self.pos.x - self.size / 2, self.pos.y - self.size / 2, self.size, self.size)
        pygame.draw.rect(win, (200, 0,122), self.enemy_rect)


    def generate_pos(self, width, height):
        directions = ["left", "right", "up", "down"]
        self.direction = random.choice(directions)
        
        if self.direction == "left":
            self.pos = Vector2(-self.size, random.randint(0, height))
            self.speed = Vector2(5, 0)
        elif self.direction == "right":
            self.pos = Vector2(width + self.size, random.randint(0, height))
            self.speed = Vector2(-5, 0)
        elif self.direction == "down":
            self.pos = Vector2(random.randint(0, width), -self.size)
            self.speed = Vector2(0, 5)
        elif self.direction == "up":
            self.pos = Vector2(random.randint(0, width), height + self.size)
            self.speed = Vector2(0, -5)

    def move(self):
        self.pos += self.speed



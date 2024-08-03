import pygame
import sys
import random
from pygame import Vector2

# Constants
WIDTH, HEIGHT = 400, 400
ENEMY_SPAWN_INTERVAL = 2000  
ENEMY_SPEED = 5


pygame.init()
win = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

class ENEMY:
    def __init__(self):
        self.pos = None
        self.speed = None
        self.enemy_rect = None
        self.direction = None
        self.size = 10

    def generate_pos(self, width, height):
        directions = ["left", "right", "up", "down"]
        self.direction = random.choice(directions)
        
        if self.direction == "left":
            self.pos = Vector2(-self.size, random.randint(0, height))
            self.speed = Vector2(ENEMY_SPEED, 0)
        elif self.direction == "right":
            self.pos = Vector2(width + self.size, random.randint(0, height))
            self.speed = Vector2(-ENEMY_SPEED, 0)
        elif self.direction == "down":
            self.pos = Vector2(random.randint(0, width), -self.size)
            self.speed = Vector2(0, ENEMY_SPEED)
        elif self.direction == "up":
            self.pos = Vector2(random.randint(0, width), height + self.size)
            self.speed = Vector2(0, -ENEMY_SPEED)

    def move(self):
        self.pos += self.speed

    def draw_enemy(self, win):
        self.enemy_rect = pygame.Rect(self.pos.x - self.size / 2, self.pos.y - self.size / 2, self.size, self.size)
        pygame.draw.rect(win, (200, 0,122), self.enemy_rect, 2)


def main():
    enemies = []
    last_enemy_spawn_time = pygame.time.get_ticks() 

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        current_time = pygame.time.get_ticks()
        if current_time - last_enemy_spawn_time >= ENEMY_SPAWN_INTERVAL:
            for _ in range(random.choice([1, 3, 5])):
                enemy = ENEMY()
                enemy.generate_pos(WIDTH, HEIGHT)
                enemies.append(enemy)
            last_enemy_spawn_time = last_enemy_spawn_time - 10  

        
        for enemy in enemies[:]:
            enemy.move()
            if (enemy.pos.x < -enemy.size or enemy.pos.x > WIDTH + enemy.size or
                enemy.pos.y < -enemy.size or enemy.pos.y > HEIGHT + enemy.size):
                enemies.remove(enemy)

        win.fill((0, 0, 0))
        for enemy in enemies:
            enemy.draw_enemy(win)
        pygame.display.update()
        clock.tick(60) 

main()

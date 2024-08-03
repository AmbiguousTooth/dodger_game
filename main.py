import pygame
import sys
import random
import time
from pygame import Vector2

#importing classes and such
from Player_class import PLAYER 


pygame.init()

ENEMY_SPAWN = pygame.USEREVENT
WIDTH, HEIGHT = 400, 450


win = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = PLAYER(WIDTH/2,HEIGHT/2)

enemy_spawn_time = 2000 
spawn_timer = 0 

def draw_on_screen():
	win.fill((0,0,0))		
	player.draw_player(win)		
	pygame.display.update()

def main():
	while True:
		spawn_timer = clock.tick(60)

		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		if spawn_timer >= enemy_spawn_time:
			for i in range(random.choice(1,3,5)):
				

			enemy_spawn_time = max(enemy_spawn_time-50, 500)

		player.movement(WIDTH,HEIGHT)
		draw_on_screen()
main()
import pygame
import sys
import random
import time
from pygame import Vector2

#importing classes and such
from Player_class import PLAYER 
from Enemy_class import ENEMY

pygame.init()

ENEMY_SPAWN = pygame.USEREVENT
WIDTH, HEIGHT = 400, 400

enemies = []
win = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = PLAYER(WIDTH/2,HEIGHT/2)

enemy_spawn_time = 2000 
spawn_timer = 0 

def draw_on_screen():
	win.fill((0,0,0))		
	for i in enemies:
		i.draw_enemy(win)	
	player.draw_player(win)		
	pygame.display.update()
	
def spawing_and_collision_with_player():
	for enemy in enemies[:]:
		enemy.move()	
		if (enemy.pos.x < -enemy.size or enemy.pos.x > WIDTH + enemy.size or
				enemy.pos.y < -enemy.size or enemy.pos.y > HEIGHT + enemy.size):
				enemies.remove(enemy)
		if enemy.enemy_rect.colliderect(player.player_rect):
			pygame.quit()
			sys.exit()

while True:
	spawn_timer += clock.tick(60)

	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	if spawn_timer > enemy_spawn_time:
		for i in range(random.choice([1,3,5])):	
			i = ENEMY()
			i.generate_pos(WIDTH,HEIGHT)
			enemies.append(i)
		enemy_spawn_time = max(enemy_spawn_time-100, 500)
		spawn_timer = 0

	spawing_and_collision_with_player()	
	player.movement(WIDTH,HEIGHT)
	draw_on_screen()

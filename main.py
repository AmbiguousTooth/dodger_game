import pygame
import sys
import random
import time
from pygame import Vector2

#importing classes and functions
from Player_class import PLAYER 
from Enemy_class import ENEMY
from reading_and_writing_score import read_highscore,write_highscore

pygame.init()

ENEMY_SPAWN = pygame.USEREVENT
WIDTH, HEIGHT = 400, 400

enemies = []
win = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = PLAYER(WIDTH/2,HEIGHT/2)

stime = time.time()
enemy_spawn_time = 2000 
spawn_timer = 0 

score = 0
highscore = read_highscore()


def draw_on_screen():
	font = pygame.font.Font('freesansbold.ttf', 18)
	score_text = font.render('Score: ' + str(score),1, (255,255,255))
	high_text = font.render('Highscore: ' + str(highscore), 1, (255,255,255))
	

	win.fill((0,0,0))		
	
	win.blit(score_text, (5,5))
	win.blit(high_text,(5, 22))
	
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

def increment_score():
	global stime,score
	
	if time.time() - stime > 1:
		score += 1
		stime = time.time()


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
	
	increment_score()
	if score > highscore:
		highscore = score
		write_highscore(highscore)
	
	spawing_and_collision_with_player()	
	player.movement(WIDTH,HEIGHT)
	draw_on_screen()

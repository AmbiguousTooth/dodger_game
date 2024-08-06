import pygame
import sys

def draw(win):
	name_font = pygame.font.Font('freesansbold.ttf', 50)
	game_name = name_font.render('Dodger', True, (85, 85, 222))
	
	font = pygame.font.Font('freesansbold.ttf', 25)
	text1 = font.render('Press \'SPACE\' to start', True, (255, 255, 255))
	text2 = font.render('Move with arrow keys', True, (255, 255, 255))
	
	window_width, window_height = win.get_size()
	
	game_name_rect = game_name.get_rect(center=(window_width // 2, window_height // 2 - 30))
	text1_rect = text1.get_rect(center=(window_width // 2, window_height // 2 + 20))
	text2_rect = text2.get_rect(center=(window_width // 2, window_height // 2 + 60))
	
	win.fill((0, 0, 0))
	win.blit(game_name, game_name_rect)
	win.blit(text1, text1_rect)
	win.blit(text2, text2_rect)
	
	pygame.display.update()

def main_menu(width, height):
	pygame.init()
	win = pygame.display.set_mode((width, height))

	while True:
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			break

		draw(win)

if __name__ == "__main__":
	main_menu(800, 600)

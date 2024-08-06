import pygame

def lose(win):

	while True:
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			break


		font = pygame.font.Font('freesansbold.ttf', 25)
		text1 = font.render('Press \'SPACE\' to continue', True, (255, 255, 255))

		win.fill((0,0,0))
		window_width, window_height = win.get_size()
		text1_rect = text1.get_rect(center=(window_width // 2, window_height // 2 ))
		win.blit(text1, text1_rect)
		pygame.display.update()
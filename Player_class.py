import pygame



class PLAYER:
    def __init__(self, width, height):
        self.pos = pygame.Vector2(width, height)
        self.speed = 5 
        self.size = 20  

    def draw_player(self, win):
        player_rect = pygame.Rect(self.pos.x - self.size / 2, self.pos.y - self.size / 2, self.size, self.size)
        pygame.draw.rect(win, (255, 255, 255), player_rect, 2)

    def movement(self,WIDTH,HEIGHT):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_DOWN]:
            direction.y += 1
        
        if direction.length() > 0:
            direction.normalize_ip()
       
        new_pos = self.pos + direction * self.speed


        if new_pos.x < self.size / 2:
            new_pos.x = self.size / 2
        elif new_pos.x > WIDTH - self.size / 2:
            new_pos.x = WIDTH - self.size / 2
        
        if new_pos.y < self.size / 2:
            new_pos.y = self.size / 2
        elif new_pos.y > HEIGHT - self.size / 2:
            new_pos.y = HEIGHT - self.size / 2
\
        self.pos = new_pos

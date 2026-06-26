import pygame
import random

from config import WIDTH, HEIGHT, POWER_SPEED, Colors

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.dx = random.uniform(-5, 5)
        self.dy = random.uniform(-5, 5)

        self.life = 30

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 200, 0),
            (int(self.x), int(self.y)),
            3
        )
    
class Explosion: 

    def __init__(self, x, y): 
        self.rect = pygame.Rect(x, y, 50, 50)
        self.timer = 0
        self.duracion = 90

    def update(self): 
        self.timer += 1

        if self.timer >= self.duracion: 
            return True
        
        return False
    
    def draw(self, screen): 
        radio = self. timer

        alpha = max(0, 255 - (self.timer * 3))

        surface = pygame.Surface((radio * 2, radio * 2), pygame.SRCALPHA)

        pygame.draw.circle(screen, (255, 100, 0), self.rect.center, radio)
        pygame.draw.circle(screen, (255, 220, 0), self.rect.center, int(radio * 0.7))
        pygame.draw.circle(screen, (255, 255, 255), self.rect.center, int(radio * 0.3))

        screen.blit(
            surface,
            (self.rect.centerx - radio, self.rect.centery - radio)
        )
        



    

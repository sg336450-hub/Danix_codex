import pygame
import random

from config import WIDTH, HEIGHT, POWER_SPEED, Colors

class PowerUp:

    def __init__(self, speed=POWER_SPEED):

        x = random.randint(5, WIDTH - 50)

        self.rect = pygame.Rect(x, -50, 50, 50)
        self.speed = speed

    def update(self):

        self.rect.y += self.speed

        # reaparecer arriba
        if self.rect.top > HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(5, WIDTH - 50)
            self.speed += 0.3
            self.speed = min(self.speed, 10)

            return True
    
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.GOLDEN, self.rect)
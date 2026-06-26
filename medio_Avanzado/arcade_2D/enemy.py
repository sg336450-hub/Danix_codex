# enemy.py

import pygame
import random

from config import WIDTH, HEIGHT, ENEMY_SPEED, Colors


class Enemy:

    def __init__(self, speed=ENEMY_SPEED):

        x = random.randint(5, WIDTH - 50)

        def __init__(self):

         self.image = pygame.image.load(
            "assets/enemy.png"
         ).convert_alpha()

         self.image = pygame.transform.scale(
            self.image,
            (50, 50)
         )

        self.rect = self.image.get_rect()

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
     screen.blit(self.image, self.rect)
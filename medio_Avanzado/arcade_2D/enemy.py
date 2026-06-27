import pygame
import random
from config import WIDTH, HEIGHT, ENEMY_SPEED
import os

BASE_DIR = os.path.dirname(__file__)

enemy_path = os.path.join(BASE_DIR, "assets", "enemy.png")


class Enemy:

    def __init__(self, speed=ENEMY_SPEED):

        self.speed = speed

        self.image = pygame.image.load(
            enemy_path
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (50, 50)
        )

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(5, WIDTH - 50)
        self.rect.y = -50

    def update(self):

        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(5, WIDTH - 50)
            self.speed += 0.3
            self.speed = min(self.speed, 10)
            return True

        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
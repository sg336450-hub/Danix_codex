# player.py

import pygame
from config import WIDTH, HEIGHT, PLAYER_SPEED, Colors
import os

BASE_DIR = os.path.dirname(__file__)

player_path = os.path.join(BASE_DIR, "assets", "player.png")

class Player:

    def __init__(self):

        self.image = pygame.image.load(
            player_path
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (64, 64)
        )

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

        self.max_health = 100
        self.health = 100

    def move(self, keys):

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        if keys[pygame.K_UP]: 
            self.rect.y -= PLAYER_SPEED

        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # límites pantalla
        if self.rect.left < 5:
            self.rect.left = 5

        if self.rect.right > WIDTH - 5:
            self.rect.right = WIDTH - 5

        if self.rect.top < 5: 
            self.rect.top = 5

        if self.rect.bottom > HEIGHT - 5: 
            self.rect.bottom = HEIGHT - 5 

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def draw_healthbar(self, screen):
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, Colors.RED, (110, 87, 200, 20))
        pygame.draw.rect(screen, Colors.GREEN, (110, 87, 200 * ratio, 20))

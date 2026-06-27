# game.py

import pygame
import os

BASE_DIR = os.path.dirname(__file__)

background_path = os.path.join(BASE_DIR, "assets", "enemy.png")

from config import WIDTH, HEIGHT, FPS, Colors
from player import Player
from enemy import Enemy
from power import PowerUp
from explosiones import Explosion, Particle


class Game:

    def __init__(self, enemies_count=3, powerups_count=2):

        pygame.init()
        

        self.lifes = 3

        self.score = 0

        self.HP_TEXT = "HP: "
        self.font = pygame.font.SysFont("arial", 30)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ESQUIVA LOS ENEMIGOS")

        self.background = pygame.image.load(background_path).convert()

        self.background = pygame.image.load(background_path).convert()

        self.clock = pygame.time.Clock()

        self.running = True

        self.player = Player()

        self.enemies = [
            Enemy() for _ in range(enemies_count)
        ]

        self.powerups = [
            PowerUp() for _ in range(powerups_count)
        ]

        self.explosions = []

        self.particles = []

    # =========================
    # EVENTOS
    # =========================
    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False


    # =========================
    # UPDATE
    # =========================
    def update(self):

        keys = pygame.key.get_pressed()

        self.player.move(keys)

        self.create_enemies = False

        for enemy in self.enemies:
          if enemy.update(): 
                self.create_enemies = True
        if self.create_enemies and len(self.enemies) <= 8:
            self.enemies.append(Enemy())
            self.create_enemies = False
        
        for powerup in self.powerups:
            powerup.update()
            if len(self.powerups) < 2:
                self.powerups.append(PowerUp())
        
        for explosion in self.explosions: 
            if explosion.update(): 
                self.explosions.remove(explosion)

        for particle in self.particles:
            particle.update()
            if particle.life <= 0:
                self.particles.remove(particle)

# =========================
    # COLISIONES
# =========================

    def collision(self):
       for enemy in self.enemies:
            
            # colisión
            if self.player.rect.colliderect(enemy.rect):
                
                self.enemies.remove(enemy)

            
                self.player.health -= 20
                if  self.player.health <= 0: 
                    self.lifes -= 1
                    self.player.health = self.player.max_health
                if self.lifes <= 0:  
                    print("GAME OVER")
                    self.running = False
                
                self.explosions.append(Explosion(enemy.rect.centerx, enemy.rect.centery))
                # Create particles for the explosion
                for _ in range(20):
                    self.particles.append(Particle(enemy.rect.centerx, enemy.rect.centery))

       for powerup in self.powerups:
            if self.player.rect.colliderect(powerup.rect):
                self.powerups.remove(powerup)
                self.score += 5
                self.player.health += 20
                self.player.health = min(self.player.health, self.player.max_health)

    # =========================
    # DRAW
    # =========================
    def draw(self):

        self.screen.fill((20, 20, 30))

        self.player.draw(self.screen)

        self.player.draw_healthbar(self.screen)

        self.lifes_text = self.font.render(
              f"Vidas: {self.lifes}",
                 True,
               Colors.WHITE
         )
        self.screen.blit(self.lifes_text, (10, 40))

        self.HP_text = self.font.render(
              f"HP: {self.player.health}",
                 True,
               Colors.WHITE
         )
        self.screen.blit(self.HP_text, (10, 80))

        score_text = self.font.render(
              f"Puntos: {self.score}",
                 True,
               Colors.WHITE
         )
        self.screen.blit(score_text, (10, 10)) 
        
         

        for enemy in self.enemies:
            enemy.draw(self.screen)


        for powerup in self.powerups:
            powerup.draw(self.screen)

        for explosion in self.explosions: 
            explosion.draw(self.screen)
        
        for particle in self.particles:
            particle.draw(self.screen)


        pygame.display.flip()

    # =========================
    # LOOP PRINCIPAL
    # =========================
    def run(self):

        while self.running:

            self.clock.tick(FPS)

            self.handle_events()

            self.update()
            
            self.collision()

            self.draw()

        pygame.quit()
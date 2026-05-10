import pygame
import sys
import random

pygame.init()

# ==================
# CONFIG
# ==================
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva los bloques 😎")

clock = pygame.time.Clock()

# ==================
# COLORES
# ==================
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BG = (10, 10, 20)

# ==================
# FUENTE
# ==================
font = pygame.font.SysFont(None, 36)


# ==================
# CLASE PLAYER
# ==================
class Player:
    def __init__(self):
        self.size = 40
        self.x = WIDTH // 2
        self.y = 500
        self.speed = 5

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.size,
            self.size
        )

    def move(self, keys):

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # límites
        self.x = max(0, min(WIDTH - self.size, self.x))

        # actualizar rect
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)


# ==================
# CLASE ENEMY
# ==================
class Enemy:
    def __init__(self, speed):

        self.size = 40

        self.x = random.randint(0, WIDTH - self.size)
        self.y = random.randint(-300, 0)

        self.speed = speed

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.size,
            self.size
        )

    def update(self):

        self.y += self.speed

        # si sale de pantalla
        if self.y > HEIGHT:
            self.reset()
            return True

        self.rect.topleft = (self.x, self.y)

        return False

    def reset(self):

        self.y = random.randint(-300, 0)
        self.x = random.randint(0, WIDTH - self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)


# ==================
# CLASE GAME
# ==================
class Game:
    def __init__(self):

        self.Player = Player()

        self.enemies = [
            Enemy(3) for _ in range(3)
        ]

        self.lives = 3
        self.score = 0

        self.running = True

        # invulnerabilidad
        self.last_hit_time = 0
        self.hit_delay = 1000

    # ==================
    # EVENTOS
    # ==================
    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

    # ==================
    # UPDATE
    # ==================
    def update(self):

        keys = pygame.key.get_pressed()

        self.Player.move(keys)

        current_time = pygame.time.get_ticks()

        # recorrer enemigos
        for enemy_obj in self.enemies:

            # movimiento enemigo
            if enemy_obj.update():
                self.score += 1

            # colisión
            if self.Player.rect.colliderect(enemy_obj.rect):

                if current_time - self.last_hit_time > self.hit_delay:

                    self.lives -= 1

                    self.last_hit_time = current_time

                    enemy_obj.reset()

        # ==================
        # DIFICULTAD PROGRESIVA
        # ==================
        if self.score > 0 and self.score % 10 == 0:

            # evitar agregar infinitos enemigos
            if (
                len(self.enemies) < 10
                and self.score // 10 > len(self.enemies) - 3
            ):
                self.enemies.append(
                    Enemy(random.randint(3, 6))
                )

    # ==================
    # DIBUJAR
    # ==================
    def draw(self):

        screen.fill(BG)

        self.Player.draw(screen)

        for enemy_obj in self.enemies:
            enemy_obj.draw(screen)

        # HUD
        lives_text = font.render(
            f"Vidas: {self.lives}",
            True,
            WHITE
        )

        screen.blit(lives_text, (10, 10))

        score_text = font.render(
            f"Score: {self.score}",
            True,
            YELLOW
        )

        screen.blit(score_text, (10, 50))

        pygame.display.flip()

    # ==================
    # GAME OVER
    # ==================
    def game_over_screen(self):

        screen.fill(BG)

        text = font.render(
            "GAME OVER",
            True,
            RED
        )

        screen.blit(
            text,
            (WIDTH // 2 - 100, HEIGHT // 2)
        )

        pygame.display.flip()

        pygame.time.delay(2000)

    # ==================
    # LOOP PRINCIPAL
    # ==================
    def run(self):

        while self.running:

            clock.tick(60)

            self.handle_events()

            self.update()

            self.draw()

            # game over
            if self.lives <= 0:

                self.game_over_screen()

                self.running = False


# ==================
# INICIAR JUEGO
# ==================
game_instance = Game()

game_instance.run()

pygame.quit()

sys.exit()

### Ctrl + Shift + L para seleccionar todas las ocurrencias de una palabra y editarlas a la vez.

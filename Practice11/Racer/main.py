import sys
import pygame
from entities import Player, Enemy, Coin

pygame.init()

# Window size
W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racer + Weighted Coins")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)

clock = pygame.time.Clock()
FPS = 60

# Create game objects
player = Player(W, H, image_path="images/car1.png")
enemy = Enemy(W, H, image_path="images/car2.png", speed=8)
coin = Coin(W, H, image_path="images/coin.png", speed=6)

# Total collected points from coins
coins_count = 0

# Enemy speed increases every N points
N = 5
speed_level = 0  # how many times we already increased speed

font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 26)

while True:
    # Handle close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update game objects
    player.update()
    enemy.move()
    coin.move()

    # Coin collision: add coin weight to score
    if player.rect.colliderect(coin.rect):
        coins_count += coin.weight
        coin.respawn()

    # Increase enemy speed after each N points
    # Example: N=5 -> at 5, 10, 15 points...
    current_level = coins_count // N
    if current_level > speed_level:
        enemy.increase_speed(1)
        speed_level = current_level

    # Enemy collision = game over
    if player.rect.colliderect(enemy.rect):
        over_font = pygame.font.Font(None, 64)
        over_text = over_font.render("GAME OVER", True, RED)
        over_rect = over_text.get_rect(center=(W // 2, H // 2))

        screen.fill(WHITE)
        screen.blit(over_text, over_rect)
        pygame.display.update()
        pygame.time.delay(2000)

        pygame.quit()
        sys.exit()

    # Draw frame
    screen.fill(WHITE)
    player.draw(screen)
    enemy.draw(screen)
    coin.draw(screen)

    # Draw score in top-right corner
    score_text = font.render(f"Coins: {coins_count}", True, BLACK)
    score_rect = score_text.get_rect(topright=(W - 10, 10))
    screen.blit(score_text, score_rect)

    # Show enemy speed (useful to see difficulty changes)
    speed_text = small_font.render(f"Enemy speed: {enemy.speed}", True, BLACK)
    screen.blit(speed_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)
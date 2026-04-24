import sys
import pygame
from entities import Player, Enemy, Coin

# Start pygame
pygame.init()

# Window size
W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Racer + Coins")

# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FPS settings (game speed)
clock = pygame.time.Clock()
FPS = 60

# Create game objects
# car1.png = player, car2.png = enemy, coin.png = coin
player = Player(W, H, image_path="images\car1.png")
enemy = Enemy(W, H, image_path="images\car2.png", speed=8)
coin = Coin(W, H, image_path="images\coin.png", speed=6)

# Collected coins counter
coins_count = 0

# Font for score text
font = pygame.font.Font(None, 32)

# Main game loop
while True:
    # Handle events (for closing window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update all game objects each frame
    player.update()
    enemy.move()
    coin.move()

    # Check collision: player and coin
    # If player touches coin, add score and respawn coin
    if player.rect.colliderect(coin.rect):
        coins_count += 1
        coin.respawn()

    # Check collision: player and enemy
    # If player touches enemy, show GAME OVER text and close game
    if player.rect.colliderect(enemy.rect):
        over_font = pygame.font.Font(None, 64)
        over_text = over_font.render("GAME OVER", True, (255, 0, 0))
        over_rect = over_text.get_rect(center=(W // 2, H // 2))

        screen.fill((255, 255, 255))
        screen.blit(over_text, over_rect)
        pygame.display.update()
        pygame.time.delay(2000)

        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(WHITE)
    player.draw(screen)
    enemy.draw(screen)
    coin.draw(screen)

    # Draw score text in top-right corner
    text = font.render(f"Coins: {coins_count}", True, BLACK)
    text_rect = text.get_rect(topright=(W - 10, 10))
    screen.blit(text, text_rect)

    # Show frame on screen
    pygame.display.update()

    # Keep game running at fixed FPS
    clock.tick(FPS)
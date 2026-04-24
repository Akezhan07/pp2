import pygame
import random
import sys

#  Init 
pygame.init()

# Window settings
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

# Grid size (how many cells in row/column)
GRID_W = WIDTH // CELL_SIZE
GRID_H = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

# Game variables 
# Snake starts in center (3 blocks)
snake = [(10, 10), (9, 10), (8, 10)]

# Direction (start moving right)
dx, dy = 1, 0

# Score and level
score = 0
level = 1

# Foods needed for next level
FOODS_PER_LEVEL = 4

# Base speed + speed per level
BASE_FPS = 7
SPEED_STEP = 2


def get_random_food_position(snake_body):
    while True:
        x = random.randint(0, GRID_W - 1)
        y = random.randint(0, GRID_H - 1)

        # If random cell is not occupied by snake -> valid
        if (x, y) not in snake_body:
            return (x, y)


# First food
food = get_random_food_position(snake)

# Main loop 
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Change direction with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0

    # New head position
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # 1) Wall collision (snake leaves playing area)
    if new_head[0] < 0 or new_head[0] >= GRID_W or new_head[1] < 0 or new_head[1] >= GRID_H:
        break

    # 2) Self collision (snake hits itself)
    if new_head in snake:
        break

    # Move snake: add new head
    snake.insert(0, new_head)

    # Check food
    if new_head == food:
        # Snake eats food - score +1, no tail remove (snake grows)
        score += 1

        # New food in valid place
        food = get_random_food_position(snake)

        # Level up every FOODS_PER_LEVEL points
        level = (score // FOODS_PER_LEVEL) + 1
    else:
        # If no food eaten, remove tail (normal move)
        snake.pop()

    # Current game speed by level
    current_fps = BASE_FPS + (level - 1) * SPEED_STEP

    #  Draw
    screen.fill(BLACK)

    # Draw snake
    for i, (x, y) in enumerate(snake):
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        # Head a bit darker
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, rect)

    # Draw food
    food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, food_rect)

    # Draw score and level
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    level_text = small_font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.flip()
    clock.tick(current_fps)

# Game Over screen
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, RED)
final_text = small_font.render(f"Final Score: {score}   Level: {level}", True, WHITE)

game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
final_rect = final_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

screen.blit(game_over_text, game_over_rect)
screen.blit(final_text, final_rect)
pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()
sys.exit()
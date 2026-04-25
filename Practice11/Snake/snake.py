import pygame
import random
import sys

#start pygame
pygame.init()

# window size
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20

# how many cells we have horizontally/vertically
GRID_W = WIDTH // CELL_SIZE
GRID_H = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Weighted Food")

clock = pygame.time.Clock()

# colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
WHITE = (255, 255, 255)

# food color depends on food weight
# x1 red, x2 orange, x3 yellow
FOOD_COLORS = {
    1: (220, 0, 0),
    2: (255, 140, 0),
    3: (255, 215, 0)
}

# text fonts
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

# --- game state ---
# snake starts as 3 blocks
snake = [(10, 10), (9, 10), (8, 10)]

# start moving right
dx, dy = 1, 0

score = 0
level = 1

# every N points -> next level
POINTS_PER_LEVEL = 6

# speed settings
BASE_FPS = 7
SPEED_STEP = 1

# food exists only this many ms, then disappears
FOOD_LIFETIME_MS = 5000  # 5 sec


def get_random_food_position(snake_body):
    # just trying random cells until we find free one
    while True:
        x = random.randint(0, GRID_W - 1)
        y = random.randint(0, GRID_H - 1)
        if (x, y) not in snake_body:
            return (x, y)


def generate_food(snake_body):
    # new food: random place + random weight + time when it spawned
    position = get_random_food_position(snake_body)

    # x1 is most common, x3 is rare
    weight = random.choices([1, 2, 3], weights=[60, 30, 10])[0]

    return {
        "pos": position,
        "weight": weight,
        "spawned_at": pygame.time.get_ticks()
    }


# first food
food = generate_food(snake)

# --- main loop ---
running = True
while running:
    # events (close window + arrows)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # no instant reverse direction, so snake doesn't crash weirdly
            if event.key == pygame.K_UP and dy != 1:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN and dy != -1:
                dx, dy = 0, 1
            elif event.key == pygame.K_LEFT and dx != 1:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT and dx != -1:
                dx, dy = 1, 0

    # if food timer is over -> respawn food somewhere else
    now = pygame.time.get_ticks()
    if now - food["spawned_at"] >= FOOD_LIFETIME_MS:
        food = generate_food(snake)

    # calculate next head position
    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

    # wall hit -> game over
    if new_head[0] < 0 or new_head[0] >= GRID_W or new_head[1] < 0 or new_head[1] >= GRID_H:
        break

    # hit itself -> game over
    if new_head in snake:
        break

    # normal move: add new head
    snake.insert(0, new_head)

    # check if we ate food
    if new_head == food["pos"]:
        # add points based on weight (x1/x2/x3)
        score += food["weight"]

        # new food right after eating
        food = generate_food(snake)

        # update level from score
        level = (score // POINTS_PER_LEVEL) + 1
    else:
        # if no food eaten, tail goes away
        snake.pop()

    # level makes game faster
    current_fps = BASE_FPS + (level - 1) * SPEED_STEP

    # --- draw everything ---
    screen.fill(BLACK)

    # snake draw
    for i, (x, y) in enumerate(snake):
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, rect)

    # food draw (color by weight)
    fx, fy = food["pos"]
    food_rect = pygame.Rect(fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, FOOD_COLORS[food["weight"]], food_rect)

    # time left for current food
    time_left_ms = FOOD_LIFETIME_MS - (pygame.time.get_ticks() - food["spawned_at"])
    if time_left_ms < 0:
        time_left_ms = 0
    time_left_sec = time_left_ms // 1000 + 1  # looks nicer as countdown

    # UI text
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    level_text = small_font.render(f"Level: {level}", True, WHITE)
    food_text = small_font.render(f"Food x{food['weight']}", True, WHITE)
    timer_text = small_font.render(f"Food timer: {time_left_sec}s", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))
    screen.blit(food_text, (10, 60))
    screen.blit(timer_text, (10, 85))

    pygame.display.flip()
    clock.tick(current_fps)

#  game over screen 
screen.fill(BLACK)
game_over_text = font.render("GAME OVER", True, (220, 0, 0))
final_text = small_font.render(f"Final Score: {score}   Level: {level}", True, WHITE)

game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
final_rect = final_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))

screen.blit(game_over_text, game_over_rect)
screen.blit(final_text, final_rect)
pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()
sys.exit()
import pygame
import math

pygame.init()

# Window setup
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Simple Paint")
clock = pygame.time.Clock()

# Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main drawing surface (our "paper")
canvas = pygame.Surface((W, H))
canvas.fill(WHITE)

# Current tool and settings
# brush / rect / circle / eraser / square / r_triangle / e_triangle / rhombus
tool = "brush"
color = BLACK
size = 6

drawing = False
start_pos = (0, 0)
last_pos = None


def make_rect_from_points(p1, p2):
    """Create pygame.Rect from 2 points no matter drag direction."""
    x1, y1 = p1
    x2, y2 = p2
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))


def get_square_rect(start, end):
    """
    Build a square from drag start/end.
    Side is min(dx, dy), so it always stays square.
    """
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    side = min(abs(dx), abs(dy))

    # Keep square in correct drag direction
    sx = x1 if dx >= 0 else x1 - side
    sy = y1 if dy >= 0 else y1 - side

    return pygame.Rect(sx, sy, side, side)


def get_right_triangle_points(start, end):
    """
    Right triangle inside drag rectangle.
    Right angle is at bottom-left corner.
    """
    rect = make_rect_from_points(start, end)

    p1 = (rect.left, rect.bottom)   # right angle
    p2 = (rect.left, rect.top)
    p3 = (rect.right, rect.bottom)

    return [p1, p2, p3]


def get_equilateral_triangle_points(start, end):
    """
    Equilateral-like triangle based on drag width.
    Top point is centered, bottom side is horizontal.
    """
    x1, y1 = start
    x2, y2 = end

    # Use width as triangle side
    side = abs(x2 - x1)
    if side < 2:
        side = 2

    # Direction by mouse drag
    dir_x = 1 if x2 >= x1 else -1
    dir_y = 1 if y2 >= y1 else -1

    # Height of real equilateral triangle: h = sqrt(3)/2 * side
    height = int((math.sqrt(3) / 2) * side)

    # Base points
    base_left = (x1, y1)
    base_right = (x1 + dir_x * side, y1)

    # Top point goes up or down depending on drag
    top = (x1 + dir_x * (side // 2), y1 - dir_y * height)

    return [base_left, base_right, top]


def get_rhombus_points(start, end):
    """
    Rhombus inside drag rectangle using midpoints:
    top, right, bottom, left.
    """
    rect = make_rect_from_points(start, end)

    top = (rect.centerx, rect.top)
    right = (rect.right, rect.centery)
    bottom = (rect.centerx, rect.bottom)
    left = (rect.left, rect.centery)

    return [top, right, bottom, left]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Tool selection
            if event.key == pygame.K_1:
                tool = "brush"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_4:
                tool = "eraser"
            elif event.key == pygame.K_5:
                tool = "square"
            elif event.key == pygame.K_6:
                tool = "r_triangle"
            elif event.key == pygame.K_7:
                tool = "e_triangle"
            elif event.key == pygame.K_8:
                tool = "rhombus"

            # Color selection
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

            # Size for brush/eraser and line thickness for shapes
            elif event.key == pygame.K_UP:
                size = min(50, size + 1)
            elif event.key == pygame.K_DOWN:
                size = max(1, size - 1)

            # Clear canvas
            elif event.key == pygame.K_c:
                canvas.fill(WHITE)

        # Start drawing on left mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos

        # Finish shape on mouse release
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing:
                end_pos = event.pos

                if tool == "rect":
                    rect = make_rect_from_points(start_pos, end_pos)
                    pygame.draw.rect(canvas, color, rect, size)

                elif tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius, size)

                elif tool == "square":
                    sq = get_square_rect(start_pos, end_pos)
                    pygame.draw.rect(canvas, color, sq, size)

                elif tool == "r_triangle":
                    points = get_right_triangle_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, color, points, size)

                elif tool == "e_triangle":
                    points = get_equilateral_triangle_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, color, points, size)

                elif tool == "rhombus":
                    points = get_rhombus_points(start_pos, end_pos)
                    pygame.draw.polygon(canvas, color, points, size)

            drawing = False
            last_pos = None

        # Free drawing while moving mouse
        if event.type == pygame.MOUSEMOTION and drawing:
            mx, my = event.pos

            if tool == "brush":
                pygame.draw.line(canvas, color, last_pos, (mx, my), size)

            elif tool == "eraser":
                pygame.draw.line(canvas, WHITE, last_pos, (mx, my), size * 2)

            last_pos = (mx, my)

    # Draw current canvas
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    # Shape preview while dragging
    if drawing and tool in ["rect", "circle", "square", "r_triangle", "e_triangle", "rhombus"]:
        temp = canvas.copy()
        mx, my = pygame.mouse.get_pos()
        current_pos = (mx, my)

        if tool == "rect":
            rect = make_rect_from_points(start_pos, current_pos)
            pygame.draw.rect(temp, color, rect, size)

        elif tool == "circle":
            x1, y1 = start_pos
            radius = int(((mx - x1) ** 2 + (my - y1) ** 2) ** 0.5)
            pygame.draw.circle(temp, color, start_pos, radius, size)

        elif tool == "square":
            sq = get_square_rect(start_pos, current_pos)
            pygame.draw.rect(temp, color, sq, size)

        elif tool == "r_triangle":
            points = get_right_triangle_points(start_pos, current_pos)
            pygame.draw.polygon(temp, color, points, size)

        elif tool == "e_triangle":
            points = get_equilateral_triangle_points(start_pos, current_pos)
            pygame.draw.polygon(temp, color, points, size)

        elif tool == "rhombus":
            points = get_rhombus_points(start_pos, current_pos)
            pygame.draw.polygon(temp, color, points, size)

        screen.blit(temp, (0, 0))

    # Small help text at top
    font = pygame.font.SysFont(None, 24)
    info = (
        f"Tool: {tool} | Size: {size} | "
        f"1-brush 2-rect 3-circle 4-eraser 5-square 6-rightTri 7-eqTri 8-rhombus | "
        f"R/G/B/K color | C clear"
    )
    text = font.render(info, True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
from ball import Ball


def main():
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Red Ball")

    clock = pygame.time.Clock()
    fps = 60

    white = (255, 255, 255)

    ball = Ball(x=screen_width // 2, y=screen_height // 2, radius=25, color=(255, 0, 0), step=20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move_up(screen_width, screen_height)
                elif event.key == pygame.K_DOWN:
                    ball.move_down(screen_width, screen_height)
                elif event.key == pygame.K_LEFT:
                    ball.move_left(screen_width, screen_height)
                elif event.key == pygame.K_RIGHT:
                    ball.move_right(screen_width, screen_height)

        screen.fill(white)
        ball.draw(screen)
        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()


if __name__ == "__main__":
    main()
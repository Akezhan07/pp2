import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("comicsansms", 72)  
player = MusicPlayer("music")

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))  

    text = font.render("Music Player", True, (255, 0, 0))  #red
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3))

    bar_width = 600
    bar_height = 10
    bar_x = WIDTH // 2 - bar_width // 2
    bar_y = HEIGHT - 80

    progress = player.get_progress()

    pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))

    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (bar_x, bar_y, bar_width * progress, bar_height)
    )

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.prev_track()

            elif event.key == pygame.K_q:
                running = False

    clock.tick(60)

pygame.quit()
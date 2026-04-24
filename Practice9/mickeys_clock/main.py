import pygame
import sys
from clock import MickeyClock

def main():
    pygame.init()
    
    WIDTH, HEIGHT = 1408, 768
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey Mouse Real-Time Clock")
    
    SHOULDER_COORDS = (704, 390)
    
    mickey_clock = MickeyClock(screen, SHOULDER_COORDS)
    
    timer = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255)) 
        mickey_clock.draw()
        
        pygame.display.flip()
        
        timer.tick(60)

if __name__ == "__main__":
    main()
import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen, clock_center):
        self.screen = screen
        self.clock_center = clock_center
        try:
            body_path = os.path.join('images', 'mickey.png')
            self.body = pygame.image.load(body_path).convert_alpha()
        except pygame.error:
            self.body = pygame.image.load('mickey.png').convert_alpha()
        
        try:
            hand_path = os.path.join('images', 'hand1.png')
            self.hand_img = pygame.image.load(hand_path).convert_alpha()
        except pygame.error:
            self.hand_img = pygame.image.load('hand1.png').convert_alpha()

    def draw(self):
        self.screen.blit(self.body, (0, 0))

        now = datetime.datetime.now()
        minute = now.minute
        second = now.second

        
        min_canvas_size = 1000 
        min_hand_scaled = pygame.transform.smoothscale(self.hand_img, (281, 500))
        
        sec_canvas_size = 700
        sec_hand_scaled = pygame.transform.smoothscale(self.hand_img, (int(281 * 0.7), int(500 * 0.7)))

        angle_min = -(minute * 6)
        
        self._draw_rotated_hand(min_hand_scaled, angle_min, min_canvas_size)
        
        angle_sec = -(second * 6)
        
        left_hand_sec = pygame.transform.flip(sec_hand_scaled, True, False)
        
        self._draw_rotated_hand(left_hand_sec, angle_sec, sec_canvas_size)

    def _draw_rotated_hand(self, image, angle, canvas_size):
        rotated_image = pygame.transform.rotate(image, angle)
        
        rotated_rect = rotated_image.get_rect()
        rotated_center = rotated_rect.center
        
        
        orig_rect = image.get_rect()
        offset_to_pivot = pygame.math.Vector2(0, orig_rect.height / 2)
        
        offset_rotated = offset_to_pivot.rotate(-angle) 
        
        draw_pos = (
            self.clock_center[0] - offset_rotated.x - rotated_center[0],
            self.clock_center[1] - offset_rotated.y - rotated_center[1]
        )
        
        self.screen.blit(rotated_image, draw_pos)
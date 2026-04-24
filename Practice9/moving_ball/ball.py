import pygame


class Ball:
    def __init__(self, x, y, radius=25, color=(255, 0, 0), step=20):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step = step

    @property
    def diameter(self):
        return self.radius * 2

    def move(self, dx, dy, screen_width, screen_height):
        new_x = self.x + dx
        new_y = self.y + dy

        if self.radius <= new_x <= screen_width - self.radius and \
           self.radius <= new_y <= screen_height - self.radius:
            self.x = new_x
            self.y = new_y

    def move_up(self, screen_width, screen_height):
        self.move(0, -self.step, screen_width, screen_height)

    def move_down(self, screen_width, screen_height):
        self.move(0, self.step, screen_width, screen_height)

    def move_left(self, screen_width, screen_height):
        self.move(-self.step, 0, screen_width, screen_height)

    def move_right(self, screen_width, screen_height):
        self.move(self.step, 0, screen_width, screen_height)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
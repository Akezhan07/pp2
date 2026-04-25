import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, image_path="images/car1.png"):
        super().__init__()

        # Load player image and resize it to fit the road
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()

        self.w = w
        self.h = h
        self.speed = 5

        # Start near the bottom center
        self.rect.center = (w // 2, h - 70)

    def update(self):
        keys = pygame.key.get_pressed()

        # Move left, but keep player inside the screen
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        # Move right, also keep inside the screen
        if keys[pygame.K_RIGHT] and self.rect.right < self.w:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, h, image_path="images/car2.png", speed=8):
        super().__init__()

        # Enemy car image
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()

        self.w = w
        self.h = h
        self.speed = speed

        self.respawn()

    def respawn(self):
        # Put enemy at random X at the top of the screen
        self.rect.centerx = random.randint(35, self.w - 35)
        self.rect.bottom = 0

    def move(self):
        # Move enemy down every frame
        self.rect.y += self.speed

        # If enemy left the screen, spawn it again from top
        if self.rect.top > self.h:
            self.respawn()

    def increase_speed(self, value=1):
        # Small helper method to increase difficulty
        self.speed += value

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self, w, h, image_path="images/coin.png", speed=6):
        super().__init__()

        # Keep original coin image, then scale based on weight
        self.base_image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.base_image.get_rect()

        self.w = w
        self.h = h
        self.speed = speed

        # Coin value (weight): can be 1, 2 or 3
        self.weight = 1
        self.image = self.base_image

        self.respawn()

    def respawn(self):
        # Randomly choose coin weight
        # 1 is common, 2 is less common, 3 is rare
        self.weight = random.choices([1, 2, 3], weights=[60, 30, 10])[0]

        # Bigger coin = higher value (easy to notice in game)
        size_by_weight = {
            1: 26,
            2: 32,
            3: 40
        }
        size = size_by_weight[self.weight]
        self.image = pygame.transform.scale(self.base_image, (size, size))

        # Need new rect after scaling image
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

        # Spawn coin at random X from the top
        margin = self.rect.width // 2 + 5
        self.rect.centerx = random.randint(margin, self.w - margin)
        self.rect.bottom = 0

    def move(self):
        # Coin falls down
        self.rect.y += self.speed

        # If coin is out of screen, spawn a new one
        if self.rect.top > self.h:
            self.respawn()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
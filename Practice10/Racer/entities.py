import pygame
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, image_path="images\car1.png"):
        super().__init__()
        # load player image
        self.image = pygame.image.load(image_path).convert_alpha()
        # set fixed size for player car
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()

        self.w = w
        self.h = h
        self.speed = 5

        # start near bottom center
        self.rect.center = (w // 2, h - 70)

    def update(self):
        keys = pygame.key.get_pressed()

        # move left
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed

        # move right
        if keys[pygame.K_RIGHT] and self.rect.right < self.w:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, w, h, image_path="images\car2.png", speed=8):
        super().__init__()
        # load enemy image
        self.image = pygame.image.load(image_path).convert_alpha()
        # set fixed size for enemy car
        self.image = pygame.transform.scale(self.image, (60, 100))
        self.rect = self.image.get_rect()

        self.w = w
        self.h = h
        self.speed = speed

        self.respawn()

    def respawn(self):
        # random x at top
        self.rect.centerx = random.randint(35, self.w - 35)
        self.rect.bottom = 0

    def move(self):
        # move enemy down
        self.rect.y += self.speed

        # if enemy leaves screen, respawn
        if self.rect.top > self.h:
            self.respawn()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self, w, h, image_path="images\coin.png", speed=6):
        super().__init__()
        # load coin image
        self.image = pygame.image.load(image_path).convert_alpha()
        # set fixed size for coin
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        self.w = w
        self.h = h
        self.speed = speed

        self.respawn()

    def respawn(self):
        # random x at top
        self.rect.centerx = random.randint(20, self.w - 20)
        self.rect.bottom = 0

    def move(self):
        # move coin down
        self.rect.y += self.speed

        # if coin leaves screen, respawn
        if self.rect.top > self.h:
            self.respawn()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
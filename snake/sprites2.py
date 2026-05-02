import pygame
from settings import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.x, self.y = x, y
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def body_collision(self):
        if self.x == self.game.head.x and self.y == self.game.head.y:
            return True
        return False

    def update(self):
        self.rect.x = TILE_SIZE * self.x
        self.rect.y = TILE_SIZE * self.y

class Food:
    def __init__(self, game, x, y):
        self.color = RED
        self.x = x
        self.y = y
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(self.color)
        self.image_rect = self.image.get_rect()

    def update(self):
        self.image.fill(self.color)
        self.image_rect.x = self.x * TILE_SIZE
        self.image_rect.y = self.y * TILE_SIZE

    def food_collision(self):
        if self.x == self.game.head.x and self.y == self.game.head.y:
            return True
        return False
    def is_golden(self, fl):
        if fl:
            self.color = GOLD
        else:
            self.color = RED

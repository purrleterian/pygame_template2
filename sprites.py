import pygame
from settings import *


vec = pygame.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)

        self.pos = vec(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        self.acc = vec(0, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.acc.x = -PLAYER_FRICTION
            self.direction = "left"

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acc.x = +PLAYER_FRICTION
            self.direction = "right"

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.acc.y = -PLAYER_FRICTION
            self.direction = "down"

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.acc.y = +PLAYER_FRICTION
            self.direction = "up"

        self.acc.x += self.vel.x * AIR_FRICTION
        self.acc.y += self.vel.y * AIR_FRICTION

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

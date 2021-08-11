import pygame
import random
import math

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super(Entity, self).__init__()
        self.pos = pos
        self.size = size
        self.surf = pygame.Surface((self.size[0], self.size[1]))
        self.surf.fill((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.speed = 80
        self.dir = 0
        self.id = 0
        self.angle = math.radians(0)
        self.tag = "entity"
        pass

    def update(self, deltaTime):
        pass

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
        pass

import pygame
import entity
import math
import globals as g

class Enemy(entity.Entity):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.surf = pygame.Surface((self.size[0], self.size[1]))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.speed = 120
        self.dir = 0
        self.id = 0
        self.angle = math.radians(90)
        self.tag = "enemy"
        pass

    def update(self, deltaTime):
        self.pos[0] += (self.speed*math.cos(self.angle)) * deltaTime
        self.pos[1] += (self.speed*math.sin(self.angle)) * deltaTime
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        if (self.pos[1] + self.size[1] > 600):
            g.entities.remove(self)
        pass

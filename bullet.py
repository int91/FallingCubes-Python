import pygame
import entity
import math
import globals as g

class Bullet(entity.Entity):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.surf = pygame.Surface((self.size[0], self.size[1]))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.speed = 140
        self.dir = 0
        self.id = 0
        self.angle = math.radians(270)
        self.tag = "bullet"
        pass

    def update(self, deltaTime):
        self.pos[0] += (self.speed*math.cos(self.angle)) * deltaTime
        self.pos[1] += (self.speed*math.sin(self.angle)) * deltaTime
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        if (self.pos[1] + self.size[1] < 0):
            g.entities.remove(self)
        for e in g.entities:
            if (e.tag == "enemy"):
                if (g.checkCollision(self, e)):
                    g.entities.remove(self)
                    g.entities.remove(e)
        pass

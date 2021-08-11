import pygame
import globals as g
import entity
import bullet

class Player(entity.Entity):
    def __init__(self):
        self.pos = [400, 500]
        self.size = [32, 32]
        self.surf = pygame.Surface((self.size[0], self.size[1]))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        self.speed = 320
        self.sprintSpeed = 480
        self.walkSpeed = 320
        self.vel = [0, 0]
        self.id = 0
        self.tag = "player"
        self.ammo = 3
        self.lives = 3
        self.canShoot = True
        pass

    def update(self, deltaTime):
        self.vel = [0, 0]
        self.speed = self.walkSpeed
        for e in g.entities:
            if (e.tag == "enemy"):
                if (g.checkCollision(self, e)):
                    g.entities.remove(e)
                    self.lives -= 1
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d]):
            if (self.pos[0] > (800-32) - self.speed * g.deltaTime):
                self.pos[0] = 799-32
                self.vel[0] = 0
            else:
                self.vel[0] = 1
        elif (keys[pygame.K_a]):
            if (self.pos[0] < 0 + self.speed * g.deltaTime):
                self.pos[0] = 1
                self.vel[0] = 0
            else:
                self.vel[0] = -1
        if (keys[pygame.K_LSHIFT]):
            self.speed = self.sprintSpeed
        if (keys[pygame.K_SPACE] == True and self.ammo > 0 and self.canShoot):
            g.entities.append(bullet.Bullet([(self.pos[0]+16)-4, self.pos[1]], [8, 14]))
            self.ammo -= 1
            self.canShoot = False
        elif (keys[pygame.K_SPACE] == False):
            self.canShoot = True
        self.pos[0] += self.vel[0] * (self.speed * g.deltaTime)
        self.rect = self.surf.get_rect(topleft=(self.pos[0], self.pos[1]))
        pass

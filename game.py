import pygame
import enemy
import player
import time
import random
import ammobox
import globals as g

class Game():
    def __init__(self):
        pygame.init()
        self.windowWidth = 800
        self.windowHeight = 600
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.clock = pygame.time.Clock()
        self.fpsLock = 60
        self.eSpawnTime = 0.3
        self.eSpawnTimer = 0
        self.aSpawnTime = 4
        self.aSpawnTimer = 0
        g.player = player.Player()
        g.entities.append(g.player)
        g.entities.append(enemy.Enemy([100, 0], [32, 32]))
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])    
        pass

    def update(self):
        t = pygame.time.get_ticks()
        g.deltaTime = (t - g.getTicksLastFrame) / 1000.0
        g.getTicksLastFrame = t
        
        if (self.eSpawnTimer < self.eSpawnTime):
            self.eSpawnTimer +=  1 * g.deltaTime
        else:
            g.entities.append(enemy.Enemy([random.randrange(0, 768), random.randrange(-64, 0)], [32, 32]))
            if (self.eSpawnTime > 0.1):
                self.eSpawnTime -= 0.0001
            self.eSpawnTimer = 0
            pass

        if (self.aSpawnTimer < self.aSpawnTime):
            self.aSpawnTimer +=  1 * g.deltaTime
        else:
            g.entities.append(ammobox.AmmoBox([random.randrange(0, 768), random.randrange(-64, 0)], [24, 24]))
            self.aSpawnTimer = 0
            pass
        
        if (g.player.lives == 0):
            g.running = False
            pass
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    g.running = False

        self.screen.fill(pygame.Color(0, 0, 0))
        for e in g.entities:
            e.update(g.deltaTime)
            e.draw(self.screen)
        self.clock.tick(self.fpsLock)
        pygame.display.update()
        print(self.clock.get_fps())     
        pass

    def draw(self):
        for e in g.entities:
            e.draw(self.screen)
            pass
        pass

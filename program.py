"""Created by: NeoFrags
   Date Created: 07/15/2021
   Last Updated: 08/09/2021
   Avg Dev Time: 5 Hours"""


import pygame
import globals as g
import game

game = game.Game()

while g.running:
    game.update()

pygame.display.quit()
exit()

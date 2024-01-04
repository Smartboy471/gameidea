import pygame
from pygame.locals import *
import Map
import inputHandler
import player
import utils

class game:
    def __init__(self):
        self.running = True
        self.utilities = utils.utils()
        self.player = player.player([320, 320])
        self.blackbox = pygame.image.load("data/img/black.png")
        self.map = Map.Map()
        self.InputHandler = inputHandler.InputHandler(self.player)
        self.FPS = 60
        

    def setUp(self):
        self.map.setUpLevel()
    

    def HandleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            if event.type == KEYDOWN:
                self.InputHandler.UPKeyboardHandler(event)
            if event.type == KEYUP:
                self.InputHandler.DOWNKeyboardHandler(event)
        return 0


    def Update(self):
        self.player.update()
        self.map.getCloseLevelparts(self.player.camera, self.utilities.screenSize)
        pygame.display.update()
        

        
    def Render(self):
        shift = [self.player.camera.pos[0] - (self.utilities.screenSize[0] / 2), self.player.camera.pos[1] - (self.utilities.screenSize[1] / 2)]

        self.map.draw(self.utilities.screen, shift)
        self.player.draw(self.utilities.screen, shift)

    def FinishCalculations(self):
        pygame.time.Clock().tick(self.FPS)

    def Exit(self):
        pygame.quit()
        return 0

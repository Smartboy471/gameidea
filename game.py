import pygame
from pygame.locals import *
import Map
import inputHandler
import player
import utils

class game:
    def __init__(self):
        self.utilities = utils.utils()
        self.map = Map.Map()
        self.player = player.player([320, 320], self.utilities, self.map)
        self.InputHandler = inputHandler.InputHandler(self.player)
        self.deltaTime = 0
        

    def setUp(self):
        self.map.setUpLevel(self.utilities.screenSize)
    
    def isRunning(self):
        return self.utilities.running

    def HandleEvents(self):
        for event in pygame.event.get():

            if event.type == QUIT:
                self.utilities.running = False

            if event.type == KEYDOWN:
                self.InputHandler.DOWNKeyboardHandler(event)

            if event.type == KEYUP:
                self.InputHandler.UPKeyboardHandler(event)

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
        pygame.time.Clock().tick(self.utilities.FPS)
        self.utilities.DeltaTime()

    def Exit(self):
        pygame.quit()
        return 0

import pygame
from pygame.locals import *
import Map
import inputHandler
import player

class game:
    def __init__(self):
        self.running = True
        self.screenSize = [640, 640]
        self.screen = pygame.display.set_mode(self.screenSize, 0, 8, 0, 1)
        self.player = player.player([320, 320])
        self.blackbox = pygame.image.load("data/img/black.png")
        self.map = Map.Map()
        self.InputHandler = inputHandler.InputHandler(self.player)

    def setUp(self):
        self.map.setUpLevel()
    
    def Render(self):
        #Renders backround that the camera sees and one more part
        shift = [self.player.camera.pos[0] - (self.screenSize[0] / 2), self.player.camera.pos[1] - (self.screenSize[1] / 2)]
        self.map.draw(self.player.camera, self.screenSize, self.screen)
        self.player.draw(self.screen, shift)


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
        pygame.display.update()

    def Exit(self):
        pygame.quit()
        return 0

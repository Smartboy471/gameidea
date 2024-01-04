import pygame
class utils:
    def __init__(self) -> None:
        #DELTA TIME 
        self.deltaTime = [0, 0]
        self.get_ticks = pygame.time.get_ticks
        #SCREEN
        self.screenSize = [640, 640]
        self.screen = pygame.display.set_mode(self.screenSize, 0, 8, 0, 1)


    def DeltaTime(self):
        self.deltaTime[0] = self.get_ticks() - self.deltaTime[1]
        self.deltaTime[1] = self.get_ticks()

    def newScreen(self, screenSize, flags=0, depth=0, display=0, vsync=0):
        self.screen = pygame.display.set_mode(screenSize, flags, depth, display, vsync)
        self.screenSize = screenSize
        return self.screen
import pygame
class BackRoundPiece:
    def __init__(self, pos: list, img: str):
        self.pos = pos
        self.size = [32, 32]
        self.surface = pygame.image.load(img)
        self.rect = pygame.Rect(self.pos, self.size)
    def draw(self, screen, shift):
        screen.blit(self.surface, (self.pos[0]-shift[0], self.pos[1]-shift[1]))

class door:
    def __init__(self, pos: list):
        self.pos = pos
        self.size = [32, 32] 
        self.surface = pygame.image.load("data/img/modern_tileB_house3.png")
        self.surfaceClosed = (416, 204, 32, 48)
        self.surfaceFrame = (348, 264, 40, 56)
        self.rect = pygame.Rect(self.pos, self.size)
        self.open = False
    def draw(self, screen, shift):
        screen.blit(self.surface, (self.pos[0]-shift[0], self.pos[1]-shift[1]), self.surfaceFrame)
        screen.blit(self.surface, (self.pos[0]-shift[0]+4, self.pos[1]-shift[1]+4), self.surfaceClosed)
        
    
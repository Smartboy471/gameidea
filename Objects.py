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
    def __init__(self, pos: list, img: str="none"):
        self.pos = pos
        self.size = [32, 32] 
        self.surfaceClosed = pygame.image.load("data/img/Tiles_063.png")
        self.surfaceHalfOpen = pygame.image.load("data/img/Tiles_064.png")
        self.surfaceOpen = pygame.image.load("data/img/Tiles_065.png")
        self.rect = pygame.Rect(self.pos, self.size)
        self.open = False
    def draw(self, screen, shift):
        screen.blit(self.surfaceClosed, (self.pos[0]-shift[0], self.pos[1]-shift[1]))
        screen.blit(self.surfaceHalfOpen, (self.pos[0]-shift[0]+64, self.pos[1]-shift[1]+64))
        screen.blit(self.surfaceOpen, (self.pos[0]-shift[0]+128, self.pos[1]-shift[1]+128))
        
    
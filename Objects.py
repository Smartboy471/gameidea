import pygame
class BackRoundPiece:
    def __init__(self, pos: list, img: str):
        self.pos = pos
        self.size = [32, 32]
        self.surface = pygame.image.load(img)
        self.rect = pygame.Rect(self.pos, self.size)
    def draw(self, screen, shift):
        screen.blit(self.surface, (self.pos[0]-shift[0], self.pos[1]-shift[1]))
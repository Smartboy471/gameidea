import pygame
import camera
class player:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.vel = [0, 0]
        self.size = [32, 32]
        self.surface = pygame.image.load("data/img/player.png")
        self.rect = pygame.Rect(self.pos, self.size)
        self.Drawrect = pygame.Rect(self.pos, self.size)
        self.camera = camera.camera([0, 0])
    def draw(self, screen, shift):
        self.Drawrect = pygame.Rect([self.pos[0] - shift[0]-self.size[0]/2, self.pos[1] - shift[1]-self.size[1]/2], self.size)
        screen.blit(self.surface, self.Drawrect)
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        self.camera.update(self.pos)
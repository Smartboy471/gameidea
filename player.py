import pygame
import camera
import vector2
class player:
    def __init__(self, pos, utils, map) -> None:
        self.vec2 = vector2.Vec2(pos[0], pos[1])
        self.size = [32, 32]
        self.surface = pygame.image.load("data/img/player.png")
        self.rect = pygame.Rect(self.vec2.pos, self.size)
        self.Drawrect = pygame.Rect(self.vec2.pos, self.size)
        self.accel = 5
        self.map = map
        self.utilities = utils
        self.weight = 10
        self.camera = camera.camera([0, 0], self.utilities, self.map)
    def draw(self, screen, shift):
        self.Drawrect = pygame.Rect([self.vec2.pos[0] - shift[0], self.vec2.pos[1] - shift[1]], self.size)
        screen.blit(self.surface, self.Drawrect)
    def update(self, friction):
        self.vec2.vel = vector2.Intmul(self.vec2.vel, friction)
        self.vec2.addVelwithDeltaTime(self.utilities.deltaTime)
        self.camera.update(vector2.Vec2add(self.vec2.pos, vector2.Intdiv(self.size, 2)))
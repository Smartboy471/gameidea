import pygame
from pygame.locals import *
class InputHandler:
    def __init__(self, player) -> None:
        self.player = player
        self.deltaTimeEstimate = 16
    def DOWNKeyboardHandler(self, event):

        if event.key == K_w:
            self.player.vel[1] -= 5 / self.deltaTimeEstimate
        if event.key == K_s:
            self.player.vel[1] += 5 / self.deltaTimeEstimate
        if event.key == K_a:
            self.player.vel[0] -= 5 / self.deltaTimeEstimate
        if event.key == K_d:
            self.player.vel[0] += 5 / self.deltaTimeEstimate
            
    def UPKeyboardHandler(self, event):
        if event.key == K_w:
            self.player.vel[1] += 5 / self.deltaTimeEstimate
        if event.key == K_s:
            self.player.vel[1] -= 5 / self.deltaTimeEstimate
        if event.key == K_a:
            self.player.vel[0] += 5 / self.deltaTimeEstimate
        if event.key == K_d:
            self.player.vel[0] -= 5 / self.deltaTimeEstimate
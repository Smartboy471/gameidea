import pygame, vector2
from pygame.locals import *
class InputHandler:
    def __init__(self, player, utils) -> None:
        self.player = player
        self.deltaTimeEstimate = 16
        self.utils = utils
    def DOWNKeyboardHandler(self, event):
        return 0
        #match event.key:
        #    
        #    case pygame.K_w:
        #        
        #        self.player.vec2.addToVel([0, (-5/self.deltaTimeEstimate)])
        #    case pygame.K_s:
        #        self.player.vec2.addToVel([0,(5/self.deltaTimeEstimate)])
        #    case pygame.K_a:
        #        self.player.vec2.addToVel([(-5/self.deltaTimeEstimate), 0])
        #    case pygame.K_d:
        #        self.player.vec2.addToVel([(5/self.deltaTimeEstimate), 0])
            
    def UPKeyboardHandler(self, event):
        return 0
        #match event.key:
        #    case pygame.K_w:
        #        if self.player.vec2.vel[1] < -0.01:
        #            self.player.vec2.vel[1] = 0
        #    case pygame.K_s:
        #        if self.player.vec2.vel[1] > 0.01:
        #            self.player.vec2.vel[1] = 0
        #    case pygame.K_a:
        #        if self.player.vec2.vel[0] < -0.01:
        #            self.player.vec2.vel[0] = 0
        #    case pygame.K_d:
        #        if self.player.vec2.vel[0] > 0.01:
        #            self.player.vec2.vel[0] = 0

    def KeyboardHandler(self):
        for key in self.utils.Keys:
            if key[0] ==  pygame.K_w:
                if key[1] == True:
                    
                    self.player.vec2.vel[1] = -5/self.deltaTimeEstimate
                else:
                    if self.player.vec2.vel[1] < 0:
                        self.player.vec2.vel[1] = 0
                
            if key[0] == pygame.K_s:
                if key[1] == True:
                    self.player.vec2.vel[1] = 5/self.deltaTimeEstimate
                else:
                    if self.player.vec2.vel[1] > 0:
                        self.player.vec2.vel[1] = 0
                
            if key[0] == pygame.K_a:
                if key[1] == True:
                    self.player.vec2.vel[0] = -5/self.deltaTimeEstimate
                else:
                    if self.player.vec2.vel[0] < 0:
                        self.player.vec2.vel[0] = 0
                
            if key[0] == pygame.K_d:
                if key[1] == True:
                    self.player.vec2.vel[0] = 5/self.deltaTimeEstimate
                else:
                    if self.player.vec2.vel[0] > 0:
                        self.player.vec2.vel[0] = 0
                
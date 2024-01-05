screenSize = [640, 640]
class camera:
    def __init__(self, pos, utils, map) -> None:
        self.pos = pos
        self.vel = [0, 0]
        self.topleftpos = [self.pos[0]-(screenSize[0]/2), self.pos[1]-(screenSize[1]/2)]
        self.utilities = utils
        self.map = map
    def update(self, hostPos):
        self.vel[0] = ((hostPos[0] - self.pos[0]) /10)
        self.vel[1] = ((hostPos[1] - self.pos[1]) /10)  
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        right = self.map.levelsize[0] * self.map.levelPartSize[0] - (screenSize[0]/2)
        left = self.utilities.screenSize[0]/2
        bottom = self.map.levelsize[1] * self.map.levelPartSize[1] - (screenSize[1]/2)
        top = self.utilities.screenSize[1]/2

        if self.pos[0] <= left:
            self.pos[0] = left

        elif self.pos[0] >= right:
            self.pos[0] = right


        if self.pos[1] <= top:
            self.pos[1] = top
        
        elif self.pos[1] >= bottom:
            self.pos[1] = bottom

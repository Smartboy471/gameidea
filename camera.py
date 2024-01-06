
class camera:
    def __init__(self, pos, utils, map) -> None:
        self.pos = pos
        self.vel = [0, 0]
        self.utilities = utils
        self.topleftpos = [self.pos[0]-(self.utilities.screenSize[0]/2), self.pos[1]-(self.utilities.screenSize[1]/2)]
        self.map = map
    def update(self, hostPos):
        self.vel[0] = ((hostPos[0] - self.pos[0]) /10)
        self.vel[1] = ((hostPos[1] - self.pos[1]) /10)  
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        right = self.map.LevelPixelSize[0] - (self.utilities.screenSize[0]/2)
        left = self.utilities.screenSize[0]/2
        bottom = self.map.LevelPixelSize[1] - (self.utilities.screenSize[1]/2)
        top = self.utilities.screenSize[1]/2

        if self.pos[0] <= left:
            self.pos[0] = left

        elif self.pos[0] >= right:
            self.pos[0] = right


        if self.pos[1] <= top:
            self.pos[1] = top
        
        elif self.pos[1] >= bottom:
            self.pos[1] = bottom

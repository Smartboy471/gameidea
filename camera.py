import vector2
class camera:
    def __init__(self, pos, utils, map) -> None:
        self.vec2 = vector2.Vec2(pos[0], pos[1])
        self.utilities = utils
        self.topleftpos = [self.vec2.pos[0]-(self.utilities.screenSize[0]/2), self.vec2.pos[1]-(self.utilities.screenSize[1]/2)]
        self.map = map
    def update(self, hostPos):
        self.vec2.vel = (vector2.Intdiv(vector2.Vec2sub(hostPos, self.vec2.pos), 10))
        self.vec2.addVel()

        right = self.map.LevelPixelSize[0] - (self.utilities.screenSize[0]/2)
        left = self.utilities.screenSize[0]/2
        bottom = self.map.LevelPixelSize[1] - (self.utilities.screenSize[1]/2)
        top = self.utilities.screenSize[1]/2

        if self.vec2.pos[0] <= left:
            self.vec2.pos[0] = left

        elif self.vec2.pos[0] >= right:
            self.vec2.pos[0] = right


        if self.vec2.pos[1] <= top:
            self.vec2.pos[1] = top
        
        elif self.vec2.pos[1] >= bottom:
            self.vec2.pos[1] = bottom

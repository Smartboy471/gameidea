screenSize = [640, 640]
class camera:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.vel = [0, 0]
        self.topleftpos = [self.pos[0]-(screenSize[0]/2), self.pos[1]-(screenSize[1]/2)]
    def update(self, hostPos):
        print(hostPos)
        self.vel[0] = ((hostPos[0] - self.pos[0]) /10)
        self.vel[1] = ((hostPos[1] - self.pos[1]) /10)  
        self.vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
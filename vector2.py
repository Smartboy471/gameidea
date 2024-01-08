def Vec2add(vec2_1, vec2_2):
    vec = [vec2_1[0]+vec2_2[0], vec2_1[1]+vec2_2[1]]
    return vec
def Vec2sub(vec2_1, vec2_2):
    vec = [vec2_1[0]-vec2_2[0], vec2_1[1]-vec2_2[1]]
    return vec
def Vec2mul(vec2_1, vec2_2):
    vec = [vec2_1[0]*vec2_2[0], vec2_1[1]*vec2_2[1]]
    return vec
def Vec2div(vec2_1, vec2_2):
    vec = [vec2_1[0]/vec2_2[0], vec2_1[1]/vec2_2[1]]
    return vec
def Intadd(vec2, int: int):
    vec = [vec2[0]+int, vec2[1]+int]
    return vec
def Intsub(vec2, int: int):
    vec = [vec2[0]-int, vec2[1]-int]
    return vec
def Intmul(vec2, int: int):
    vec = [vec2[0]*int, vec2[1]*int]
    return vec
def Intdiv(vec2, int: int):
    vec = [vec2[0]/int, vec2[1]/int]
    return vec



class Vec2:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.vel = [0, 0]
    def addVel(self):
        self.pos = Vec2add(self.pos, self.vel)
        return self.pos
    def addVelwithDeltaTime(self, deltaTime):
        vel = Intmul(self.vel, deltaTime)
        self.pos = Vec2add(self.pos, vel)
        return self.pos
    
    def addToVel(self, vec2):
        self.vel = Vec2add(self.vel, vec2)
        return self.vel
    def subToVel(self, vec2):
        self.vel = Vec2sub(self.vel, vec2)
        return self.vel
    def mulToVel(self, vec2):
        self.vel = Vec2mul(self.vel, vec2)
        return self.vel
    def divToVel(self, vec2):
        self.vel = Vec2div(self.vel, vec2)
        return self.vel

import JH, Objects

class Map:
    def __init__(self) -> None:
        self.JsonLevel = JH.JsonReader("data/level/level.json")["level"]
        self.levelsize = [64, 64]
        self.Level = []
        self.levelPartSize = [32, 32]
        self.CloseLevelparts = []
        self.door = Objects.door([32, 32])
    
    def setUpLevel(self):
        for y in range(0, self.levelsize[0]):
            self.Level.append([])
            for x in range(0, self.levelsize[1]):

                if 0 == self.JsonLevel[y][x]:
                    self.Level[y].append(Objects.BackRoundPiece([x*self.levelPartSize[0], y*self.levelPartSize[1]], "data/img/floor.png"))

                if 1 == self.JsonLevel[y][x]:
                    self.Level[y].append(Objects.BackRoundPiece([x*self.levelPartSize[0], y*self.levelPartSize[1]], "data/img/wall.png"))

        return self.Level
    
    def draw(self, screen, shift):
        for part in self.CloseLevelparts:
            part.draw(screen, shift)
        self.door.draw(screen, shift)

    def getCloseLevelparts(self, camera, screenSize):
        self.CloseLevelparts = []
        for y in range(int((camera.pos[1] - (screenSize[1] / 2) - self.levelPartSize[1]) / self.levelPartSize[1]), int(((screenSize[1] + self.levelPartSize[1]) / self.levelPartSize[1])+(camera.pos[1] - (screenSize[1] / 2)) / self.levelPartSize[1])):
            for x in range(int((camera.pos[0] - (screenSize[0] / 2) - self.levelPartSize[0]) / self.levelPartSize[0]), int((screenSize[0] + self.levelPartSize[0]) / self.levelPartSize[0] + (camera.pos[0] - (screenSize[0] / 2)) / self.levelPartSize[0])):
                try:
                    self.CloseLevelparts.append(self.Level[y][x])
                except IndexError:
                    pass
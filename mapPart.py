import JH, Objects
from pygame import time

class Level:
    def __init__(self, jsonPart, size, partsize, names, partAmounts, objectType) -> None:
        self.JsonLevel = JH.JsonReader("data/level/level.json")[jsonPart]
        self.Levelsize = size
        self.Level = []
        self.LevelPartSize = partsize
        self.CloseLevelparts = []
        self.names = names
        self.objectType = objectType
        self.partAmounts = partAmounts

    def setUpLevel(self):
        for y in range(0, self.Levelsize[0]):
            self.Level.append([])
            for x in range(0, self.Levelsize[1]):
                for i in range(0, self.partAmounts):
                    if i == self.JsonLevel[y][x]:
                        if self.names[i] != None:
                            self.Level[y].append(self.objectType([x*self.LevelPartSize[0], y*self.LevelPartSize[1]], self.names[i]))
                    
        return self.Level
    
    def draw(self, screen, shift):
        for part in self.CloseLevelparts:
            part.draw(screen, shift)

    def getCloseLevelparts(self, camera, screenSize):
        
        
        left = int((camera.pos[0] - (screenSize[0] / 2) - self.LevelPartSize[0]) / self.LevelPartSize[0])
        right = int((screenSize[0] + self.LevelPartSize[0]) / self.LevelPartSize[0] + (camera.pos[0] - (screenSize[0] / 2)) / self.LevelPartSize[0])
        top = int((camera.pos[1] - (screenSize[1] / 2) - self.LevelPartSize[1]) / self.LevelPartSize[1])
        bottom = int(((screenSize[1] + self.LevelPartSize[1]) / self.LevelPartSize[1])+(camera.pos[1] - (screenSize[1] / 2)) / self.LevelPartSize[1])

        self.CloseLevelparts = []
        for y in range(top, bottom):
            for x in range(left, right):
                try:
                    self.CloseLevelparts.append(self.Level[y][x])
                except IndexError:
                    pass
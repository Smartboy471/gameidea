import JH, Objects, pygame

class Map:
    def __init__(self) -> None:
        self.LevelPixelSize = [8192, 8192]
        self.BackroundLevel = ["data/img/floor.png", "data/img/wall.png"]
        self.BackroundLevelsize = [256, 256]
        self.BackroundLevelPartSize = [32, 32]
        self.BackroundNames = [None, "data/img/floor.png", "data/img/wall.png"]
        self.JsonLevel = JH.JsonReader("data/level/level.json")["backround"]
        self.Level = []
        self.chunkSize = [64, 64]
        self.loadedChunks = []
        self.loadedChunksPos = [0, 0]
        self.doors = [Objects.door((480, 480))]
    
    def setUpLevel(self, screenSize):
        #self.BackroundLevel
        #for y in range(0, self.BackroundLevelsize[0]):
        #    self.BackroundLevel.append([])
        #    for x in range(0, self.BackroundLevelsize[1]):
        #        for i in range(0, 3):
        #            if i == self.JsonLevel[y][x]:
        #                if self.BackroundNames[i] != None:
        #                    self.BackroundLevel[y].append(Objects.BackRoundPiece([x*self.BackroundLevelPartSize[0], y*self.BackroundLevelPartSize[1]], self.BackroundNames[i]))


        #Self.Level
        for y in range(0, int(self.LevelPixelSize[1]/self.chunkSize[1])):
            self.Level.append([])
            for x in range(0, int(self.LevelPixelSize[0]/self.chunkSize[0])):
                self.Level[y].append([[[(self.JsonLevel[2*y][2*x]), (self.JsonLevel[2*y][2*x+1])], [(self.JsonLevel[2*y+1][2*x]), (self.JsonLevel[2*y+1][2*x+1])]]])
        #LoadedChunks
        left = 0
        right = int((screenSize[0] + (4*self.chunkSize[0])) / self.chunkSize[0])
        top = 0
        bottom = int((screenSize[1] + (4*self.chunkSize[1])) / self.chunkSize[1])
        chunkY = 0
        for y in range(top, bottom):
            chunkX = 0
            self.loadedChunks.append([])
            for x in range(left, right):
                self.loadedChunks[chunkY].append(self.Level[y][x])
                chunkX += 1
            chunkY +=1
        for door in self.doors:
            levelPos = [door.pos[0]//self.chunkSize[0], door.pos[1]//self.chunkSize[1]]
            self.Level[levelPos[0]][levelPos[1]].append(door)
        return 0
    
    def draw(self, screen, shift:list):
        surfaceFloor = pygame.image.load(self.BackroundLevel[0])
        surfaceWall = pygame.image.load(self.BackroundLevel[1])
        for y in range(0, len(self.loadedChunks)):
            for x in range(0, len(self.loadedChunks[y])):
                for part in self.loadedChunks[y][x]:
                    if type(part) == list:
                        for loadedY in range(0, len(part)):
                            for loadedX in range(0, len(part[loadedY])):
                                
                                if type(part[loadedY][loadedX]) == int:
                                    if part[loadedY][loadedX] == 0:
                                        continue
                                    if part[loadedY][loadedX] == 1:
                                        pos = [self.loadedChunksPos[0]+((x)*self.chunkSize[0])+(loadedX*32)-shift[0], self.loadedChunksPos[1]+((y)*self.chunkSize[1])+(loadedY*32)-shift[1]]
                                        if pos[0]<0:
                                            pos[0]=0
                                        if pos[1]<0:
                                            pos[1]=0
                                        screen.blit(surfaceFloor, pos)
                        
                                    if part[loadedY][loadedX] == 2:
                                        pos = [self.loadedChunksPos[0]+((x)*self.chunkSize[0])+(loadedX*32)-shift[0], self.loadedChunksPos[1]+((y)*self.chunkSize[1])+(loadedY*32)-shift[1]]
                                    
                                        screen.blit(surfaceWall, pos)
                    else:
                        part.draw(screen, shift)
        return 0

    def getCloseLevelparts(self, camera, screenSize):
        cameraPos = [(camera.pos[0] - (screenSize[0] / 2)), (camera.pos[1] - (screenSize[1] / 2))]

        left = int((cameraPos[0] - 1*self.chunkSize[0]) // self.chunkSize[0])
        right = int((screenSize[0] + (2*self.chunkSize[0]) + cameraPos[0]) // self.chunkSize[0])
        top = int((cameraPos[1] - 1*self.chunkSize[1]) // self.chunkSize[1])
        bottom = int((screenSize[1] + (2*self.chunkSize[1]) + cameraPos[1]) // self.chunkSize[1])
        self.loadedChunksPos = [left*self.chunkSize[0], top*self.chunkSize[1]]
        chunkY = 0
        for y in range(top, bottom):
            chunkX = 0
            for x in range(left, right):
                if self.loadedChunks[chunkY][chunkX] != self.Level[y][x]:
                    self.loadedChunks[chunkY][chunkX] = self.Level[y][x]
                chunkX += 1
            chunkY +=1
        return 0
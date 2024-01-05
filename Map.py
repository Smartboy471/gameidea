import JH, Objects, mapPart

class Map:
    def __init__(self) -> None:
        self.LevelSize = [12288, 12288]

        self.backroundLevel = mapPart.Level("backround", [384, 384], [32, 32], ["data/img/floor.png", "data/img/wall.png"], 2, Objects.BackRoundPiece)

        self.doorLevel = mapPart.Level("door", [256, 256], [48, 48], [None, "stanard img"], 2, Objects.door)

        
    
    def setUpLevel(self):
        self.backroundLevel.setUpLevel()
        self.doorLevel.setUpLevel()
        return 0
    
    def draw(self, screen, shift):
        self.backroundLevel.draw(screen, shift)
        self.doorLevel.draw(screen, shift)
        return 0

    def getCloseLevelparts(self, camera, screenSize):
        self.backroundLevel.getCloseLevelparts(camera, screenSize)
        self.doorLevel.getCloseLevelparts(camera, screenSize)
        return 0
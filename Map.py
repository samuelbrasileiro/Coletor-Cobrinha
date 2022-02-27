# The Map Class
from Terrain import Terrain
class Map():
    
    def __init__(self, tileSize, scl):
        self.tileSize = tileSize
        self.scl = scl
        self.rows = height/self.tileSize
        self.columns = width/self.tileSize
        self.__makeTiles()
        
    def __makeTiles(self):
        self.tiles = [[self.getTerrain(i, j) for i in range(self.columns)] for j in range(self.rows)]
        self.printMap()
        
    def display(self):
        noStroke()
        for i in range(self.columns):
            for j in range(self.rows):
                fill(self.getColor(i, j))
                rect(i * self.tileSize, j * self.tileSize, self.tileSize, self.tileSize)
    
    def getColor(self, x, y):
        terrain = self.getTerrain(x, y)
        if terrain == Terrain.water:
            return color(155, 255, 255)
        elif terrain == Terrain.sand:
            return color(30, 255, 255)
        elif terrain == Terrain.grass:
            return color(66, 255, 255)
        else: 
            return color(80, 255, 200)
        
    def getTerrain(self, x, y):
        v = noise(x * self.scl, y * self.scl)
        if v < 0.3:
            return Terrain.water
        elif v < 0.4:
            return Terrain.sand
        elif v < 0.7:
            return Terrain.grass
        else:
            return Terrain.tree
        
    def getTiles(self):
        return self.tiles
    
    def getTile(self, position):
        return self.tiles[floor(position.y)][floor(position.x)]

    def generateTargetPosition(self, origin):
        origin = origin/self.tileSize
        
        target = self.__randomTile()
        while self.__isUnreacheable(origin, target):
            target = self.__randomTile()
        return target*self.tileSize
    
    def __isUnreacheable(self, origin, target):
        return self.getTile(target) == Terrain.tree
    
    def __randomTile(self):
        return PVector(floor(random(self.columns)), floor(random(self.rows)))
    
    def printMap(self):
        s = [[str(e) for e in row] for row in self.tiles]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)

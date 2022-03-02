# The Map Class
from Terrain import Terrain
class Map():
    
    def __init__(self, tileSize, scl):
        self.tileSize = tileSize
        self.scl = scl
        self.visited = []
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
    
    def getTile(self, (x, y)):
        return self.tiles[y][x]
    
    def getValidTile(self):
        target = self.__randomTile()
        while self.isBlocked(target):
            target = self.__randomTile()
        return target
    
    def gridPositionFromPosition(self, (x, y)):
        return int((y + self.tileSize/2) // self.tileSize), int((x + self.tileSize/2) // self.tileSize)
    
    def getNeighbours(self, row, col):
        neighbours = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i == 0 and j == 0:
                    continue
                checkX = col + i
                checkY = row + j
                
                if checkX >= 0 and checkX < self.columns and checkY >= 0 and checkY < self.rows:
                    neighbours.append((checkX, checkY))
        return neighbours
                
    def isBlocked(self, target):
        return self.getTile(target) == Terrain.tree
    
    def isTileBlocked(self, row, col):
        return self.tiles[row][col] == Terrain.tree
    
    def __randomTile(self):
        return (floor(random(self.columns)), floor(random(self.rows)))

    def resetVisited(self):
        self.visited = []
    
    def printMap(self):
        s = [[str(e) for e in row] for row in self.tiles]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print '\n'.join(table)

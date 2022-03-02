#The PathFollower class

class PathFollower:
    def __init__(self, path, tileSize):
        self.path = path
        self.current = 0
        self.count = len(path)
        self.tileSize = tileSize
    
    def arrive(self):
        self.current += 1
    
    def getTarget(self):
        if not self.didFinish():
            (x, y) = self.path[self.current]
            return PVector(x, y) * self.tileSize
    
    def getTile(self):
        if not self.didFinish():
            return self.path[self.current]
    
    def didFinish(self):
        return self.current == self.count

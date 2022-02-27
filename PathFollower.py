#The PathFollower class

class PathFollower:
    def __init__(self, path, tileSize):
        self.path = path
        self.current = 0
        self.count = len(path)
        print(self.count)
        self.tileSize = tileSize
    
    def arrive(self):
        self.current += 1
    
    def getTarget(self):
        if not self.didFinish():
            (x, y) = self.path[self.current]
            return PVector(x, y) * self.tileSize
    
    def didFinish(self):
        return self.current == self.count

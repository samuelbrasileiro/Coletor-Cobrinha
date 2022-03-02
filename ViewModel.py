# The View Model Class

from Food import Food
from Vehicle import Vehicle
from Map import Map
from PathViewer import PathViewer
from PathFollower import PathFollower
from Algorithm import Algorithm

class ViewModel():
    
    def __init__(self):
        self.count = 0
        self.tileSize = 32
        self.waitFrames = 5 # is equal to a .08s wait
        self.frmCount = 0
        self.makeMap()
        self.makeViewer()
        self.makeVehicle()
        self.makeFood()
        self.makeFollower(self.vehicle.position, self.food.position)
            
    def makeFood(self):
        position = self.map.getValidTile()
        self.food = Food(position, self.tileSize)
        
    def makeVehicle(self):
        position = self.map.getValidTile()
        self.vehicle = Vehicle(position, self.tileSize)
    
    def makeMap(self):
        self.map = Map(self.tileSize, 0.1)
        
    def makeViewer(self):    
        self.viewer = PathViewer(self.tileSize)
    
    def makeFollower(self, startPos, targetPos):
        pathFinder = Algorithm.AStar(self.map, self.viewer)
        path = pathFinder.findPath((startPos.x, startPos.y), (targetPos.x, targetPos.y))

        if (not len(path)):
            self.makeFood()
            self.map.resetVisited()
            self.makeFollower(self.vehicle.position, self.food.position)
        else:
            self.follower = PathFollower(path, self.tileSize)
        
        
    def collectFood(self):
        self.updateScore()
        self.makeFood() 
        self.viewer.reset()
        self.map.resetVisited()
        self.makeFollower(self.vehicle.position, self.food.position)        
        self.frmCount = 0
    
    def updateScore(self):
        self.count += 1
        print("Score: " + str(self.count))
        
    def update(self):
        self.frmCount += 1
        if not self.viewer.finished:
            if self.frmCount >= self.waitFrames:
                self.viewer.paintIteratively()
                self.frmCount = 0        
        else:
            if self.follower.didFinish():
                self.collectFood()
            target = self.follower.getTarget()
            weight = self.map.getTile(self.follower.getTile())
            if self.isVehicleCloseEnoughToTarget(target):
                self.follower.arrive()
            
            self.vehicle.arrive(target)
            self.vehicle.update(weight)
            
        self.display()

    def isVehicleCloseEnoughToTarget(self, target):
        return eucledean(self.vehicle.position, target) < (self.vehicle.r)
    
    def display(self):
        self.map.display()
        self.viewer.display()
        self.food.display()
        self.vehicle.display()

def eucledean(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

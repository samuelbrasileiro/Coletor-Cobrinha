# The View Model Class

from Food import Food
from Vehicle import Vehicle
from Map import Map
from PathViewer import PathViewer
from PathFollower import PathFollower

class ViewModel():
    
    def __init__(self):
        self.count = 0
        self.tileSize = 32
        self.makeMap()
        self.makeViewer()
        self.makeVehicle()
        self.makeFood()
        self.makeFollower()
        self.viewer.paintPath(self.follower.path)
            
    def makeFood(self):
        position = self.map.generateTargetPosition(self.vehicle.getPosition())
        self.food = Food(position, self.tileSize)
        
    def makeVehicle(self):
        self.vehicle = Vehicle(width / 2, height / 2, self.tileSize)
    
    def makeMap(self):
        self.map = Map(self.tileSize, 0.1)
        
    def makeViewer(self):    
        self.viewer = PathViewer(self.tileSize)
    
    def makeFollower(self):
        path = [(20,10), (21,10), (22,10), (22,11), (22,12), (22,13), (22,14), (22,15), (22,16)]
        self.follower = PathFollower(path, self.tileSize)
        
    def collectFood(self):
        self.updateScore()
        self.makeFood()
        self.makeFollower()
        self.viewer.resetColors()
        self.viewer.paintPath(self.follower.path)
    
    def updateScore(self):
        self.count += 1
        print("Score: " + str(self.count))
        
    def update(self):
        if self.follower.didEnded():
            self.collectFood()
        target = self.follower.getTarget()
        weight = self.map.getTile(self.vehicle.getPosition()/self.tileSize)
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

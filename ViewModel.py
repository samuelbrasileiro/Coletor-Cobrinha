# The View Model Class

from Food import Food
from Vehicle import Vehicle
from Map import Map
from PathViewer import PathViewer

class ViewModel():
    
    def __init__(self):
        self.count = 0
        self.makeMap()
        self.makeVehicle()
        self.makeFood()
        self.makeViewer()
            
    def makeFood(self):
        position = self.map.generateTargetPosition(self.vehicle.getPosition())
        self.food = Food(position)
        
    def makeVehicle(self):
        self.vehicle = Vehicle(width / 2, height / 2)
    
    def makeMap(self):
        self.map = Map(16, 0.1)
        
    def makeViewer(self):    
        self.viewer = PathViewer(self.map)
    
    def collectFood(self):
        self.updateScore()
        self.makeFood()
        self.vehicle.arrive()
    
    def updateScore(self):
        self.count += 1
        print("Score: " + str(self.count))
        
    def update(self):
        if self.vehicle.isFoodLocated():
            self.vehicle.seek()
        else:
            self.vehicle.locateFood(self.food)
        
        self.vehicle.update()
        self.vehicle.boundaries()
        if self.isVehicleCloseEnoughToFood():
            self.collectFood()
        self.display()
    
    def isVehicleCloseEnoughToFood(self):
        return eucledean(self.vehicle.position, self.food.position) < (self.food.r + self.vehicle.r - 4)
    
    def display(self):
        self.map.display()
        self.viewer.display()
        self.food.display()
        self.vehicle.display()

def eucledean(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

# The View Model Class

from Food import Food
from Vehicle import Vehicle

class ViewModel():
    
    def __init__(self):
        self.count = 0
        self.makeFood()
        self.makeVehicle()
                              
    def makeFood(self):
        self.food = Food()
        
    def makeVehicle(self):
        self.vehicle = Vehicle(width / 2, height / 2)
        
    def collectFood(self):
        self.updateScore()
        self.makeFood()
        self.vehicle.arrive()
    
    def updateScore(self):
        self.count += 1
        print("Score: " + str(self.count))
        
    def update(self):
        if self.vehicle.isFoodLocated():
            self.vehicle.drive()
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
        self.vehicle.display()
        self.food.display()

def eucledean(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

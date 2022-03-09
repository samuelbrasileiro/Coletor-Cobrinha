# The View Model Class

from Food import Food
from Vehicle import Vehicle
from Map import Map
from PathViewer import PathViewer
from PathFollower import PathFollower
from Algorithm import Algorithm

global selected_option

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
        #self.makeFollower(self.vehicle.position, self.food.position)
        
        self.enteredOnce = False
        self.chosen = False
            
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
    
    def makeFollower(self, startPos, targetPos, keypressed):
        
        if(key == '1'):
            pathFinder = Algorithm.AStar(self.map, self.viewer)
        elif(key == '2'):
            pathFinder = Algorithm.Dijkstra(self.map, self.viewer)
        elif(key == '3'):
            pathFinder = Algorithm.BFS(self.map, self.viewer)
        elif(key == '4'):
            pathFinder = Algorithm.DFS(self.map, self.viewer)
        elif(key == '5'):
            pathFinder = Algorithm.Greedy(self.map, self.viewer)
            
        path = pathFinder.findPath((startPos.x, startPos.y), (targetPos.x, targetPos.y))
        #print(path)

        if (not len(path)):
            self.makeFood()
            self.map.resetVisited()
            self.makeFollower(self.vehicle.position, self.food.position, '1')
        else:
            self.follower = PathFollower(path, self.tileSize)
        
        
    def collectFood(self):
        self.updateScore()
        self.makeFood() 
        self.viewer.reset()
        self.map.resetVisited()
        #self.makeFollower(self.vehicle.position, self.food.position)        
        self.frmCount = 0
    
    def updateScore(self):
        self.count += 1
        print("Score: " + str(self.count))
        
    def update(self):
        
        if(keyPressed and not self.chosen):
            self.enteredOnce = True
            if(key == '1'):
                self.makeFollower(self.vehicle.position, self.food.position,'1')
                self.chosen = True
            elif(key == '2'):
                self.makeFollower(self.vehicle.position, self.food.position,'2')
                self.chosen = True
            elif(key == '3'):
                self.makeFollower(self.vehicle.position, self.food.position,'3')
                self.chosen = True
            elif(key == '4'):
                self.makeFollower(self.vehicle.position, self.food.position,'4')
                self.chosen = True
            elif(key == '5'):
                self.makeFollower(self.vehicle.position, self.food.position,'5')
                self.chosen = True
            
        if(self.enteredOnce):
            self.frmCount += 1
            if not self.viewer.finished:
                if self.frmCount >= self.waitFrames:
                    self.viewer.paintIteratively()
                    self.frmCount = 0        
            else:
                if self.follower.didFinish():
                    self.collectFood()
                    self.chosen = False
                    self.enteredOnce = False
                else:
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

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
        self.makeFollower(self.vehicle.position, self.food.position, '1')
        self.pathFinder = Algorithm.AStar(self.map, self.viewer)
        
        self.newkey = 1
        self.chosenAlgo = 'AStar'
            
    def makeFood(self):
        position = self.map.getValidTile()
        self.food = Food(position, self.tileSize)
        
    def makeVehicle(self):
        position = self.map.getValidTile()
        self.vehicle = Vehicle(position, self.tileSize)
    
    def makeMap(self):
        self.map = Map(self.tileSize, 0.3)
        
    def makeViewer(self):    
        self.viewer = PathViewer(self.tileSize)
    
    def makeFollower(self, startPos, targetPos, keypressed):
        
        if(keypressed == '1'):
            self.pathFinder = Algorithm.AStar(self.map, self.viewer)
            self.chosenAlgo = 'AStar'
        elif(keypressed == '2'):
            self.pathFinder = Algorithm.Dijkstra(self.map, self.viewer)
            self.chosenAlgo = 'Djikstra'
        elif(keypressed == '3'):
            self.pathFinder = Algorithm.BFS(self.map, self.viewer)
            self.chosenAlgo = 'BFS'
        elif(keypressed == '4'):
            self.pathFinder = Algorithm.DFS(self.map, self.viewer)
            self.chosenAlgo = 'DFS'
        elif(keypressed == '5'):
            self.pathFinder = Algorithm.Greedy(self.map, self.viewer)
            self.chosenAlgo = 'Guloso'
            
        path = self.pathFinder.findPath((startPos.x, startPos.y), (targetPos.x, targetPos.y))
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
        self.makeFollower(self.vehicle.position, self.food.position, self.newkey)        
        self.frmCount = 0
    
    def updateScore(self):
        self.count += 1
        print("Score: " + str(self.count))
        
    def update(self):
        
        if(keyPressed):
            if(key == '1'):
                self.newkey = '1'
            elif(key == '2'):
                self.newkey = '2'
            elif(key == '3'):
                self.newkey = '3'
            elif(key == '4'):
                self.newkey = '4'
            elif(key == '5'):
                self.newkey = '5'
            
        self.frmCount += 1
        if not self.viewer.finished:
            if self.frmCount >= self.waitFrames:
                self.viewer.paintIteratively()
                self.frmCount = 0        
        else:
            if self.follower.didFinish():
                self.collectFood()
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

EXPLORED_COLOR = color(230, 0, 255)
PATH_COLOR = color(186, 20, 31, 255)

class PathViewer:
    """
    This class has useful methods to draw the chosen path by many algorithms
    """
    
    def __init__(self, tileSize):
        self.tileSize = tileSize
        self.colorsToDisplay = {}
        self.path = []
        self.exploredNodes = []
        self.indexToPaint = -1
        self.finished = False
    
        
    def paintExploredNode(self, x, y):
        """
        Paints a node with default color for explored nodes
        """
        if (x, y) not in self.exploredNodes:
            self.exploredNodes.append((x, y))
        
    def paintExplored(self, exploredNodes):
        """        
        Paints a list of nodes with default color for explored nodes
        """
        self.exploredNodes = exploredNodes
        for (x, y) in exploredNodes:
            self.paintExploredNode(x, y)
        
    def paintPathNode(self, x, y):
        """
        Paints a node with default color for path nodes
        """        
        if (x, y) not in self.path:
            self.path.append((x, y))
        
    def paintPath(self, path):
        """
        Paints a list of nodes with default color for path nodes
        """
        self.path = path
        for (x, y) in path:
            self.paintPathNode(x, y)
        
    def restoreColor(self, x, y):
        """
        Restores specific grid position color
        """
        if (x, y) in self.colorsToDisplay:
            self.colorsToDisplay.pop((x,y))     
            
    def resetColors(self):
        """
        Resets all grid colors
        """
        self.colorsToDisplay = {}
            
    def reset(self):
        """
        Resets object state
        """
        self.finished = False        
        self.indexToPaint = -1   
        self.colorsToDisplay = {}
        self.path = []
        self.exploredNodes = []
            
    def display(self):
        for (i, j) in self.colorsToDisplay.keys():
            fill(self.colorsToDisplay[(i, j)])
            rect(i * self.tileSize, j * self.tileSize, self.tileSize, self.tileSize)
            
    def displayTile(self, i, j, newColor):
        self.colorsToDisplay[(i, j)] = newColor
            
    def paintIteratively(self):
        """
        Paints one node at time, starting from explored nodes
        """
        self.indexToPaint += 1
        if self.indexToPaint >= (len(self.path) + len(self.exploredNodes)):
            self.finished = True
            return
        elif self.indexToPaint >= len(self.exploredNodes):
            self.finished = False
            i = self.indexToPaint - len(self.exploredNodes)
            col, row = self.path[i]
            self.displayTile(col, row, PATH_COLOR)
        else:
            self.finished = False
            i = self.indexToPaint
            col, row = self.exploredNodes[i]
            self.displayTile(col, row, EXPLORED_COLOR)
            
        
            
        
        

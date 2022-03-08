EXPLORED_COLOR = color(230, 0, 255, 140)
BORDER_COLOR = color(230, 0, 255, 180)
PATH_COLOR = color(186, 20, 31, 255)

class PathViewer:
    """
    This class has useful methods to draw the chosen path by many algorithms
    """
    
    def __init__(self, tileSize):
        self.tileSize = tileSize
        self.colorsToDisplay = {}
        self.path = []
        self.borderAndExplored = {}
        self.indexToPaint = -1
        self.finished = False    
        
    def paintBorderAndExplored(self, animFrame, borderNodes, exploredNodes):
        """
        Adds border and explored nodes to animation in specified frame
        """
        self.borderAndExplored[animFrame] = (borderNodes, exploredNodes)
        
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
        self.borderAndExplored = {}
            
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
        if self.indexToPaint >= (len(self.path) + len(self.borderAndExplored)):
            self.finished = True
            return
        elif self.indexToPaint >= len(self.borderAndExplored):
            self.finished = False
            i = self.indexToPaint - len(self.borderAndExplored)
            col, row = self.path[i]
            self.displayTile(col, row, PATH_COLOR)
        else:
            self.finished = False
            i = self.indexToPaint
            if i in self.borderAndExplored:
                border, explored = self.borderAndExplored[i]    
                for node in border:
                    row, col = tuple(node)
                    self.displayTile(col, row, BORDER_COLOR) 
                for node in explored:
                    row, col = tuple(node)
                    self.displayTile(col, row, EXPLORED_COLOR)
            
        
            
        
        

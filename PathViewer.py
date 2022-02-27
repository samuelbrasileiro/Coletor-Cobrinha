EXPLORED_COLOR = color(230, 0, 255)
PATH_COLOR = color(186, 20, 31)

class PathViewer:
    """
    This class has useful methods to draw the chosen path by many algorithms
    """
    
    def __init__(self, map):
        self.map = map
        self.newColors = {}
        
    def paint(self, x, y, newColor):
        """
        Fills rectangle centered at (x, y) with specified color
        """   
        self.newColors[(x, y)] = newColor
        
    def paintExploredNode(self, x, y):
        """
        Paints a node with default color for explored nodes
        """     
        self.newColors[(x, y)] = EXPLORED_COLOR
        
    def paintPathNode(self, x, y):
        """
        Paints a node with default color for path nodes
        """
        self.newColors[(x, y)] = PATH_COLOR
        
    def restoreColor(self, x, y):
        if (x, y) in self.newColors:
            self.newColors.pop((x,y))
            
            
    def resetColors(self):
        for k in self.newColors.keys():
            self.newColors.pop(k)
            
    def display(self):
        for (i, j) in self.newColors.keys():
            fill(self.newColors[(i, j)])
            rect(i * self.map.tileSize, j * self.map.tileSize, self.map.tileSize, self.map.tileSize)
        
            
        
        

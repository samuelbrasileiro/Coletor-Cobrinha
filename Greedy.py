from Queue import PriorityQueue

class Greedy():
    """
    Implements the BFS path finding algorithm
    """
    def __init__(self, map, pathViewer):
        self.parent = {}
        self.visited = set()
        
        self.frontier = PriorityQueue()
        self.map = map
        self.viewer = pathViewer
        
    def heuristic(self, x,y):
    # Manhattan distance on a square grid
        #print(self.map.getTile((x,y)))
        return self.map.getTile((x, y))
        
    def findPath(self, startPos, targetPos):
        startRow, startCol = self.map.gridPositionFromPosition(startPos)
        targetRow, targetCol = self.map.gridPositionFromPosition(targetPos)
        
        target = (targetRow, targetCol)
        source = (startRow, startCol)
        print(startRow)
        print(startCol)
        print("qie")
        print(targetRow)
        print(targetCol)
        print("eiq")
        
        quickpath = []
        
        self.frontier.put((source, 0))
        came_from = dict()
        came_from[source] = None
        
        while not self.frontier.empty():
            current = self.frontier.get()[0]
            
            (row,col) = current
            
            if current == target:
                v = target
                quickpath.append((row,col))
                while came_from[v] != None:
                    quickpath.append(came_from[v])
                    v = came_from[v]
                break

            #currentRow, currentCol = self.map.gridPositionFromPosition((current[0],current[1]))
            for next in self.map.getNeighbours(row,col):
                if next not in came_from:
                    (nrow,ncol) = next
                    priority = self.heuristic(nrow, ncol)
                    self.frontier.put((next, priority))
                    came_from[next] = current
        
        quickpath.reverse()
        print(quickpath)
        return quickpath
    
    def toNodes(self, tiles):
        """
        Converts list of tuples (col, row) to Node
        """
        nodes = []
        for (x, y) in tiles:
            nodes.append(Node((x * self.map.tileSize, y * self.map.tileSize), y, x, self.map.tiles[y][x]))
        return nodes

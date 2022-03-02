import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return not self.elements
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

class BFS:
    """
    Implements the BFS path finding algorithm
    """
    def __init__(self, map, pathViewer):
        self.parent = {}
        self.visited = set()
        self.queue = Queue()

        self.map = map
        self.viewer = pathViewer
    
    def getNeighbours(self, rowPos, colPos):
        up = (rowPos - 1, colPos)
        down = (rowPos + 1, colPos)
        left = (rowPos, colPos - 1)
        right = (rowPos, colPos + 1)

        return [up, right, down, left]

    def isValidNeighbour(self, rowPos, colPos):
        if (rowPos < 0 or colPos <0): return False
        if (rowPos >= self.map.rows or colPos >= self.map.columns): return False
        return not self.map.isTileBlocked(rowPos, colPos)
        
    def findPath(self, startPos, targetPos):
        startRow, startCol = self.map.gridPositionFromPosition(startPos)
        targetRow, targetCol = self.map.gridPositionFromPosition(targetPos)
        target = (targetRow, targetCol)
        start = (startRow, startCol)
        
        self.queue.put(start)
        self.parent[start] = None

        while not self.queue.empty():
            current = self.queue.get()
            if current in self.visited:
                continue

            if current == target:
                return self.backtrace(start, target)

            (row, col) = current
            if current not in self.visited:
                row, col = current
                self.viewer.paintExploredNode(col, row)
                self.visited.add(current)
                self.map.visited.append(current)
            
            neighbours = self.getNeighbours(row, col)
            for neighbour in neighbours:
                (neighbourRow, neighbourCol) = neighbour
                if neighbour not in self.visited and self.isValidNeighbour(neighbourRow, neighbourCol):
                    self.queue.put(neighbour)
                    if neighbour not in self.parent:
                        self.parent[neighbour] = current
        
        return []
         
    def backtrace(self, start, target):
        """
        Backtraces path from target to start
        """
        (startRow, startCol) = target
        (targetRow, targetCol) = target
        path = [(targetCol, targetRow)]

        current = target
        while self.parent[current] != None:
            (parentRow, parentCol) = self.parent[current]
            path.append((parentCol, parentRow))
            current = self.parent[current]
        
        # Paint path including the vehicle position
        path.append((startCol, startRow))
        path.reverse()
        self.viewer.paintPath(path)
        
        # Take out the vehicle position
        path.pop(0)
        return path

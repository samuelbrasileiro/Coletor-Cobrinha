from Container import Stack, Queue

class XFS(object):
    """
    Implements the BFS or DFS path finding algorithm
    """
    def __init__(self, map, pathViewer, container):
        self.parent = {}
        self.visited = set()
        self.container = container # It is a Queue if BFS and a Stack if DFS

        self.map = map
        self.viewer = pathViewer
    
    def getNeighbours(self, rowPos, colPos):
        up = (rowPos - 1, colPos)
        down = (rowPos + 1, colPos)
        left = (rowPos, colPos - 1)
        right = (rowPos, colPos + 1)

        return [up, right, down, left]

    def isValidNeighbour(self, rowPos, colPos):
        # If tile is beyond the map
        if (rowPos < 0 or colPos < 0): return False
        if (rowPos >= self.map.rows or colPos >= self.map.columns): return False
        # Else: if tile is not blocked by an obstacle
        return not self.map.isTileBlocked(rowPos, colPos)
        
    def findPath(self, startPos, targetPos):
        # Define start and target tiles
        startRow, startCol = self.map.gridPositionFromPosition(startPos)
        targetRow, targetCol = self.map.gridPositionFromPosition(targetPos)
        target = (targetRow, targetCol)
        start = (startRow, startCol)
        
        # Step 1: put the start tile in the container
        self.container.put(start)
        self.parent[start] = None

        while not self.container.empty():
            # Step 2: take a tile of the container and add it to the visited list of tiles (if not already in there)
            current = self.container.get()
            if current in self.visited:
                continue

            # Stop condition: if the popped item of the container corresponds to the target
            if current == target:
                return self.backtrace(start, target)

            (row, col) = current
            if current not in self.visited:
                row, col = current
                self.viewer.paintExploredNode(col, row)
                self.visited.add(current)
                self.map.visited.append(current)
            
            # Step 3: create a list of neighbour tiles and add the ones which aren't in the visited list to the top of the container
            neighbours = self.getNeighbours(row, col)
            for neighbour in neighbours:
                (neighbourRow, neighbourCol) = neighbour
                # If the neighbour wasn't visited and is valid
                if neighbour not in self.visited and self.isValidNeighbour(neighbourRow, neighbourCol):
                    # Add to the top of the container
                    self.container.put(neighbour)
                    if neighbour not in self.parent:
                        self.parent[neighbour] = current
        
        return []
         
    def backtrace(self, start, target):
        """
        Backtraces path from target to start
        """
        (startRow, startCol) = start
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

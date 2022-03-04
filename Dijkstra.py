from Container import PriorityQueue

class Node:
    """
    The node class for Dijkstra pathfinding algorithm
    """
    def __init__(self, parent, cost, explored, position):
        self.parent = parent
        self.cost = cost
        self.explored = explored
        self.position = position
    
    def __str__(self):
        return "pos: ({0} | cost: {1} | explored: {2} | parent: {3}".format(self.position, self.cost, self.explored, self.parent)

class Dijkstra(object):
    """
    Implements the Dijkstra path finding algorithm
    """
    def __init__(self, map, pathViewer):
        self.map = map
        self.viewer = pathViewer
        self.container = PriorityQueue()
        self.createNodes()
    
    def createNodes(self):
        # Creating all nodes with default values
        self.nodes = {}
        for row in range(self.map.rows):
            for column in range(self.map.columns):
                self.nodes[(row, column)] = Node(None, float('inf'), False, (row, column))
        
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
        
        return True
        
    def findPath(self, startPos, targetPos):
        # Define start and target tiles
        startRow, startCol = self.map.gridPositionFromPosition(startPos)
        start = (startRow, startCol)
        targetRow, targetCol = self.map.gridPositionFromPosition(targetPos)
        target = (targetRow, targetCol)
        
        # Step 1: put the start tile in the container and set its values
        self.nodes[(startRow, startCol)] = Node(None, 0, False, start)
        self.container.put(start, 0)

        while not self.container.empty():
            # Step 2: take a tile of the container and get its node
            current = self.container.get()
            currentNode = self.nodes[current]

            if currentNode.explored:
                continue

            # Stop condition: if the popped item of the container corresponds to the target
            if current == target:
                row, col = current
                self.viewer.paintExploredNode(col, row)
                return self.backtrace(start, target)
            
            # If tile hasn't been explored, mark itz explored attribute as True
            (row, col) = current
            if not currentNode.explored:
                row, col = current
                self.viewer.paintExploredNode(col, row)
                currentNode.explored = True
            
            # Step 3: create a list of neighbour tiles and add the ones which hasn't been explored to the top of the container
            neighbours = self.getNeighbours(row, col)
            for neighbour in neighbours:
                (neighbourRow, neighbourCol) = neighbour
                if (not self.isValidNeighbour(neighbourRow, neighbourCol)):
                    continue

                neighbourNode = self.nodes[neighbour]
                newCost = currentNode.cost + self.map.getTile((neighbourCol, neighbourRow))

                # If the neighbour wasn't explored and the old cost is bigger than the new one
                if not neighbourNode.explored and (newCost < neighbourNode.cost):
                    # Add to the container with its newCost as a priority value
                    self.container.put(neighbour, newCost)
                    neighbourNode.parent = current
                    neighbourNode.cost = newCost
        
        return []
         
    def backtrace(self, start, target):
        """
        Backtraces path from target to start
        """
        (startRow, startCol) = start
        (targetRow, targetCol) = target
        path = [(targetCol, targetRow)]

        current = target
        while self.nodes[current].parent != None:
            (parentRow, parentCol) = self.nodes[current].parent
            path.append((parentCol, parentRow))
            current = self.nodes[current].parent
        
        # Paint path including the vehicle position
        path.append((startCol, startRow))
        path.reverse()
        self.viewer.paintPath(path)
        
        # Take out the vehicle position
        path.pop(0)
        return path

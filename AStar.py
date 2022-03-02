class Node:
    """
    The node class for A* pathfinding algorithm
    """
    def __init__(self, position, row, col, cost):
        self.position = position
        self.row = row
        self.col = col
        self.cost = cost
        self.hCost = 0
        self.gCost = 0
        self.parent = None
    
    def fCost(self):
        return self.hCost + self.gCost
    
    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.row == self.row and obj.col == self.col
    
    def __ne__(self, obj):
        return not self == obj
    
    def __str__(self):
        return "{0} | ({1}, {2}) | hCost: {3} | gCost: {4} | nodeCost: {5}".format(self.position, self.row, self.col, self.hCost, self.gCost, self.cost)


class AStar:
    """
    Implements the A* path finding algorithm
    """
    def __init__(self, map, pathViewer):
        self.map = map
        self.viewer = pathViewer
        
    def toNodes(self, tiles):
        """
        Converts list of tuples (col, row) to Node
        """
        nodes = []
        for (x, y) in tiles:
            nodes.append(Node((x * self.map.tileSize, y * self.map.tileSize), y, x, self.map.tiles[y][x]))
        return nodes
    
    def distance(self, nodeA, nodeB):
        """
        Computes distance between 2 nodes (non eucledean)
        """
        distX = abs(nodeA.col - nodeB.col)
        distY = abs(nodeA.row - nodeB.row)
        
        if distX > distY:
            return (14*distY + 10*(distX - distY))
        return (14*distX + 10*(distY - distX))
        
    def findPath(self, startPos, targetPos):
        """
        Finds path given start and end positions
        """
        targetRow, targetCol = self.map.gridPositionFromPosition(targetPos)
        targetNode = Node(targetPos, targetRow, targetCol, 1)
        startRow, startCol = self.map.gridPositionFromPosition(startPos)
        startNode = Node(startPos, startRow, startCol, 1)
        
        openSet = []
        closedSet = []
        openSet.append(startNode)
        
        while openSet:
            currentNode = openSet[0]
            for node in openSet[1:]:
                if node.fCost() < currentNode.fCost() or (node.fCost() == currentNode.fCost() and node.hCost < currentNode.hCost):
                    currentNode = node
            openSet.remove(currentNode)
            closedSet.append(currentNode)
            self.viewer.paintExploredNode(currentNode.col, currentNode.row)
            
            if currentNode == targetNode:
                return self.retracePath(startNode, currentNode)
            
            for n in self.toNodes(self.map.getNeighbours(currentNode.row, currentNode.col)):
                if self.map.isTileBlocked(n.row, n.col) or n in closedSet:
                    continue
                                
                costToNeighbour = currentNode.gCost + self.distance(currentNode, n) + n.cost
                
                if costToNeighbour < n.gCost or n not in openSet:
                    n.gCost = costToNeighbour
                    n.hCost = self.distance(n, targetNode)
                    n.parent = currentNode
                    if n not in openSet:
                        openSet.append(n)
                    else:
                        i = openSet.index(n)
                        openSet[i] = n
        return []
                        
    def retracePath(self, startNode, endNode):
        """
        Retraces path from 
        """
        currentNode = endNode
        path = []
        while currentNode != startNode and currentNode != None:
            path.append((currentNode.col, currentNode.row))
            currentNode = currentNode.parent
        path.append((startNode.col, startNode.row))
        path.reverse()
        self.viewer.paintPath(path)
        return path
        
                
                    
    

from XFS import XFS
from Container import Queue

class BFS(XFS):
    def __init__(self, map, pathViewer):
        super(BFS, self).__init__(map, pathViewer, Queue())

from XFS import XFS
from Container import Stack

class DFS(XFS):
    def __init__(self, map, pathViewer):
        super(DFS, self).__init__(map, pathViewer, Stack())

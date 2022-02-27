#The PathFollower class

class PathFollower:
    def __init__(self, path):
        self.path = path
        self.current = 0
        self.count = len(path)

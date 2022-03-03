from collections import deque

class Stack:
    def __init__(self):
        self.elements = deque()
    
    def empty(self):
        return not self.elements
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop()

class Queue:
    def __init__(self):
        self.elements = deque()
    
    def empty(self):
        return not self.elements
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

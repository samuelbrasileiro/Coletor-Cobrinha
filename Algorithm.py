#The Algorithm Enum

from AStar import AStar
from BFS import BFS

def enum(**enums):
    return type('Enum', (), enums)

global Algorithm 

Algorithm = enum(AStar = AStar, BFS = BFS)

def name(self):
    if self == Algorithm.AStar:
        return "AStar"
    elif self == Algorithm.BFS:
        return "BFS"

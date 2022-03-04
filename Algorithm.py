#The Algorithm Enum

from AStar import AStar
from BFS import BFS
from DFS import DFS
from Dijkstra import Dijkstra

def enum(**enums):
    return type('Enum', (), enums)

global Algorithm 

Algorithm = enum(AStar = AStar, BFS = BFS, DFS = DFS, Dijkstra = Dijkstra)

def name(self):
    if self == Algorithm.AStar:
        return "AStar"
    elif self == Algorithm.BFS:
        return "BFS"
    elif self == Algorithm.DFS:
        return "DFS"
    elif self == Algorithm.Dijkstra:
        return "Dijkstra"

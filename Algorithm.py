#The Algorithm Enum

from AStar import AStar
from BFS import BFS
from DFS import DFS
from Dijkstra import Dijkstra
from Greedy import Greedy

def enum(**enums):
    return type('Enum', (), enums)

global Algorithm 

Algorithm = enum(AStar = AStar, BFS = BFS, DFS = DFS, Greedy = Greedy, Dijkstra = Dijkstra)

def AlgorithmName(algo):
    if algo == Algorithm.AStar:
        return "AStar"
    elif algo == Algorithm.BFS:
        return "BFS"
    elif algo == Algorithm.DFS:
        return "DFS"
    elif algo == Algorithm.Dijkstra:
        return "Dijkstra"
    elif algo == Algorithm.Greedy:
        return "Guloso"

def AlgorithmLabel():
    return "1: {}, 2: {}, 3: {}, 4: {}, 5: {}".format(AlgorithmName(Algorithm.AStar), AlgorithmName(Algorithm.Dijkstra),AlgorithmName(Algorithm.BFS), AlgorithmName(Algorithm.DFS), AlgorithmName(Algorithm.Greedy))

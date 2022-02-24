#The Terrain Enum

def enum(**enums):
    return type('Enum', (), enums)

global Terrain 
Terrain = enum(water=15, sand=5, grass=1, tree=float('inf'))

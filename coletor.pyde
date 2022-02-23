# Draws a "vehicle" on the screen

from ViewModel import ViewModel

def setup():
    global viewModel
    size(640, 360)
    viewModel = ViewModel()

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    viewModel.update()    
    

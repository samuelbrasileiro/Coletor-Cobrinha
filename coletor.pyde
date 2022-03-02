
from ViewModel import ViewModel

def setup():
    global viewModel
    size(800, 640)
    frameRate(60)
    viewModel = ViewModel()
    noStroke()
    colorMode(HSB)

def draw():
    mouse = PVector(mouseX, mouseY)
    viewModel.update()    


from ViewModel import ViewModel

def setup():
    global viewModel
    size(800, 640)
    viewModel = ViewModel()
    noStroke()
    colorMode(HSB)

def draw():
    viewModel.update()

    # Escreve score na tela
    font = loadFont("OCRAExtended-20.vlw")
    textFont(font, 20)
    fill(0, 0, 0)
    score = "Score: " + str(viewModel.count)
    text(score, 15, 25)

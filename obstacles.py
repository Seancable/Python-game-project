from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Obstacle:
    def __init__(self, x, y, length, height, thickness, colour):
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.length = length
        self.height = height
        self.thickness = thickness
        self.colour = colour

    def draw(self, canvas):
        canvas.draw_line(self.location, (self.length, self.height), self.thickness, self.colour)
        
        

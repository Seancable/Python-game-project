from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Bullet:
    def __init__(self,sheet):
        self.sheet=sheet
        self.pos=Vector(0,0)
        self.vel=Vector(10,0)
        self.colour='Yellow'
        self.border=1
        self.radius=5
    def draw(self,canvas):
        canvas.draw_circle(self.pos.get_p(),self.radius,self.border,self.colour,self.colour)
    def update(self):
        self.pos.add(self.vel)
    def is_fired(self):
        if self.pos==Vector(0,0):
            return True
        else:
            return False

from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up=False
        self.fire=False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['space']:
            self.up = True
        if key == simplegui.KEY_MAP['F']:
            self.fire =  True
            
 
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['space']:
            self.up = False
        if key == simplegui.KEY_MAP['F']:
            self.fire = False

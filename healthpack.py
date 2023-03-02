from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH=500
HEIGHT=500
IMAGE=simplegui.load_image('https://opengameart.org/sites/default/files/preview_843.png')

class HealthPack:
    def __init__(self):
        self.height=IMAGE.get_height()
        self.width=IMAGE.get_width()
        self.pos=Vector(WIDTH/2,HEIGHT/2)

    def draw(self,canvas):
        canvas.draw_image(IMAGE, (self.width/2,self.height/2),(self.width,self.height),self.pos.get_p(),(100,100))
                          
hp=HealthPack()     
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(hp.draw)
frame.start()

from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH=500
HEIGHT=500
IMAGE=simplegui.load_image('https://opengameart.org/sites/default/files/preview_843.png')

class HealthPack:
    def __init__(self,pos):
        self.height=IMAGE.get_height()
        self.width=IMAGE.get_width()
        self.pos=pos
        self.used=False

    def draw(self,canvas):
        if self.used==False:
            canvas.draw_image(IMAGE, (self.width/2,self.height/2),(self.width,self.height),self.pos.get_p(),(50,50))

'''                          
hp=HealthPack()     
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(hp.draw)
frame.start()
'''

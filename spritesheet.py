from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH= 500
HEIGHT= 500
IMAGE=simplegui.load_image('http://www.inkfood.com/wordprez/wp-content/uploads/SpriteSheet.png')


class Spritesheet:
    def __init__(self):
        self.row=
        self.col=3
        self.width=IMAGE.get_width()
        self.height=IMAGE.get_height() 
        self.rows=(self.height/self.row)/2
        self.cols=(self.width/self.row)/2

    def draw(self,canvas):
        canvas.draw_image(IMAGE, (self.cols, self.rows), (self.width/self.col, self.height/self.row), (250, 250), (500,500))
    def next_frame(self):
        self.cols+=self.width/self.col
        if self.cols>=self.width:
            self.cols=(self.width/self.col)/2
            self.rows+=self.height/self.row
            if self.rows>=self.height:
                self.rows=(self.height/self.row)/2

class Clock:
    def __init__(self):
        self.time=0
    def tick(self):
        self.time+=1
    def transistion(self,frame_duration):
        if self.time % frame_duration==0:
            return True
        else:
            return False


sheet=Spritesheet()
clock=Clock()
def draw(canvas):
    sheet.draw(canvas)
    clock.tick()
    if clock.transistion(10)==True:
        sheet.next_frame()
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.start()

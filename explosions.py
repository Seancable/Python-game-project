from vectorClass import Vector
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH=500
HEIGHT=500
IMAGE=simplegui.load_image('https://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png')


class SpriteSheet:
    def __init__(self):
        self.row=5
        self.col=6
        self.num_frames = 0
        self.width=IMAGE.get_width()
        self.height=IMAGE.get_height()
        self.rows=150
        self.cols=150
        self.explosions = []
        
    def draw(self,canvas):
        if len(self.explosions) == 0:
            self.make_list()
        for x in self.explosions:
            canvas.draw_image(IMAGE, x[0], x[1], x[2], (870,870))

    def make_list(self):
        new_list = []
        for num in range(0, 2):
            random_x, random_y = random.randint(0, 500), random.randint(0,500)
            self.explosions.append([(self.cols, self.rows), (self.width/self.col, self.height/self.row), (random_x, random_y), (870,870)])
        
    def next_frame(self):
        for x in self.explosions:
            x[0] = (x[0][0] + (self.width/self.col)*2, x[0][1])
            #self.cols+=(self.width/self.col)*2
            #self.rows += self.height/self.row + 22
            if x[0][0]>=self.width + 10:
                x[0] = (150, x[0][1])
                self.rows += self.height/self.row + 22
                x[0] = (x[0][0], x[0][1] + (self.height/self.row + 22))
                if self.done(x):
                    x[0] = (150, 150)

 
    def done(self, x):
        return x[0][1] >= 1000

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
            
                
sheet=SpriteSheet()
clock=Clock()
def draw(canvas):
    sheet.draw(canvas)
    clock.tick()
    if clock.transistion(10)==True:
        sheet.next_frame()
        pass
def my_click_handler(position):
    print(position)
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(my_click_handler)
frame.start()


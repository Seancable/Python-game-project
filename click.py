import random, math
from vector import Vector
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 400
HEIGHT = 300
class Ball:
    def __init__(self, position, radius,colour):   
        self.position=position
        self.velocity=Vector(0,0)
        self.radius=radius
        self.colour=colour
    def draw(self,canvas):
        canvas.draw_circle(self.position.get_p(), self.radius,self.radius*2, self.colour)
        self.update()
    def get_radius(self):
        return self.radius
    def set_pos(self,pos):
        self.position=list(pos)
    def update(self):
        self.position.add(self.velocity)
    def set_velocity(self,x,y):
        self.velocity=Vector(x/5,y/5)
        
        

class Mouse:
    def __init__(self):
        self.position=None
    def click_pos(self):
        click=self.position
        self.position=None
        return click
    def handler(self,handle):
        self.position=handle
            
class interaction:
    def __init__(self,ball,mouse):
        self.ball=ball
        self.mouse=mouse
    def point(self,point1,point2):
        if point1==None or point2==None:
            return 100
        else:
            return math.sqrt(((point1[0]-point2[0])** 2) + ((point1[1] - point2[1]) ** 2))
    def interact(self,canvas):
        clicked=self.mouse.click_pos()
        if clicked==None:
            self.ball.draw(canvas)
        else:
            move2=Vector(clicked[0],clicked[1])
            if self.point(self.ball.position.get_p(),clicked)<self.ball.radius*2:
                move2.subtract(self.ball.position)
                self.ball.set_velocity(move2.get_p()[0],move2.get_p()[1])
                #self.ball.colour='Black'
                self.ball.draw(canvas)
            else:
                self.ball.position=Vector(clicked[0],clicked[1])
                self.ball.set_velocity(0,0)
                self.ball.draw(canvas)

# Create a frame and assign callbacks to event handlers
start=Vector(int(WIDTH/2),int(HEIGHT/2))
ball = Ball(start,20,'Red')
mouse=Mouse()
interaction=interaction(ball,mouse)
frame = simplegui.create_frame("Click", WIDTH, HEIGHT)
frame.set_mouseclick_handler(mouse.handler)
frame.set_draw_handler(ball.draw)
frame.set_draw_handler(interaction.interact)

# Start the frame animation
frame.start()

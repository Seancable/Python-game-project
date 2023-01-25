import random, math
from vector import Vector
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 400
HEIGHT = 300
class Ball:
    def __init__(self, position, velocity, radius,colour):   
        self.position=position
        self.velocity=velocity
        self.radius=radius
        self.colour=colour
    def draw(self,canvas):
        canvas.draw_circle(self.position, self.radius,self.radius*2, self.colour)
    def get_radius(self):
        return self.radius
    def set_pos(self,pos):
        self.position=list(pos)
    #def update():
    def set_velocity():
        self.velocity=0
        
        

class Mouse:
    def __init__(self):
        self.position=None
    def click_pos(self,pos):
        self.position=pos
            
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
        #move1=Vector(self.ball.position)
        #move2=Vector(self.mouse.position)
        if self.mouse.position==None:
            canvas.draw_circle(self.ball.position, self.ball.radius,self.ball.radius*2, self.ball.colour)
        else:
            if self.point(self.ball.position,self.mouse.position)<self.ball.radius*2:
                #direction=move1.subtract(move2)
                #self.ball.position=move1.add(direction)
                self.ball.colour='Black'
                canvas.draw_circle(self.ball.position, self.ball.radius,self.ball.radius*2, self.ball.colour)
            else:
                self.ball.position=self.mouse.position
                self.mouse.position=None
                canvas.draw_circle(self.ball.position, self.ball.radius,self.ball.radius*2, self.ball.colour)


# Create a frame and assign callbacks to event handlers
velocity=random.randrange(-5,5)
ball = Ball((int(WIDTH/2),int(HEIGHT/2)),velocity,20,'Red')
mouse=Mouse()
interaction=interaction(ball,mouse)
frame = simplegui.create_frame("Click", WIDTH, HEIGHT)
frame.set_mouseclick_handler(mouse.click_pos)
frame.set_draw_handler(ball.draw)
frame.set_draw_handler(interaction.interact)

# Start the frame animation
frame.start()

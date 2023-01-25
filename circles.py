from vectorClass import Vector
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def randCol():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

def randRadius():
    return random.randrange(10, 50)

class Ball:
    def __init__(self, position, velocity, radius, colour):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.colour = colour

    def draw(self, canvas):
        self.update()
        canvas.draw_circle(self.position.get_p(), self.radius, self.radius*2, self.colour)

    def update(self):
        self.velocity = Vector(random.randrange(-5, 5), random.randrange(-5, 5))
        self.position.add(self.velocity)

    def __str__(self):
        return f"{self.position}, {self.velocity}, {self.radius}, {self.colour}"

WIDTH, HEIGHT = 400, 200
frame = simplegui.create_frame(" Colours ", WIDTH, HEIGHT)
velocity = Vector(random.randrange(-5, 5))
position = Vector(WIDTH/2, HEIGHT/2)
ballList = []

def timer_handler():
    global ballList
    velocity = Vector(random.randrange(-5, 5))
    position = Vector(WIDTH/2, HEIGHT/2)
    ball = Ball(position, velocity, randRadius(), randCol())
    ballList.append(ball)
    for ball in ballList:
        print(ballList)
        frame.set_draw_handler(ball.draw)
def timer_handler2():
    print(1)
    for ball in ballList:
        print(ballList)
        frame.set_draw_handler(ball.draw)

print(1)
print(ballList)


timer = simplegui.create_timer(2000, timer_handler)
timer2 = simplegui.create_timer(0.1, timer_handler2)
timer.start()
timer2.start()
#start the frame animation
print(10)
frame.start()


        

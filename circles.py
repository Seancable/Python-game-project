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
        #draws each circle in the gloabl ballList
        self.update(False)
        for balls in ballList:
            canvas.draw_circle(balls.position.get_p(), balls.radius, balls.radius*2, balls.colour)

    def offScreen(self, balls):
        #returns True if any of the circles are off the screen
        x, y, radi = balls.position.get_p()[0], balls.position.get_p()[1], balls.radius
        return x > WIDTH + radi or y > HEIGHT + radi or x < WIDTH - (400 + radi) or y < HEIGHT - (200 + radi)

    def update(self, flag):
        #updates the velocity of each ball so that they can move randomly around the screen
        #removes balls if their size = 1 or if offScreen method returns True
        for balls in ballList:
            balls.velocity = Vector(random.randrange(-4, 5), random.randrange(-4, 5))
            balls.position.add(balls.velocity)
            if flag and balls.radius > 1:
                balls.radius -= 1
            elif balls.radius == 1:
                ballList.remove(balls)
                print("The number of balls on the screen:", len(ballList))
                
            if self.offScreen(balls):
                ballList.remove(balls)
                print("The number of balls on the screen:", len(ballList))

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
    print("The number of balls on the screen:", len(ballList))
    frame.set_draw_handler(ball.draw)
    ball.update(True)

timer = simplegui.create_timer(2000, timer_handler)
timer.start()
#start the frame animation
frame.start()


        

from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Wall:
    def __init__(self, border, color):
        self.border = border
        self.color = color
        self.normals = Vector(1,0)
        self.normalt=Vector(0,1)
        self.edge_r = WIDTH - self.border
        self.edge_l=  self.border
        self.edge_f=HEIGHT-self.border
    def draw(self, canvas):
        canvas.draw_line((0, 0),
                         (0, HEIGHT),
                         self.border,
                         self.color)
        canvas.draw_line((WIDTH, 0),
                         (WIDTH, HEIGHT),
                         self.border,
                         self.color)
        canvas.draw_line((0, 0),
                         (WIDTH, 0),
                         self.border,
                         self.color)
        canvas.draw_line((0, HEIGHT),
                         (WIDTH, HEIGHT),
                         self.border,
                         self.color)

    def hit(self, ball):
        h=(ball.offset_l()<=self.edge_r)
        return ((ball.offset_l()<=self.edge_l)or(ball.offset_r()>=WIDTH)or(ball.offset_t()<=self.edge_l)or(ball.offset_f()>=self.edge_f))

class Ball:
    def __init__(self, pos, vel, radius, border, color):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.border = 1
        self.color = color

    def offset_l(self):
        return self.pos.x - self.radius
    def offset_r(self):
        return self.pos.x + self.radius
    def offset_t(self):
        return self.pos.y - self.radius
    def offset_f(self):
        return self.pos.y + self.radius
                 

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border,
                           self.color,
                           self.color)

    def bounce(self, normal):
        self.vel.reflect(normal)

class Interaction:
    def __init__(self, wall, ball):
        self.ball = ball
        self.wall = wall

    def update(self):
        if self.wall.hit(self.ball):
            if self.ball.pos.x>=WIDTH-self.wall.border or self.ball.pos.x<=self.wall.border:
                self.ball.pos=Vector(300,self.ball.pos.y)
            if self.ball.pos.y>=HEIGHT-self.wall.border or self.ball.pos.y<=self.wall.border:
                self.ball.pos=Vector(self.ball.pos.x,200)
            
            if (self.ball.offset_t()<=self.wall.edge_l)or(self.ball.offset_f()>=self.wall.edge_f):
                self.ball.bounce(self.wall.normalt)
            else:
                self.ball.bounce(self.wall.normals)
        self.ball.update()

    def draw(self, canvas):
        self.update()
        self.ball.draw(canvas)
        self.wall.draw(canvas)

# The canvas dimensions
WIDTH = 600
HEIGHT = 400

# Initial position and velocity of the ball
p = Vector(600,200)
v = Vector(1,-1)



# Creating the objects

b = Ball(p, v, 20, 50, 'blue')
w = Wall( 5, 'red')
i = Interaction(w, b)

    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("ball-wall",WIDTH, HEIGHT)
frame.set_draw_handler(i.draw)

# Start the frame animation
frame.start()

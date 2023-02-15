import random
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
    def ballhit(self,b1,b2):
        distance=b1.pos.copy().subtract(b2.pos).length()
        return distance<b1.radius+b2.radius
        #return ((b1.pos.x+b1.radius==b2.pos.x+b2.radius)or(b1.pos.x-b1.radius==b2.pos.x+b2.radius)or(b1.pos.x+b1.radius==b2.pos.x-b2.radius)or(b1.pos.x-b1.radius==b2.pos.x-b2.radius))and ((b1.pos.y+b1.radius==b2.pos.y+b2.radius)or(b1.pos.y-b1.radius==b2.pos.y+b2.radius)or(b1.pos.y+b1.radius==b2.pos.y-b2.radius)or(b1.pos.y-b1.radius==b2.pos.y-b2.radius))
class Interaction:
    def __init__(self, wall, ballset):
        self.ballset = ballset
        self.wall = wall

    def update(self):
        for i in self.ballset:
            if self.wall.hit(i):
                if i.pos.x>=WIDTH-self.wall.border or i.pos.x<=self.wall.border:
                    i.pos=Vector(300,i.pos.y)
                if i.pos.y>=HEIGHT-self.wall.border or i.pos.y<=self.wall.border:
                    i.pos=Vector(i.pos.x,200)           
                if (i.offset_t()<=self.wall.edge_l)or(i.offset_f()>=self.wall.edge_f):
                    i.bounce(self.wall.normalt)
                else:
                    i.bounce(self.wall.normals)
            for j in self.ballset:
                if i!=j:
                    if i.ballhit(i,j):
                        normal = i.pos.copy().subtract(j.pos).normalize()
                        v1_pa=i.vel.get_proj(normal)
                        v1_pe=i.vel.copy().subtract(v1_pa)
                        v2_pa=j.vel.get_proj(normal)
                        v2_pe=j.vel.copy().subtract(v2_pa)
                        i.vel=v2_pa+v1_pe
                        j.vel=v1_pa+v2_pe
                        
                             
            i.update()

    def draw(self, canvas):
        for i in self.ballset:
            self.update()
            i.draw(canvas)
            self.wall.draw(canvas)

# The canvas dimensions
WIDTH = 600
HEIGHT = 400

# Initial position and velocity of the ball
p1 = Vector(random.randint(0,WIDTH),random.randint(0,HEIGHT))
p2 = Vector(random.randint(0,WIDTH),random.randint(0,HEIGHT))
p3 = Vector(random.randint(0,WIDTH),random.randint(0,HEIGHT))
p4 = Vector(random.randint(0,WIDTH),random.randint(0,HEIGHT))
v1 = Vector(random.randint(-1,1),random.randint(-1,1))
v2 = Vector(random.randint(-1,1),random.randint(-1,1))
v3 = Vector(random.randint(-1,1),random.randint(-1,1))
v4 = Vector(random.randint(-1,1),random.randint(-1,1))



# Creating the objects
b1=Ball(p1, v1, 20, 50, 'blue')
b2=Ball(p2, v2, 20, 50, 'Yellow')
b3=Ball(p3, v3, 20, 50, 'Green')
b4=Ball(p4, v4, 20, 50, 'Pink')
ballset={b1,b2,b3,b4}
w = Wall( 5, 'red')
inter = Interaction(w, ballset)

    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("ball-wall",WIDTH, HEIGHT)
frame.set_draw_handler(inter.draw)

# Start the frame animation
frame.start()

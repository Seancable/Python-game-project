from vectorClass import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

class Wall:
    def __init__(self, border, color):
        self.border = border
        self.color = color
        self.normals = Vector(1,0)
        self.normalt=Vector(0,1)
        self.edge_r = CANVAS_WIDTH - self.border
        self.edge_l=  self.border
        self.edge_f= CANVAS_HEIGHT-self.border
    def draw(self, canvas):
        canvas.draw_line((0, 0),
                         (0, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)
        canvas.draw_line((CANVAS_WIDTH, 0),
                         (CANVAS_WIDTH, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)
        canvas.draw_line((0, 0),
                         (CANVAS_WIDTH, 0),
                         self.border*2+1,
                         self.color)
        canvas.draw_line((0, CANVAS_HEIGHT),
                         (CANVAS_WIDTH, CANVAS_HEIGHT),
                         self.border*2+1,
                         self.color)

    def hit(self, ball):
        h=(ball.offset_l()<=self.edge_r)
        return ((ball.offset_l()<=self.edge_l)or(ball.offset_r()>=CANVAS_WIDTH)or(ball.offset_t()<=self.edge_l)or(ball.offset_f()>=self.edge_f))

class Ball:
    def __init__(self, pos, vel, radius, color):
        self.pos = pos
        self.vel = vel
        self.radius = radius
        self.border = 1
        self.color = color

    def draw(self, canvas):
        #draws each of the circle objects
        canvas.draw_circle(self.pos.get_p(),
                self.radius ,
                self.border,
                self.color,
                self.color)

    def offset_l(self):
        return self.pos.x - self.radius
    def offset_r(self):
        return self.pos.x + self.radius
    def offset_t(self):
        return self.pos.y - self.radius
    def offset_f(self):
        return self.pos.y + self.radius

    def update(self):
        #changes the location of circles
        self.pos.add(self.vel)
    
    def bounce(self, normal):
        #changes the velocity when circles collide
        self.vel.reflect(normal)
        
class Domain:
    #the circles that the circle collides with
    def __init__(self, pos, rad, border, color, border_col):
        self.pos = pos
        self.radius = rad
        self.border = border
        self.color = color
        self.border_color = border_col
        self.edge = self.radius - self.border

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),
                           self.radius,
                           self.border*2+1,
                           self.border_color,
                           self.color)

    def hit(self, ball):
        distance = self.pos.copy().subtract(ball.pos).length()
        return distance - ball.radius <= self.edge

    def normal(self, ball):
        perpendicular = self.pos.copy().subtract(ball.pos)
        return perpendicular.normalize()

class Interaction:
    def __init__(self, domain, ball, wall):
        self.ball = ball
        self.wall = wall
        self.domain = domain
        self.in_collision = False
        
    def draw(self, canvas):
        self.update()
        for domains in self.domain:
            domains.draw(canvas)
        self.ball.draw(canvas)
        self.wall.draw(canvas)

    def update(self):
        self.ball.update()
        for domains in self.domain:
            if domains.hit(self.ball):
                if not self.in_collision:
                    normal = domains.normal(self.ball)
                    self.ball.bounce(normal)
                    self.in_collision = True
            else:
                self.in_collision = False
        if self.wall.hit(self.ball):
            if (self.ball.offset_t()<=self.wall.edge_l)or(self.ball.offset_f()>=self.wall.edge_f):
                self.ball.bounce(self.wall.normalt)
            else:
                self.ball.bounce(self.wall.normals)

ball = Ball(Vector(400, 300),
            Vector(-4, 1),
            10,
            "blue")
w = Wall( 5, 'red')
domain = Domain(Vector(100, 100),
                50,
                5,
                "black",
                "red")
domain2 = Domain(Vector(400, 100),
                50,
                5,
                "black",
                "red")
domain3 = Domain(Vector(100, 400),
                50,
                5,
                "black",
                "red")
domain4 = Domain(Vector(400, 400),
                50,
                5,
                "black",
                "red")
interaction = Interaction([domain, domain2, domain3, domain4], ball, w)

frame = simplegui.create_frame("Domain", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(interaction.draw)

frame.start()
frame.start()

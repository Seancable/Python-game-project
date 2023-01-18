# Python-game-project
Python game project repository

--------------------------------------------
point.py
import simplegui

# Constants are written in capital letters
WIDTH = 700
HEIGHT = 500

# Handler to draw on canvas :
# this function is called 60 times per second
def draw(canvas):
    canvas.draw_point ([WIDTH /2, HEIGHT /2] , 'Yellow')
    canvas.draw_point ([WIDTH , HEIGHT ] , 'Yellow')
    canvas.draw_point ([WIDTH , 0] , 'Yellow')
    canvas.draw_point ([0, HEIGHT ] , 'Yellow')
    canvas.draw_point ([0, 0] , 'Yellow')


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Points", WIDTH , HEIGHT )
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
-------------------------------------------------------------------------------
line.py
import simplegui

WIDTH = 500
HEIGHT = 300
global position
position=0

def draw_handler(canvas):
    global position
    canvas.draw_line((0, 0), (0, HEIGHT), 12, 'Red')
    canvas.draw_line([WIDTH, 0], [WIDTH, HEIGHT], 20, 'Blue')
    canvas.draw_line([position, HEIGHT/4], [position, HEIGHT/2+HEIGHT/4], 1, 'YELLOW')
    position += 1
    if position==WIDTH:
        position=0

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.start()

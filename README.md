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

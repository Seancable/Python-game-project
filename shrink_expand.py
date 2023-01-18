import random
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Constants are written in capital letters
WIDTH = 600
HEIGHT = 400
size = 50
flipper = 1


# Handler to draw on canvas :
# this function is called 60 times per second
def draw(canvas):
    global size, flipper
    canvas.draw_circle([WIDTH /2, HEIGHT /2], size, 20 , "yellow")
    if 51 > size > 1:
        size -= flipper
    else:
        size += flipper
        flipper *= -1
    

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Points", WIDTH , HEIGHT )
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

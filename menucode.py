# Add after call to Main:

def draw(canvas):
    main.runGame(canvas, WIDTH, HEIGHT)


def pause(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.pausemenu(canvas)

def start(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.mainmenu(canvas)

def click(pos):
    global frame
    # Start Game
    print(pos)
    x = pos[0]
    y = pos[1]

    if (195 < x < 555) and (197 < y < 240):
        print("Start Game")
        frame.set_draw_handler(draw)
        frame.set_keydown_handler(kbd.keyDown)
        frame.set_keyup_handler(kbd.keyUp)
    if (195 < x < 555) and (355 < y < 385):
        print("Settings")
        quit()
    if (245 < x < 505) and (415 < y < 440):
        print("Quit")
        quit()
    if (705 < x < 745) and (8 < y < 45):
        print("Pause")
        frame.set_draw_handler(pause)

frame = simplegui.create_frame(' The War of The Worlds ', WIDTH, HEIGHT)
frame.set_draw_handler(start)
frame.set_mouseclick_handler(click)
frame.start()

import random
from menuCont import MenuCont

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Menu:

    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT

    def mainmenu(self, canvas):
        # Main menu background
        canvas.draw_polygon([[self.width/2 - 300, self.height/2 - 250], [self.width/2 + 300, self.height/2 - 250],
        [self.width/2 + 300, self.height/2 +  250], [self.width/2 - 300, self.height/2 + 250]], 12, 'Black', 'ForestGreen')
        # New Game button
        canvas.draw_polygon([[self.width/4, self.height/4], [3/4*(self.width), self.height/4],
                             [3/4*(self.width), self.height/4 + 60], [self.width/4, self.height/4 + 60]], 12, 'Grey', 'Silver')
        canvas.draw_text('Start Game', [self.width/4 + 80, self.height/4 + 45], 45, 'Red')

        # Settings Button
        canvas.draw_polygon([[self.width/4, self.height/4 + 160], [3/4*(self.width), self.height/4 + 160],
                             [3/4*(self.width), self.height/4 + 200], [self.width/4, self.height/4 + 200]], 12, 'Grey', 'Silver')
        canvas.draw_text('Settings', [self.width/4 + 140, self.height/4 + 190], 30, 'Red')

        # Quit Button
        canvas.draw_polygon([[self.width/4 + 50, self.height/4 + 260], [3/4*(self.width) - 50, self.height/4 + 260],
                             [3/4*(self.width) - 50, self.height/4 + 220], [self.width/4 + 50, self.height/4 + 220]], 12, 'Grey', 'Silver')
        canvas.draw_text('Quit', [self.width/4 + 166, self.height/4 + 250], 25, 'Red')
        # Save Game button ** if time allows **
        #canvas.draw_polygon([[self.width/4, self.height/4 + 80], [3/4*(self.width), self.height/4 + 80],
                             #[3/4*(self.width), self.height/4 + 140], [self.width/4, self.height/4 + 140]], 12, 'Silver', 'Silver')
        #canvas.draw_text('Start Game', [self.width/4 + 30, self.height/4 + 45], 45, 'Red')

        menChoice = "start"

        return menChoice

    def pausemenu(self, canvas):
        canvas.draw_polygon([[self.width/2 - 300, self.height/2 - 250], [self.width/2 + 300, self.height/2 - 250],
        [self.width/2 + 300, self.height/2 +  250], [self.width/2 - 300, self.height/2 + 250]], 12, 'Black', 'ForestGreen')
        # New Game button
        canvas.draw_polygon([[self.width/4, self.height/4], [3/4*(self.width), self.height/4],
                             [3/4*(self.width), self.height/4 + 60], [self.width/4, self.height/4 + 60]], 12, 'Grey', 'Silver')
        canvas.draw_text('Resume', [self.width/4 + 80, self.height/4 + 45], 45, 'Red')

        # Settings Button
        canvas.draw_polygon([[self.width/4, self.height/4 + 160], [3/4*(self.width), self.height/4 + 160],
                             [3/4*(self.width), self.height/4 + 200], [self.width/4, self.height/4 + 200]], 12, 'Grey', 'Silver')
        canvas.draw_text('Controls', [self.width/4 + 140, self.height/4 + 190], 30, 'Red')

        # Quit Button
        canvas.draw_polygon([[self.width/4 + 50, self.height/4 + 260], [3/4*(self.width) - 50, self.height/4 + 260],
                             [3/4*(self.width) - 50, self.height/4 + 220], [self.width/4 + 50, self.height/4 + 220]], 12, 'Grey', 'Silver')
        canvas.draw_text('Quit', [self.width/4 + 166, self.height/4 + 250], 25, 'Red')

    def contmenu(self, canvas):
        canvas.draw_polygon([[self.width/2 - 300, self.height/2 - 250], [self.width/2 + 300, self.height/2 - 250],
        [self.width/2 + 300, self.height/2 +  250], [self.width/2 - 300, self.height/2 + 250]], 12, 'Black', 'ForestGreen')
        # Continue button
        canvas.draw_polygon([[self.width/4, self.height/4 + 50], [3/4*(self.width), self.height/4 + 50],
                             [3/4*(self.width), self.height/4 + 110], [self.width/4, self.height/4 + 110]], 12, 'Grey', 'Silver')
        canvas.draw_text('Continue', [self.width/4 + 80, self.height/4 + 95], 45, 'Red')
        # Quit Button
        canvas.draw_polygon([[self.width/4 + 50, self.height/4 + 260], [3/4*(self.width) - 50, self.height/4 + 260],
                             [3/4*(self.width) - 50, self.height/4 + 220], [self.width/4 + 50, self.height/4 + 220]], 12, 'Grey', 'Silver')
        canvas.draw_text('Quit', [self.width/4 + 166, self.height/4 + 250], 25, 'Red')
        
     def controlsMenu(self, canvas):
        pass

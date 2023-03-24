WALL_IMG = ("https://raw.githubusercontent.com/Seancable/Python-game-project/main/wall.png")
class Obstacle:
    def __init__(self, x, y, endX, endY, thickness, colour):
        self.x = x
        self.y = y
        self.start = (self.x, self.y)
        self.endX = endX
        self.endY = endY
        self.end = (self.endX, self.endY)
        self.thickness = thickness
        self.colour = colour
        self.center = ((self.start[0] + self.end[0])/2, (self.start[1] + self.end[1])/2)
        self.widthHeight = (self.endX - self.x, self.endY - self.y)
        self.centerDest = (254/2, 243/2)

    def draw(self, canvas):
        #canvas.draw_image(self.image, self.center, self.widthHeight, self.centerDest, self.dest)
        #canvas.draw_image(WALL_IMG, self.center, self.widthHeight, self.centerDest, self.start)
        canvas.draw_line(self.start, (self.endX, self.endY), self.thickness, self.colour)
        
        canvas.draw_polygon([[700, 50], [750, 50],
                             [750, 0], [700, 0]], 12, 'Grey', 'Silver')
        canvas.draw_text('||', [720, 40], 40, 'SlateGray')
        
    def getStartX(self):
        return self.x

    def getEndX(self):
        return self.endX

    def getY(self):
        return self.y

    def collisions(self, character):
        #detects collisions between obstacles and character
        #could also be used for enemy if needed
        if self.x < character.pos.get_p()[0] < self.endX:
            if round(character.pos.get_p()[1]) + self.thickness/2 + 25< self.y < round(character.pos.get_p()[1]) + self.thickness/2 + 40:
                return True
        return False

    def sideCollisionsRight(self, character):
        #checks to see if the character collides with the side of an obstacle
        #returning true if they do
        #used self.thickness as a boundary on either side, self.thickness/2
        #wasnt a big enough boundary
        if self.x - 25 < character.pos.get_p()[0] - 10 < self.x:
            if round(character.pos.get_p()[1]) - self.thickness/1.2 < self.y < round(character.pos.get_p()[1]) + self.thickness/1.2:
                return True
        return False

    def sideCollisionsLeft(self, character):
        #checks to see if the character collides with the side of an obstacle
        #returning true if they do
        #used self.thickness as a boundary on either side, self.thickness/2
        #wasnt a big enough boundary
        if self.endX < character.pos.get_p()[0] < self.endX + 25:
            print(10)
            if round(character.pos.get_p()[1]) - self.thickness/1.2 < self.y < round(character.pos.get_p()[1]) + self.thickness/1.2:
                return True
        return False


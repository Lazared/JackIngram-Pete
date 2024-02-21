import random

class Player:
    def __init__(self, x, y, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas

    def draw(self):
        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill=self.color)

    def move_randomly(self):
        self.x += random.uniform(-5, 5)
        self.y += random.uniform(-5, 5)

        # Keep the players within the boundaries of the field
        if self.x - 10 < 0:
            self.x = 10
        elif self.x + 10 > 800:
            self.x = 800 - 10

        if self.y - 10 < 0:
            self.y = 10
        elif self.y + 10 > 400:
            self.y = 400 - 10

        self.draw()
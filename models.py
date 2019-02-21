class Player:
    GRAVITY = 1
    STARTING_VELOCITY = 15

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

        self.vy = Player.STARTING_VELOCITY

    def update(self, delta):
        self.y += self.vy
        self.vy -= 1
        self.vy -= Player.GRAVITY

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.player = Player(self, width // 2, height // 2)

        self.vy = 15
 
    def update(self, delta):
        self.player.update(delta)
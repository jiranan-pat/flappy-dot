import arcade
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
class FlappyDotWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE)
 
    def on_draw(self):
        arcade.start_render()
 
 
def main():
    window = FlappyDotWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
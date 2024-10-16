from objekts import Frogger
from turtle import Screen

class Steuerung:
    def __init__(self, screen : Screen):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.direction = "s"
        
        screen.listen()

        
    def controller(self, screen):
        screen.onkeypress(self.up_player, "Up")
        screen.onkeyrelease(self.release_up_player, "Up")

        screen.onkeypress(self.down_player, "Down")
        screen.onkeyrelease(self.release_down_player, "Down")

        screen.onkeypress(self.left_player, "Left")
        screen.onkeyrelease(self.release_left_player, "Left")

        screen.onkeypress(self.right_player, "Right")
        screen.onkeyrelease(self.release_right_player, "Right")
        
    def up_player(self):
        self.up = True

    def release_up_player(self):
        self.up = False
    
    def down_player(self):
        self.down = True
        
    def release_down_player(self):
        self.down = False
        
    def left_player(self):
        self.left = True
        
    def release_left_player(self):
        self.left = False
        
    def right_player(self):
        self.right = True
        
    def release_right_player(self):
        self.right = False
    
    def movement(self, frog, player):    
        if self.up:
            self.direction = "n"
            y = player.ycor()
            player.goto(player.xcor(),y+40)
            
            
        if self.down:
            self.direction = "s"
            y = player.ycor()
            player.goto(player.xcor(),y-40)
            
        if self.left:
            self.direction = "w"
            x = player.xcor()
            player.goto(x-40,player.ycor())
            
        if self.right:
            self.direction = "o"
            x = player.xcor()
            player.goto(x+40,player.ycor())
            
        frog.erstelle_bild(self.direction)
    class Movement():
        def __init__(self):
            pass
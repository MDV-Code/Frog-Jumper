from objekts import Frogger
from turtle import Screen

class Steuerung:
    def __init__(self, screen : Screen):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
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
    
    def movement(self, player):    
        if self.up:
            y = player.ycor()
            player.goto(player.xcor(),y+20)
            
        if self.down:
            y = player.ycor()
            player.goto(player.xcor(),y-20)
            
        if self.left:
            x = player.xcor()
            player.goto(x-20,player.ycor())
            
        if self.right:
            x = player.xcor()
            player.goto(x+20,player.ycor())
    
    class Movement():
        def __init__(self):
            pass
from objekts import Frogger
from turtle import Screen
from time import sleep


class Steuerung:
    def __init__(self, screen : Screen):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.direction = "s"
        self.jump = "x"
        self.screen = screen        
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
        self.jump = "n"

    def release_up_player(self):
        self.up = False
        self.jump = "x"
    
    def down_player(self):
        self.down = True
        self.jump = "s"
        
    def release_down_player(self):
        self.down = False
        self.jump = "x"
        
    def left_player(self):
        self.left = True
        self.jump = "w"
        
    def release_left_player(self):
        self.left = False
        self.jump = "x"
        
    def right_player(self):
        self.right = True
        self.jump = "o"
        
    def release_right_player(self):
        self.right = False
        self.jump = "x"
        
    def movement(self, frog, player):    
        if self.up:
            self.direction = "n"
            y = player.ycor()
            player.goto(player.xcor(),y+40)
            
            
        elif self.down:
            self.direction = "s"
            y = player.ycor()
            player.goto(player.xcor(),y-40)
            
        elif self.left:
            self.direction = "w"
            x = player.xcor()
            player.goto(x-40,player.ycor())
            
        elif self.right:
            self.direction = "o"
            for i in range(1,20):
                x = player.xcor()
                player.goto(x+2,player.ycor())
                sleep(0.008)
                player.shape(f"./sprites/rechts_sprung/r{i}.gif")
                self.screen.update()
            
        
            # player.goto(x+40,player.ycor())
            
        frog.erstelle_bild(self.direction, self.jump)
    class Movement():
        def __init__(self):
            pass
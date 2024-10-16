from turtle import Turtle, Screen

class Frogger(Turtle):
    def __init__(self, screen : Screen) -> None:
        self.frogger()
        self.bild
        self.froglist = 1

        for bild in range(1, 49):
            screen.register_shape(f"./sprites/front/f{bild}.gif")
            
        for bild in range(1, 16):
            screen.register_shape(f"./sprites/links_sprung/l{bild}.gif")
        for bild in range(1, 9):
            screen.register_shape(f"./sprites/rechts_sprung/r{bild}.gif")
            
        for bild in range(1, 10):
            screen.register_shape(f"./sprites/links_stehen/{bild}l.gif")
        for bild in range(1, 9):
            screen.register_shape(f"./sprites/rechts_stehen/{bild}r.gif")
        for bild in range(1, 8):
            screen.register_shape(f"./sprites/oben_sprung/t{bild}.gif")            
        for bild in range(1, 2):
            screen.register_shape(f"./sprites/tot/dead{bild}.gif")
        screen.register_shape(f"./sprites/oben_stehen/1t.gif")

            
                   

    def erstelle_bild(self, direction):
        
        if direction == "s":
            if self.froglist == 49:
                self.froglist = 1
            self.bild.shape(f"./sprites/front/f{self.froglist}.gif")
            self.froglist += 1
        
        elif direction == "n":
            if self.froglist >= 1:
                self.froglist = 1
            self.bild.shape(f"./sprites/oben_stehen/{self.froglist}t.gif")
            self.froglist += 1

        elif direction == "o":
            if self.froglist > 8:
                self.froglist = 1
            self.bild.shape(f"./sprites/rechts_stehen/{self.froglist}r.gif")
            self.froglist += 1
            
        elif direction == "w":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/links_stehen/{self.froglist}l.gif")
            self.froglist += 1
      

    def frogger(self):
        bild = Turtle()
        bild.penup()
        bild.goto(0,320)
        self.bild = bild






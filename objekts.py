from turtle import Turtle, TurtleScreen

class Frogger(Turtle):
    def __init__(self, screen : TurtleScreen):
        self.frogger()
        self.bild
        self.froglist = 1

       
        for bild in range(1, 11):
            screen.register_shape(f"./sprites/oben_stehen/{bild}f.gif")
            screen.register_shape(f"./sprites/unten_stehen/f{bild}.gif")
            screen.register_shape(f"./sprites/links_stehen/{bild}l.gif")
            screen.register_shape(f"./sprites/rechts_stehen/{bild}r.gif")

            screen.register_shape(f"./sprites/links_sprung/l{bild}.gif")
            screen.register_shape(f"./sprites/rechts_sprung/r{bild}.gif")
            screen.register_shape(f"./sprites/oben_sprung/t{bild}.gif")            
            screen.register_shape(f"./sprites/unten_sprung/{bild}t.gif")
            
        for bild in range(1,2):       
            screen.register_shape(f"./sprites/tot/dead{bild}.gif")

    def erstelle_bild(self, direction, jump):
        
        if direction == "s":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/unten_stehen/f{self.froglist}.gif")
            self.froglist += 1
        
        elif direction == "n":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/oben_stehen/{self.froglist}f.gif")
            self.froglist += 1

        elif direction == "o":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/rechts_stehen/{self.froglist}r.gif")
            self.froglist += 1
            
        elif direction == "w":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/links_stehen/{self.froglist}l.gif")
            self.froglist += 1
            ################################################## JUMP
        if jump == "s":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/unten_stehen/f{self.froglist}.gif")
            self.froglist += 1
        
        elif jump == "n":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/oben_stehen/{self.froglist}f.gif")
            self.froglist += 1

        elif jump == "o":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/rechts_stehen/{self.froglist}r.gif")
            self.froglist += 1
            
        elif jump == "w":
            if self.froglist >= 10:
                self.froglist = 1
            self.bild.shape(f"./sprites/links_stehen/{self.froglist}l.gif")
            self.froglist += 1
      

    def frogger(self):
        bild = Turtle()
        bild.penup()
        bild.goto(20,320)
        self.bild = bild






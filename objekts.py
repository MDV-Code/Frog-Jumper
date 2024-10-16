from turtle import Turtle
#########Hier 

class Frogger(Turtle):
    def __init__(self, screen):
        self.frogger()
        self.frog
        self.froglist = 0
        for bild in range(0, 49):
            print(f"./sprites/front/f{bild}.gif")
            screen.register_shape(f"./sprites/front/f{bild}.gif")
        for bild in range(0, 16):
            screen.register_shape(f"./sprites/links_sprung/l{bild}.gif")
        for bild in range(1, 10):
            screen.register_shape(f"./sprites/rechts_sprung/r{bild}.gif")
        for bild in range(1, 10):
            screen.register_shape(f"./sprites/links_stehen/{bild}l.gif")
        for bild in range(1, 9):
            screen.register_shape(f"./sprites/rechts_stehen/{bild}r.gif")
        for bild in range(1, 1):
            screen.register_shape(f"./sprites/oben_stehen/{bild}t.gif")
        for bild in range(1, 8):
            screen.register_shape(f"./sprites/oben_sprung/t{bild}.gif")            
        for bild in range(1, 2):
            screen.register_shape(f"./sprites/tot/dead{bild}.gif")            

    def erstelle_bild(self,last_movement):
        if last_movement == "s":
            if self.froglist == 49:
                #print("here")
                self.froglist = 0
            self.frog.shape(f"./sprites/front/f{self.froglist}.gif")
            self.froglist += 1
        
        elif last_movement == "n":
            if self.froglist >= 1:
                self.froglist = 1
            self.frog.shape(f"./sprites/oben_stehen/{self.froglist}t.gif")
            self.froglist += 1

        elif last_movement == "o":
            if self.froglist >= 9:
                self.froglist = 1
            self.frog.shape(f"./sprites/rechts_stehen/f{self.froglist}r.gif")
            self.froglist += 1
            
        else: 
            if self.froglist >= 10:
                self.froglist = 1
            self.frog.shape(f"./sprites/links_stehen/f{self.froglist}l.gif")
            self.froglist += 1


    def links_sprung(self):
        shapelist = 1
        if shapelist == 34:
            shapelist = 0
        self.frog.shape(f"./sprites/links_sprung/{shapelist}.gif")

    def frogger(self):
        frog = Turtle()
        frog.penup()
        frog.goto(0,320)
        self.frog = frog






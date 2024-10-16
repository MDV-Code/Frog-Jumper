from turtle import Turtle

class Frogger(Turtle):
    def __init__(self, screen):
        self.frogger()
        self.frog
        self.froglist = 0
        for bild in range(0, 49):
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
        
        if self.froglist == 49:
            self.froglist = 0
        self.frog.shape(f"./sprites/front/f{self.froglist}.gif")
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






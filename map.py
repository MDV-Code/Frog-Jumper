from turtle import Turtle, TurtleScreen
from random import randint

class Map(Turtle):
    def __init__(self, screen : TurtleScreen):
        screen.register_shape("./sprites/textures/gras1.gif")
        screen.register_shape("./sprites/textures/gras2.gif")
        screen.register_shape("./sprites/textures/gras3.gif")
        screen.register_shape("./sprites/textures/gras4.gif")
        screen.register_shape("./sprites/textures/sand.gif")
        screen.register_shape("./sprites/textures/street.gif")
        self.map_coordinates = []
        self.map_segments = []
        self.map_positions()
        
    def map_positions(self):
        for i in range(-460, 480, 40):
            x = i
            for j in range(360, -400, -40):
                y = j
                r = randint(1,3)
                self.map_coordinates.append((x,y,r))
        print(self.map_coordinates)
        self.generate_map()
        
    def generate_map(self):
        for position in self.map_coordinates:
            map_segment = Turtle()
            if position[1] >= 280:
                if position[2] == 1:
                    map_segment.shape(f"./sprites/textures/gras{randint(1,4)}.gif")
                elif position[2] >= 2:
                    map_segment.shape("./sprites/textures/sand.gif")
            if position[1] < 280 and position[1] >= 140 or position[1] < 60 and position[1] >= -100 or position[1] < -180 and position[1] >= -300:
                map_segment.shape("./sprites/textures/street.gif")
            elif position[2] == 1:
                map_segment.shape(f"./sprites/textures/gras{randint(1,4)}.gif")
            elif position[2] >= 2:
                map_segment.shape("./sprites/textures/sand.gif")
                
            map_segment.penup()
            map_segment.shapesize(2)
            map_segment.goto(position[0], position[1])
            


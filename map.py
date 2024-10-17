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
        screen.register_shape("./sprites/textures/street1.gif")
        screen.register_shape("./sprites/textures/street2.gif")
        screen.register_shape("./sprites/textures/street3.gif")
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
            #################################################^^^^^START^^^^
            
            ############FAHRBAHNLINIEN ERMITTELN
            if (
                position[1] < 240 and position[1] >= 160 or
                position[1] < 40 and position[1] >= 0 or
                position[1] < -40 and position[1] >= -80 or
                position[1] < -240 and position[1] >= -280
                ):
                ###### FAHRBAHNLINIEN FÜLLEN
                for pos in range(-460, 480, 80):
                    if position[0] == pos:
                        map_segment.shape("./sprites/textures/street1.gif")
                ###### ZWISCHEN DEN FAHRBAHNLINIEN FÜLLEN
                for pos in range(-420, 480, 80):
                    if position[0] == pos:
                        map_segment.shape("./sprites/textures/street.gif")
            ######## NUR FAHRBAHN FÜLLEN (ZWEITE GROßE STRAßE MITTE)
            elif position[1] < 0 and position[1] >= -40:
                map_segment.shape("./sprites/textures/street.gif")

            ##############BOARDSTEINKANTEN        
            if (
                position[1] < 280 and position[1] >= 240 or
                position[1] < 80 and position[1] >= 40 or
                position[1] < -200 and position[1] >= -240
                ):
                map_segment.shape("./sprites/textures/street2.gif")
            elif(
                position[1] < 200 and position[1] >= 160 or
                position[1] < -80 and position[1] >= -120 or
                position[1] < -280 and position[1] >= -320
                ):
                map_segment.shape("./sprites/textures/street3.gif")
            ################### RESTLICHEN FLÄCHEN ZUFÄLLIG GENERIEREN         
            elif(
                position[1] < 160 and position[1] >= 80 or
                position[1] < -120 and position[1] >= -200 or
                position[1] < -320 and position[1] >= -360
                ):
                if position[2] == 1:
                    map_segment.shape(f"./sprites/textures/gras{randint(1,4)}.gif")
                elif position[2] >= 2:
                    map_segment.shape("./sprites/textures/sand.gif")
            
                
            map_segment.penup()
            map_segment.shapesize(2)
            map_segment.goto(position[0], position[1])
            


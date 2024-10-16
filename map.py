from turtle import Turtle, Screen

class Map(Turtle):
    def __init__(self):
        self.map_coordinates = []
        self.map_positions()
    
    def map_positions(self):
        for i in range(-460, 460, 40):
            x = i
            for j in range(360, 240, -40):
                y = j
                self.map_coordinates.append((x,y))
        print(self.map_coordinates)
        self.generate_map()
        
    def generate_map(self):
        for position in self.map_coordinates:
            map_segment = Turtle()
            map_segment.penup()
            map_segment.shape("square")
            map_segment.color("red")
            map_segment.shapesize(2)
            map_segment.goto(position)


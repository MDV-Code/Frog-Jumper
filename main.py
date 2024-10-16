from turtle import Screen
from objekts import Frogger
from steuerung import Steuerung
from map import Map
import time
screen = Screen()
screen.tracer(0)
screen.bgcolor("white")

frog = Frogger(screen)
steuerung = Steuerung(screen)
steuerung.controller(screen)

screen.update()
game_is_on = True
last_movement =["n","s","e","w"]  #Nord,Süd, Ost, West 
screen.update()
while game_is_on:
    screen.update()
    frog.erstelle_bild()
    steuerung.movement(frog.frog)
                                    #print("schleife ist an")
    time.sleep(0.15)

screen.exitonclick()


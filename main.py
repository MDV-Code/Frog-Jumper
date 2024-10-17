from turtle import Screen
from objekts import Frogger
from steuerung import Steuerung
from map import Map
import time
screen = Screen()
screen.setup (width=960, height=775)
screen.title("Frog Jumper")
screen.tracer(0)
screen.bgcolor("white")


frog = Frogger(screen)
steuerung = Steuerung(screen)
steuerung.controller(screen)
map = Map(screen)
screen.update()
game_is_on = True
screen.update()
while game_is_on:
    screen.update()
    
    steuerung.movement(frog, frog.bild)
                                  
    time.sleep(0.15)

screen.exitonclick()



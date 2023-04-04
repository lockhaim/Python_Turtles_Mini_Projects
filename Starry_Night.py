from turtle import *
from random import *

# START
# Set the background color to BLACK
# Repeat 100 times
#     Generate random star position
#     Generate random star size
#     Draw the star
# END

bgcolor("black")
hideturtle() #hide the turtle so as not to obstruct our 'stars'

def draw_star(xpos, ypos): #star generation
    size = randrange(2,9)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

draw_star(0, 0) #test stars
draw_star(24, 15)
draw_star(-50, 100)
draw_star(100, 52)

done()
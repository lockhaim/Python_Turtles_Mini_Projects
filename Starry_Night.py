from turtle import *


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
    penup()
    goto(xpos, ypos)
    pendown()
    dot(20, "white")

draw_star(0, 0) #test star

done()
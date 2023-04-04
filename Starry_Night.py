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

width = window_width()
height = window_height()

speed(0)

def draw_star(xpos, ypos): #star generation
    size = randrange(3,12)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

# draw_star(0, 0) #test stars
# draw_star(24, 15)
# draw_star(-50, 100)
# draw_star(100, 52)


for x in range(125):     # (0,0) is the center of the screen so all stars currently in NE quadrant if the range doesnt start at negative
    xpos = randrange(round(-width/2), round(width/2)) #uses a full screen size in window if not /2
    ypos = randrange(round(-height/2), round(height/2)) #dividing width and height by 2 will give us all dots in the default window size
    draw_star(xpos, ypos) #used the 'round' function so that when the width or height calculation gave a floating point decimal the final number would be a whole integer instead

done()
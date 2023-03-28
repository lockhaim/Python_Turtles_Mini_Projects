from turtle import *

## OBJECTIVES ##
#detect inputs
#require multiple inputs to pop balloon
#utilize variable conditions and functions

## PSEUDOCODE ##
## Draw Balloon
## Up Key Pressed
## Is the balloon at max size?
##  --If No
##  ----Increase balloon size
##  ----then go to draw step
##  --If Yes
##  ----Clear Balloon
##  ----Display "POP!"

diam = 40
pop_diam = 100

def draw_balloon():
    color("red")
    dot(diam)

draw_balloon()
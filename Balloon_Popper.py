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
 
def draw_ball():  # draw balloon fcn
    color("red")
    dot(diam)

def inf_ball():  # inflate balloon 
    global diam
    diam +=10
    draw_ball()

    if diam >= pop_diam:  #conditional for when to pop
        clear()
        diam = 40
        write("POP!")

draw_ball() #actually calling fcn 

onkey(inf_ball, "Up") #when the user presses the up key increase size
listen() #listen for inputs

done() #stops execution of code
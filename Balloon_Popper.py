from turtle import *

## OBJECTIVES ##

# detect inputs
# require multiple inputs to pop balloon
# utilize variable conditions and functions



# WE CAN TO GO FURTHER

# Create a 5x5 grid of ballons
# Allow user to click on balloon to inflate its size.
# Assign each balloon a random size to pop between 50-100.



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
#turtle graphics game
import turtle
import math#(when both object snake and their food touches each other then their distance is very small )
import random
color_choice=["grey","red","yellow","lime","blue","powder blue","brown","orange"]
#launch turtle window
wn= turtle.Screen()
wn.bgcolor("black")
#draw border
#first define new turtle
mypen=turtle.Turtle()
mypen.penup()

mypen.setposition(-350,-350)
mypen.hideturtle()
mypen.color("lime")
mypen.down()
mypen.pensize(3)
for side in range (4):
        mypen.forward(700)
        mypen.left(90)
mypen.hideturtle()
#we create player in turtle:
player=turtle.Turtle()
player.color("white")
player.shape("turtle")
player.pensize(100)
player.penup()#it can't show the tail of turtle

player.speed(0)
#create some achivements
x=4
achiv=[]
for count in range (x):
        achiv.append(turtle.Turtle())
        achiv[count].color(random.choice(color_choice))
        achiv[count].shape("circle")
        achiv[count].penup()
        achiv[count].setposition(random.randint(-200,200),random.randint(-150,230))
speed=1 #it just like the var that in the loop continues the turtle
#keyboard binding

def left():
        player.left(90)

def right():
        player.right(90)
def pause ():
        global speed
        speed-=speed
def resume():
        global speed
        speed=2
#making function which increase the speed of player
def increaseSpeed():
        global speed
        speed+=0.1
        if speed==2:
                speed-=0.2
def decreaseSpeed():
        global speed
        speed-=0.1
        if speed==2:
                speed+=0.2
wn.onkey(resume, "a")
wn.onkey(pause, "space")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.onkey(increaseSpeed,"Up")
wn.onkey(decreaseSpeed,"Down")
wn.listen()
while True:#(it continues the turtle whenever this loop true)
    player.forward(speed)
    #bowndary checking
    if player.xcor()> 330 or player.xcor() < -330:
            player.right(90)
    if player.ycor()> 330 or player.ycor() < -330:
            player.right(90)
    #collision checking
    
    
    for count in range (x):
        if achiv[count].xcor()> 300 or achiv[count].xcor() < -300:
                    achiv[count].right(random.randint(0,360))
        if achiv[count].ycor()> 300 or achiv[count].ycor() < -300:
                    achiv[count].right(random.randint(0,360))
        d = math.sqrt(math.pow(player.xcor()-achiv[count].xcor(),2)+math.pow(player.ycor()-achiv[count].ycor(),2))
        if d<15:
                #achiv.hideturtle()
                achiv[count].color(random.choice(color_choice))
                achiv[count].setposition(random.randint(-310,310),random.randint(-310,310))
                speed+=0.01
   #move goal
        achiv[count].forward(1)
            
'''basically player and echiv are two turtles we find the distance b/w them if distance is very b/w them then achiv will dissapear or move it to a random position'''

   

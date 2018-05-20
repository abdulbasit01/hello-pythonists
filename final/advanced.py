#turtle graphics game
import turtle
import math#(when both object snake and their food touches each other then their distance is very small )
import random
color_choice=["grey","red","yellow","black","blue","powder blue","green","orange"]
#launch turtle window
wn= turtle.Screen()
wn.bgcolor("brown")
wn.title("loading..................")
#draw border
score=0
st=turtle.Turtle()
st.penup()
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
player.color("grey")
player.shape("turtle")
player.pensize(100)
player.penup()#it can't show the tail of turtle

player.speed(0)
#create some achivements
achiv=turtle.Turtle()
achiv.color(random.choice(color_choice))
achiv.shape("circle")
achiv.penup()
achiv.setposition(random.randint(-200,200),random.randint(-150,230))

wn.title("game started")
speed=1 #it just like the var that in the loop continues the turtle
#keyboard binding

def left():
        player.left(45)

def right():
        player.right(45)
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
def exc():
        wn.exit()
wn.onkey(exc, "a")
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
            #player.right(90)
            player.hideturtle()
            achiv.hideturtle()
            mypen.penup()
            wn.bgcolor("green")
            new_turtle=turtle.Turtle()
            new_turtle.write("game over",align="center", font=("classic", 100, "bold"))
            new_turtle.hideturtle()
            wn.title("you strite the boundary")
    if player.ycor()> 330 or player.ycor() < -330:
            #player.right(90)
            player.hideturtle()
            achiv.hideturtle()
            mypen.penup()
            wn.bgcolor("green")
            new_turtle=turtle.Turtle()
            new_turtle.write("game over",align="center", font=("classic", 100, "bold"))
            new_turtle.hideturtle()
            wn.title("you strite the boundary")
    if achiv.xcor()> 330 or achiv.xcor() < -330:
                achiv.right(random.randint(0,360))
    if achiv.ycor()> 330 or achiv.ycor() < -330:
                achiv.right(random.randint(0,360))
        #collision checking
    d = math.sqrt(math.pow(player.xcor()-achiv.xcor(),2)+math.pow(player.ycor()-achiv.ycor(),2))
    if d<15:
        
                #achiv.hideturtle()
                score+=1
            
                st.undo()
                st.penup()
                st.color("lime")
                st.hideturtle()
                st.setposition(-340,310)
                scorestring="score : %s" %score
                st.write(scorestring)
            
                achiv.color(random.choice(color_choice))
                achiv.setposition(random.randint(-310,310),random.randint(-310,310))
                speed+=0.01
        #move goal
    achiv.forward(1.5)
            
'''basically player and echiv are two turtles we find the distance b/w them if distance is very b/w them then achiv will dissapear or move it to a random position'''

#turtle graphics game

import os

import turtle

import math#(when both object snake and their food touches each other then their distance is very small )
import random
import time
os.system("Main Tere Kabil Hoon ke nahi.mp3&")
color_choice=["grey","red","yellow","blue","powder blue","brown","orange"]
#launch turtle window
wn= turtle.Screen()
wn.title(' basic module of turtle GAME')        
wn.bgcolor("black")
#wn.bgpic("tumblr_mduqruzbIc1qktq7uo1_500.gif")
#draw border
#first define new turtle
st=turtle.Turtle()
st.penup()
mypen=turtle.Turtle()
mypen.penup()

mypen.setposition(-350,-350)
mypen.hideturtle()
mypen.color("blue")
mypen.down()
mypen.pensize(3)
mypen.penup
for side in range (4):
        mypen.forward(700)
        mypen.left(90)
score=0
mypen.hideturtle()
#we create player in turtle:
player=turtle.Turtle()
player.color("grey")
player.shape("turtle")
player.penup()#it can't show the tail of turtle

player.speed(0)
#create some achivements
score=0
achiv=turtle.Turtle()
achiv.color(random.choice(color_choice))
achiv.shape("square")
achiv.penup()
achiv.setposition(random.randint(-200,200),random.randint(-150,230))
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
    d = math.sqrt(math.pow(player.xcor()-achiv.xcor(),2)+math.pow(player.ycor()-achiv.ycor(),2))
    
    if d<15:
            
            
            score+=1
            
            st.undo()
            st.penup()
            st.color("lime")
            st.hideturtle()
            st.setposition(-340,310)
            scorestring="score : %s" %score
            st.write(scorestring)
            #achiv.hideturtle()
            achiv.color(random.choice(color_choice))
            achiv.setposition(random.randint(-310,310),random.randint(-310,310))
            speed+=0.05
        
        
    if achiv.xcor()> 330 or achiv.xcor() < -330:

            achiv.right(random.randint(0,360))
            
    if achiv.ycor()> 330 or achiv.ycor() < -330:
            achiv.right(random.randint(0,360))
            score+=1

    if player.xcor()> 330 or player.xcor()<-330:
            player.hideturtle()
            achiv.hideturtle()
            mypen.penup()
            wn.bgcolor("green")
            new_turtle=turtle.Turtle()
            new_turtle.write("game over",align="center", font=("classic", 100, "bold"))
            new_turtle.hideturtle()
            time.sleep(2)
            
            
    if player.ycor()> 330 or player.ycor()<-330:

            player.hideturtle()
            achiv.hideturtle()
            mypen.penup()
            wn.bgcolor("green")
            new_turtle=turtle.Turtle()
            new_turtle.write("game over",align="center", font=("classic", 100, "bold") )
            new_turtle.hideturtle()
            
               #move goal
'''basically player and echiv are two turtles we find the distance b/w them if distance is very b/w them then achiv will dissapear or move it to a random position'''

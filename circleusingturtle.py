#turtle graphics game
import turtle
#launch turtle window
wn= turtle.Screen()
wn.bgcolor("lime")
#we create player in turtle:
player=turtle.Turtle()
player.color("grey")
player.shape("circle")
#set speed variable
speed=1
def right():
    global speed
    speed-=speed    
while True:#(it continues the turtle whenever this loop true)
    player.forward(speed)
    player.right(speed)
def right():
    player.stop()
    
wn.onkey(right, "Right")


wn.listen()


import random
from turtle import Turtle, Screen
turtle=Turtle()

timmy=Turtle()
timmy.speed(0)

colours=["bisque",'peach puff','light salmon','coral','tomato' ,'orange red',	'salmon',	'light coral',	'indian red']
def spirograph(gap_size: object) -> object:
    for _ in range (int((360/gap_size))) :
        timmy.color(random.choice(colours))
        timmy.circle(200)
        timmy.setheading(timmy.heading()+gap_size)

spirograph(5)






screen = Screen()
screen.exitonclick()
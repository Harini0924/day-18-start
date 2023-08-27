from turtle import Turtle, Screen
import random
timmy = Turtle()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

timmy.speed("fastest")
for i in range (100):
    timmy.color(random_color())
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading+10)
    timmy.circle(100)





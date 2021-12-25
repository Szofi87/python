from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("classic")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#def draw_shape(num_sides):
 #   angle = 360 / num_sides
  #  for _ in range(num_sides):
   #     timmy.forward(100)
    #    timmy.right(angle)


#for shape_side_n in range(3, 11):
#    timmy.color(random.choice(colours))
#    draw_shape(shape_side_n)
directions = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

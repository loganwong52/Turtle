import turtle

# Create a Turtle screen
screen = turtle.Screen()

# create a Turtle object
pen = turtle.Turtle()

# Set the speed of the turtle
pen.speed(2)

# define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    pen.color(color)
    pen.forward(100)
    pen.left(60)

print("Hello world")

# Close the turtle graphic window on click
screen.exitonclick()

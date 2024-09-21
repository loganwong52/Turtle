import turtle


def draw_hexagon(pen, colors):
    """
    colors is list of strings
    """
    # Draw a hexagon
    for color in colors:
        pen.color(color)
        pen.forward(100)
        pen.left(60)


def main():
    # Create a Turtle screen
    screen = turtle.Screen()

    # create a Turtle object
    pen = turtle.Turtle()

    # Set the speed of the turtle
    pen.speed(5)

    # define colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    draw_hexagon(pen, colors)

    # Lift up the pen
    pen.up()

    pen.forward(150)

    # Set the pen back down
    pen.down()

    draw_hexagon(pen, colors)

    # Close the turtle graphic window on click
    screen.exitonclick()


main()

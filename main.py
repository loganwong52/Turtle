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


def draw_2_hexagons(pen, colors):
    draw_hexagon(pen, colors)
    # Lift up the pen
    pen.up()
    pen.forward(150)
    # Set the pen back down
    pen.down()
    draw_hexagon(pen, colors)


def spiral(r, pen):
    # Loop for printing spiral circle
    for i in range(100):
        pen.circle(r + i, 45)


def main():
    # Create a Turtle screen
    screen = turtle.Screen()

    # create a Turtle object
    pen = turtle.Turtle()
    # pen.tracer(False)

    # Set the speed of the turtle
    pen.speed("fastest")

    # define colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # draw_2_hexagons(pen, colors)

    spiral(10, pen)
    pen.up()
    pen.right(45)
    pen.backward(200)
    pen.left(45)
    pen.down()

    r = 10
    for i in range(r, 150, 2):
        pen.circle(i)

    pen.up()
    pen.right(90)
    pen.forward(150)
    pen.left(90)
    pen.down()

    for s in range(3, 50):
        i = s - 3
        if s > len(colors):
            i = s - (int(s / len(colors)) * len(colors))
        pen.color(colors[i])
        pen.circle(50, steps=s)

    # Close the turtle graphic window on click
    screen.exitonclick()


main()

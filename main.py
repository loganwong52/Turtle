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


def concentric_circles(r, pen):
    # radius of the circle
    r = 10

    # Loop for printing concentric circles
    for i in range(50):
        pen.circle(r * i)
        pen.up()
        pen.sety((r * i) * (-1))
        pen.down()


def tangent_circles(r, pen):
    # r = 10
    for i in range(r, 150, 2):
        pen.circle(i)


def draw_shapes_inside_shapes(pen, colors):
    r = 50
    for s in range(3, 20):
        i = s - 3
        if s > len(colors):
            i = s - (int(s / len(colors)) * len(colors))
        pen.color(colors[i])
        pen.circle(r, steps=s)
        r += 5


def filled_in_circle(pen, color, r):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()


def reset_pen(pen):
    pen.up()
    pen.setpos(0, 0)
    pen.down()


def main():
    # Create a Turtle screen
    screen = turtle.Screen()

    # create a Turtle object
    pen = turtle.Turtle()

    # hide turtle
    pen.hideturtle()

    # Set the speed of the turtle
    # pen.speed("fastest")
    screen.tracer(False)

    # define colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # draw_2_hexagons(pen, colors)

    pen.up()
    pen.left(45)
    pen.backward(400)
    pen.right(45)
    pen.down()
    concentric_circles(10, pen)

    reset_pen(pen)

    spiral(10, pen)

    pen.up()
    pen.right(45)
    pen.forward(200)
    pen.left(45)
    pen.down()

    tangent_circles(10, pen)

    reset_pen(pen)

    pen.up()
    pen.goto(150, 150)
    pen.down()
    draw_shapes_inside_shapes(pen, colors)
    pen.color("black")

    pen.up()
    pen.goto(150, -150)
    pen.down()
    filled_in_circle(pen, "blue", 40)

    # Close the turtle graphic window only by using the x button
    pen.hideturtle()
    print(pen.isvisible())
    screen.mainloop()


main()

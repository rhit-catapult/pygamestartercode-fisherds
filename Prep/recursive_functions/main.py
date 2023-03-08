import rosegraphics as rg


def main():
    window = rg.TurtleWindow()
    turtle = rg.SimpleTurtle("turtle")
    turtle.speed = 20

    # for k in range(3):
    #     turtle.forward(300)
    #     turtle.left(120)
    # turtle.backward(300)
    # for k in range(3):
    #     turtle.forward(300)
    #     turtle.left(120)

    # draw_triangle(turtle, "red", 5, 100)
    # turtle.backward(150)
    # draw_triangle(turtle, "blue", 3, 180)

    # draw_two_triangles(turtle, 200)
    draw_many_triangles(turtle, 400, 80, "magenta", "blue", "aqua")

    window.close_on_mouse_click()


def draw_triangle(turtle, color, thickness, length_of_sides):
    """ :type turtle rg.SimpleTurtle """
    turtle.pen = rg.Pen(color, thickness)
    turtle.pen_down()
    for _ in range(3):
        turtle.forward(length_of_sides)
        turtle.left(120)
    turtle.pen_up()


def draw_two_triangles(turtle, length_of_sides):
    draw_triangle(turtle, "red", 5, length_of_sides)
    turtle.forward(5)
    draw_triangle(turtle, "blue", 3, length_of_sides * .9)


def draw_many_triangles(turtle, length_of_sides, thickness, color1, color2, color3):
    if thickness < 0.01:
        return
    turtle.pen.thickness = thickness
    draw_triangle(turtle, color1, thickness, length_of_sides)
    draw_many_triangles(turtle, length_of_sides * .9, thickness * 0.7, color2, color3, color1)


main()


import rosegraphics as rg


def main():
    print("Recursive Triangles")
    window = rg.TurtleWindow()
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("red", 20)
    turtle.speed = 10

    draw_triangle(turtle, "green", 10, 300)
    draw_triangle(turtle, "pink", 20, 100)

    window.close_on_mouse_click()


def draw_triangle(t, color, thickness, length_of_side):
    t.pen = rg.Pen(color, thickness)
    for k in range(3):
        t.forward(length_of_side)
        t.left(120)


main()

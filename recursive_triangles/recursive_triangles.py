import rosegraphics as rg


def main():
    print("Recursive Triangles")
    window = rg.TurtleWindow()
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("red", 20)
    turtle.speed = 10

    thickness = 5
    print(f"Before {turtle.pen.color}  {thickness}")
    draw_triangle(turtle, "green", thickness, 300)
    print(f"Middle {turtle.pen.color}  {thickness}")
    draw_triangle(turtle, "pink", 20, 100)
    print(f"End {turtle.pen.color}  {thickness}")

    # draw_two_triangles(turtle, 200)

    draw_many_triangles(turtle, 300, 20, "red", "blue", "yellow")

    window.close_on_mouse_click()


def draw_triangle(t, color, thickness, length_of_side):
    thickness = 20
    t.pen = rg.Pen(color, thickness)
    for k in range(3):
        t.forward(length_of_side)
        t.left(120)


def draw_two_triangles(turtle, length_of_sides):
    draw_triangle(turtle, "red", 15, length_of_sides)
    draw_triangle(turtle, "blue", 5, length_of_sides * 0.9)


def draw_many_triangles(turtle, length_of_side, thickness, c1, c2, c3):
    if thickness < 0.05:
        return
    draw_triangle(turtle, c1, thickness, length_of_side)
    draw_many_triangles(turtle, length_of_side * 0.9, thickness * 0.7, c2, c3, c1)


main()

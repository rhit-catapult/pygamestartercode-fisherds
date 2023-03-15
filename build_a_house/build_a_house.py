import rosegraphics as rg


def main():
    print("Build a House")
    # shapes_and_rosewindows()
    turtles_and_turtlewindows()


def turtles_and_turtlewindows():
    window = rg.TurtleWindow()

    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("red", 5)
    turtle.speed = 20

    draw_the_house(turtle)

    window.close_on_mouse_click()


def draw_the_house(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-80, -160))
    turtle.pen_down()
    for k in range(4):
        turtle.forward(160)
        turtle.left(90)


def shapes_and_rosewindows():
    # window = rg.RoseWindow(800, 500, "Build a House")
    window = rg.RoseWindow(height=400, title="Build a House", width=600)

    house_box = rg.Square(rg.Point(200, 200), 160)
    house_box.fill_color = "red"
    house_box.attach_to(window)

    roof1 = rg.Line(rg.Point(100, 120), rg.Point(200, 40))
    roof2 = rg.Line(rg.Point(200, 40), rg.Point(300, 120))
    roof3 = rg.Line(rg.Point(100, 120), rg.Point(300, 120))
    roof1.attach_to(window)
    roof2.attach_to(window)
    roof3.attach_to(window)

    window.render()

    window.close_on_mouse_click()


main()

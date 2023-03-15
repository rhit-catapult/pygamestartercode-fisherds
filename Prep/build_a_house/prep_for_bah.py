import rosegraphics as rg


def main():
    print("Build a House")
    shapes_and_rosewindows()
    turtles_and_turtlewindows()


def shapes_and_rosewindows():
    window = rg.RoseWindow(title="Shapes")
    rect = rg.Rectangle(rg.Point(100, 100), rg.Point(200, 200))
    rect.attach_to(window)
    window.render()
    window.close_on_mouse_click()


def turtles_and_turtlewindows():
    window = rg.TurtleWindow()
    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("blue", 3)
    turtle.speed = 20  # Optional - Faster!

    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-80, -160))
    turtle.pen_down()
    for k in range(4):
        turtle.forward(160)
        turtle.left(90)

    window.close_on_mouse_click()



main()

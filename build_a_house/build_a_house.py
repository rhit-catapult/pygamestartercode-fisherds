import rosegraphics as rg


def main():
    print("Build a House")
    # shapes_and_rosewindows()
    # turtles_and_turtlewindows()
    build_a_house_menu()

def build_a_house_menu():
    window = rg.TurtleWindow()

    turtle = rg.SimpleTurtle("turtle")
    turtle.pen = rg.Pen("red", 5)
    turtle.speed = 20

    # draw_the_house(turtle)

    while True:
        print("1: House, 2: Roof, 3: Door, 4: Window, 5: Doorknob, 6: Chimney")
        print("r: Red, b: Blue, g: Green")
        print("0: to exit")
        selection = input("Selection: ")
        if selection == "0":
            break
        if selection == "1":
            draw_the_house(turtle)
        if selection == "g":
            turtle.pen.color = "green"
        if selection == "r":
            turtle.pen.color = "red"
        if selection == "b":
            turtle.pen.color = "blue"
        if selection == "2":
            draw_the_roof(turtle)

    # window.close_on_mouse_click()


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


def draw_the_roof(turtle):
    turtle.pen_up()
    turtle.set_heading(0)
    turtle.go_to(rg.Point(-100, 0))
    turtle.pen_down()
    for k in range(3):
        turtle.forward(200)
        turtle.left(120)

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

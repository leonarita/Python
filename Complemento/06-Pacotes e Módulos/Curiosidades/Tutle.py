import turtle


def Square():
    skk = turtle.Turtle()
    for i in range(4):
        skk.forward(50)
        skk.right(90)
    turtle.done()


def Star():
    star = turtle.Turtle()
    for i in range(50):
        star.forward(50)
        star.right(144)
    turtle.done()


def Hexagon():
    polygon = turtle.Turtle()
    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides
    for i in range(num_sides):
        polygon.forward(side_length)
        polygon.right(angle)
    turtle.done()


i = 1
while i != 0:
    i = int(input("Digite 1 (quadrado), 2 (estrela), 3 (hexágono) ou 0 (Sair) : "))
    if i == 1:
        Square()
    elif i == 2:
        Star()
    elif i == 3:
        Hexagon()
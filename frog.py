import turtle as t


def ellipse(rad):
    # rad --> radius of arc
    for i in range(2):
        # two arcs
        t.circle(rad, 90)
        t.circle(rad // 8, 90)


# Main section
# tilt the shape to negative 45

t.title("Frog")
t.setup(800, 800)
# малюємо вісь x
t.setposition(-400, 0)
t.forward(800)
# повертаємось в точку (0, 0)
t.home()
t.up()
t.goto(250, 0)
t.down()
t.setheading(90)
t.color('lime green')
# малюємо тіло
t.begin_fill()
t.circle(250, extent=180)
t.end_fill()
t.setheading(90)
t.goto(-200, -50)
t.begin_fill()
t.circle(50, extent=180)
t.end_fill()
t.up()
# малюємо нижня частина лапки
t.goto(300, -50)
t.down()
t.setheading(90)
t.begin_fill()
t.circle(50, extent=180)
t.end_fill()
t.up()
# малюємо очі
t.goto(-160, 200)
t.setheading(0)
t.down()
t.begin_fill()
t.circle(50)
t.end_fill()
t.color('white')
t.up()
t.goto(-160, 215)
t.down()
t.begin_fill()
t.circle(30)
t.end_fill()
t.setheading(0)
t.goto(-150, 225)
t.color('black')
t.begin_fill()
t.circle(20)
t.end_fill()
t.up()
t.goto(-255, 0)
t.down()
t.seth(60)
t.begin_fill()
t.color('dark green')
ellipse(120)
t.end_fill()
t.up()
t.goto(255, 0)
t.down()
t.seth(30)
t.begin_fill()
t.color('dark green')
ellipse(120)
t.end_fill()
t.mainloop()

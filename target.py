import turtle as t

# turtle.circle(radius, extent=None, steps=None)
t.title('circle')
t.setup(600, 600)
t.color('brown', 'orange')
t.width(1)
# малюємо вісь x
t.setposition(-300, 0)
t.forward(600)
t.up()
t.goto(0, -300)
t.down()
t.left(90)
t.forward(600)
# повертаємось в точку (0, 0)
t.home()
t.setheading(0)
t.color('black')
t.up()
t.goto(0, -160)
t.begin_fill()
t.down()
t.circle(160)
t.end_fill()
t.up()
t.goto(0, -120)
t.down()
t.begin_fill()
t.color('blue')
t.circle(120)
t.end_fill()
t.up()
t.goto(0, -80)
t.down()
t.begin_fill()
t.color('red')
t.circle(80)
t.end_fill()
t.up()
t.goto(0, -40)
t.down()
t.begin_fill()
t.color('yellow')
t.circle(40)
t.end_fill()
t.hideturtle()
t.mainloop()
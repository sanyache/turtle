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
t.up()
t.goto(-150, 0)
t.setheading(0)
t.down()
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(300)
    t.left(170)
    print(int(t.xcor()), t.ycor())
    if int(t.xcor()) == -149 and t.ycor() < 1:
        break
t.end_fill()
t.mainloop()
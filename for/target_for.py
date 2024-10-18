import turtle as t

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

colors = ['black', 'blue', 'red', 'yellow']

for i in range(4):
    t.up()
    t.goto(0, -160 + 40*i)
    t.down()
    t.color(colors[i])
    t.begin_fill()
    t.circle(160 - 40*i)
    t.end_fill()

t.mainloop()
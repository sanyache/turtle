import turtle as t

t.title('circle')
t.setup(840, 802)
t.color('brown', 'orange')
t.width(1)
# малюємо вісь x
t.setposition(-400, 0)
t.forward(800)
# малюємо вісь y
t.up()
t.goto(0, -400)
t.down()
t.left(90)
t.forward(800)
# переходимо в точку де розпочнемо малювання квадратів
t.up()
t.setheading(0)
t.width(3)
t.goto(-400, 0)
colors = ['blue', 'green', 'orange', 'dark magenta', 'yellow']
# малювання квадрата
for j in range(5):
    t.down()
    t.color('black', colors[j])
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.up()
    t.forward(175)

t.mainloop()

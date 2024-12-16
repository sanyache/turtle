import turtle as t
import random

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
# повертаємося в початок координат
t.up()
t.home()
t.down()
colors = ['red', 'blue', 'magenta', 'white', 'lime green', 'indigo']
# малюємо прямокутник
for degree in range(0, 360, 40):
    t.color('black', colors[degree//40%6])
    t.down()
    t.begin_fill()
    t.setheading(degree)
    for i in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()
    t.up()
    t.delay(20)
t.mainloop()
"""
Створення прямокутника за допомогою цикла for
"""
import turtle as t
import random

def rectangle(r_x, r_y, rec_len, color_line, color_bg):
    t.up()
    t.goto(r_x, r_y)
    t.down()
    t.color(color_line, color_bg)
    t.begin_fill()
    for i in range(4):
        t.forward(rec_len)
        t.left(90)
    t.end_fill()


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
# переходимо в початок координат
t.up()
t.setheading(0)
t.width(3)
colors = ['black', 'blue', 'red', 'yellow']
# розпичинаю малювати прямокутник
for i in range(4):
    rectangle(-200 + 50*i ,-200 + 50*i, (200-50*i)*2, 'black', colors[i])
t.mainloop()
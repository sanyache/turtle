"""
Створення прямокутника за допомогою цикла for
"""
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
# переходимо в початок координат
t.up()
t.setheading(0)
t.width(3)
t.color('black', 'blue')
t.home()
# розпичинаю малювати прямокутник
t.down()
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
    print(i)
t.end_fill()
t.mainloop()
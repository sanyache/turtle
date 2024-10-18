import turtle as t
import random
from pydoc import replace

t.title('circle')
t.setup(800, 800)
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
t.up()
t.setheading(0)
# створюємо список координат (лівий нижній кут прямокутника)
coordinates = [(-350,250), (-250,50), (-150,200), (50,100), (150, 250),
               (150, -50), (-350,-250), (-200,-150), (-100, -300), (250,-300)]
# створюємо список кольорів
colors = ['red', 'blue', 'magenta', 'lime green', 'indigo',
          'purple', 'light coral', 'dark orange']
for x, y in coordinates:
    t.goto(x, y)
    t.down()
    random.shuffle(colors)
    t.color('black', random.choice(colors))
    t.begin_fill()
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.up()
t.mainloop()
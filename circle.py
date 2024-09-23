import turtle as t

# turtle.circle(radius, extent=None, steps=None)
t.title('circle')
t.setup(600, 600)
t.color('brown', 'orange')
t.width(3)
# малюємо вісь x
t.setposition(-300, 0)
t.forward(600)
# повертаємось в точку (0, 0)
t.home()
t.begin_fill()
# розвертаємо перо, щоб шестикутник стояв на бічній грані
t.right(30)
#  малюємо шестикутник
t.circle(100, steps=6)
t.end_fill()
t.up()
t.goto(-200, 0)
t.down()
# встановлюємо позицію пера
t.setheading(270)
# малюємо півкруг
t.begin_fill()
t.circle(100, 180)
t.end_fill()
t.mainloop()

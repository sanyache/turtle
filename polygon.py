import turtle as t

t.title("Polygon")
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
t.mainloop()


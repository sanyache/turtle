import turtle as t

t.title('Grass and sun')
t.bgcolor('LightSkyBlue')
t.setup(1000, 1200)
t.width(6)
t.speed(0)

# draw the sun
t.color("Yellow")
t.penup()
t.goto(350, 400)
t.down()
t.begin_fill()
for i in range(50):
    t.forward(60)
    if i % 2 == 0:
        t.right(180)
    else:
        t.left(160)
t.end_fill()


# draw the flower
t.up()
t.color('brown')
t.goto(-50, 0)
t.down()
t.goto(0, -500)
t.up()
t.home()
t.down()
t.begin_fill()
t.color('DeepPink')
for i in range(72):
    t.forward(60)
    if i % 2 == 0:
        t.right(170)
    else:
        t.left(160)
t.end_fill()


# draw the grass
t.setheading(85)
t.penup()
t.goto(-500, -520)
t.down()
t.color('DarkGreen')
t.begin_fill()
for i in range(120):
    t.forward(100)
    if i % 2 == 0:
        t.right(170)
    else:
        t.left(170)
t.end_fill()
t.mainloop()

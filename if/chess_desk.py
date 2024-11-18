import turtle as t

t.title("Chess desk")
t.setup(800, 800)
t.speed(0)
t.color('black')
t.up()
#t.goto(-400, -400)
t.setheading(0)
for row in range(8):
    for column in range(8):
        t.goto(-400 + column * 100, -400 + row * 100)
        t.down()
        print((row+column)%2)
        if (row + column) % 2 == 0:
            t.color('black', 'white')
        else:
            t.color('black', 'black')
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
        t.up()
t.mainloop()
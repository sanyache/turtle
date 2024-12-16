import turtle as t

def sq(x, y, l, color):
    t.color('black', color)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for _ in range(4):
        t.forward(l)
        t.left(90)
    t.end_fill()

def fractal(x, y, l, depth=0):
    colors = ['yellow','gold', 'orange',  'goldenrod', 'dark goldenrod']
    color = colors[depth%len(colors)]
    sq(x, y ,l, color)
    if l < 10:
        return
    fractal(x - l * 0.2, y - l * 0.2, l * 0.4, depth + 1)
    fractal(x - l * 0.2, y + l * 0.8, l * 0.4, depth + 1)
    fractal(x + l * 0.8, y + l * 0.8, l * 0.4, depth + 1)
    fractal(x + l * 0.8, y - l * 0.2, l * 0.4, depth + 1)


t.setup(1000, 1000)
t.title("Rectangle fractal")
t.bgcolor('gray')
t.speed(0)
t.color('black', 'orange')
fractal(-100, -100, 200)
t.mainloop()
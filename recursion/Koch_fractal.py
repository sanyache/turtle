import turtle as t

def koch(l, level):
    if level == 0:
        t.forward(l)
        return
    l /= 3.0
    koch(l, level-1)
    t.left(60)
    koch(l, level - 1)
    t.right(120)
    koch(l, level - 1)
    t.left(60)
    koch(l , level - 1)


t.setup(1000, 1000)

t.up()
t.goto(-300, 0)
t.down()
koch(600, 3)
t.mainloop()
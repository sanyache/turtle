import turtle as t

t.title("forward while")
t.setup(600, 800)
t.speed(0)
t.width(3)
t.up()
t.color('black', 'brown')
t.goto(100, 250)
t.begin_fill()
t.setheading(0)
t.circle(50)
t.end_fill()
t.home()
t.down()
colors = ['blue', 'orange', 'green', 'yellow', 'brown']
t.left(5)
i = 0
t.color(colors[0])
run = True
while run:
    if t.xcor() > 300 or t.xcor() < -300 or t.ycor() > 400 or t.ycor() < -400:
        i += 1
        i = i % 5
        t.color(colors[i])
        t.left(95)

        t.forward(50)
    t.forward(5)
    if  50 < t.xcor() < 150 and  250 < t.ycor() < 350:
        print("boom!!!")
        t.forward(10)
        run = False


t.mainloop()

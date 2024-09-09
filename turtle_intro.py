import turtle as t

t.title("house")  # заголовок вікна
t.setup(600, 800)  # встановлюємо розміри вікна
t.shape("turtle")  # встановлюємо вигляд пера
t.color('dim gray', 'peru')  # встановлюємо колір контуру і заливки
t.width(3)  # встановлюємо тощину пера
t.begin_fill()  # з цього місця розпочинається заливка фігури
# малюємо прямокутник
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()  # з цього місця закінчується заливка фігури
t.up()  # підняли перо
t.goto(0, 100)  # перемістили перо
t.down()  # опустили перо
t.color('dim gray', 'saddle brown')
# малюємо дах і заливаємо отриману область
t.begin_fill()
t.goto(50, 150)
t.goto(100, 100)
t.end_fill()
# піднімаємо перо
t.up()
t.goto(50, 25)
t.down()
t.color('black', 'alice blue')
t.begin_fill()
# малюємо вікно
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.end_fill()
t.up()
t.goto(-150, 300)
t.down()
t.color('yellow')
# малюємо круг
t.begin_fill()
t.circle(40)
t.end_fill()
# ховаємо перо
t.hideturtle()
t.mainloop()

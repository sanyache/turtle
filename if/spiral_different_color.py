import turtle as t

t.title("spiral")
t.setup(600, 600)

t.bgcolor('#043c4d')
t.width(5)
t.color('#7ef582')
colors = ['light steel blue', 'CornFlowerBlue', 'royal blue',
          'blue', 'MediumBlue', 'navy', 'dark blue', 'midnight blue']
spiral = 0
for i in range(4, 300, 4):
    # if i > 100:
    if spiral%6 == 0:
        t.color(colors[spiral//6%8])
        print(spiral//6%8)
    t.forward(i)
    t.right(60)
    spiral += 1

t.mainloop()


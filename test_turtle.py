import turtle

# t = turtle.Pen()
# turtle.bgcolor("black")
# sides = 6
# colors = ["red", "yellow", "green", "blue", "orange", "purple"]
# for x in range(360):
#     t.pencolor(colors[x % sides])
#     t.forward(x * 3 / sides + x)
#     t.left(360 / sides + 1)
#     t.width(x * sides / 200)


# t = turtle.Pen()
# turtle.bgcolor("black")
# # sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
# sides = 6
# colors = ["red", "yellow", "green", "blue", "orange", "purple"]
# for x in range(360):
#     t.pencolor(colors[x % sides])
#     t.forward(x * 3 / sides + x)
#     t.left(360 / sides + 1)
#     t.width(x * sides / 180)
#     t.left(91)

t = turtle.Pen()
turtle.bgcolor("black")

my_name = turtle.textinput("输入你的姓名", "你的名字？")
colors = ["red", "yellow", "purple", "blue"]
for x in range(100):
    t.pencolor(colors[x % 4])
    t.penup()
    t.forward(x * 4)
    t.pendown()
    t.write(my_name, font=("Arial", int((x + 4) / 4), "bold"))
    t.left(92)

print("####结束####")

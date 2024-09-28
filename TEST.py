from turtle import *

def draw_windmill():
    speed(10)  # 设置画笔速度
    bgcolor("skyblue")  # 设置背景颜色

    # 画风车中心
    penup()
    goto(0, -20)
    pendown()
    fillcolor("gray")
    begin_fill()
    circle(20)  # 中心圆
    end_fill()

    # 画风车的扇叶
    for i in range(4):  # 画4个扇叶
        penup()
        goto(0, 0)  # 移动回中心点
        pendown()
        seth(i * 90)  # 旋转每个扇叶的方向
        fillcolor("green")
        begin_fill()
        fd(10)  # 中心的短边
        left(45)
        fd(100)  # 扇叶的长度
        left(90)
        fd(100)  # 扇叶的另一边
        left(45)
        fd(10)  # 扇叶连接中心的短边
        end_fill()

    # 画风车的支柱
    penup()
    goto(-15, -20)
    seth(-90)
    pendown()
    fillcolor("brown")
    begin_fill()
    fd(200)  # 支柱的长度
    right(90)
    fd(30)  # 支柱的宽度
    right(90)
    fd(200)
    end_fill()

    # 画地面
    penup()
    goto(-300, -220)
    seth(0)
    pendown()
    fillcolor("lightgreen")
    begin_fill()
    fd(600)  # 地面的长度
    right(90)
    fd(50)  # 地面的高度
    right(90)
    fd(600)
    end_fill()

    hideturtle()
    done()

draw_windmill()

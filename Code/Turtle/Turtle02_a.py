'''
功能：绘制同心圆
重点：随机数的概念、颜色的表示方法、range函数的用法
作者：薛景
最后修改于：2019/05/27
'''

import turtle
t = turtle.Turtle()
t.shape("turtle")

'''
计算机中表示颜色的第二种方法是用三个0~255的整数来表示红、绿、蓝，通过百度我们可
以查到七种彩虹颜色的标准配比，但是在使用这种模式表示颜色之前，必须使用colormode
函数改变小海龟的颜色模式，下面列表中的每一个三元组都是一种颜色，最后一个是天蓝色。
'''
turtle.colormode(255)
colors = [(255,0,0), (255,165,0), (255,255,0), (0,255,0),\
    (0,127,255), (0,0,255), (139,0,255), "skyblue"]
turtle.bgcolor(colors[7])   # 把背景设置成天蓝色，注意列表元素的序号从0开始哟

for i in range(10, 2, -1):
    t.color(colors[10-i])   # 从colors列表中顺序选择其中的颜色
    t.begin_fill()          # 与同心圆不同，构成半圆区域的起始点就是原点
    t.goto(20*i, 0)
    t.setheading(90)
    t.circle(20*i, 180)     # 第二个参数表示绘制弧的角度，180度就是半圆
    t.home()                # 回到海龟初始的位置，构成封闭的半圆形
    t.end_fill()            # 对这个封闭的半圆进行颜色填充
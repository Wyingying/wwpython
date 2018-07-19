import turtle
import time 
def drawline(draw): ##画线
      turtle.penup()
      turtle.fd(5)
      turtle.pendown() if draw else turtle.penup()
      turtle.fd(20)
      turtle.penup()
      turtle.fd(5)
      turtle.right(90)
      
def drawdigit(digit):  ##0-9的数字绘制
      
      drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
      drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
      drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
      drawline(True) if digit in [0,2,6,8] else drawline(False)
      turtle.left(90)
      drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
      drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
      drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
      
      turtle.left(180)
      turtle.penup()
      turtle.fd(20)
def drawdate(date):  ##绘制日期
      turtle.pencolor("red")
      for i in date:
            if i=="-":
                  turtle.write("年",font=("Arial",20,"normal"))
                  turtle.pencolor("green")
                  turtle.fd(40)
            elif i=="+":
                  turtle.write("月",font=("Arial",20,"normal"))
                  turtle.pencolor("blue")
                  turtle.fd(40)
            elif i=="=":
                  turtle.write("日",font=("Arial",20,"normal"))
            elif i=="1":
                  turtle.bk(30)
                  drawdigit(eval(i))
            else:
                  drawdigit(eval(i))
      turtle.fd(60)
                  
def drawtime(time):  ##绘制时间
      turtle.pencolor("red")
      for i in time:
            if i=="-":
                  turtle.write(":",font=("Arial",20,"normal"))
                  turtle.pencolor("green")
                  turtle.fd(20)
            elif i=="+":
                  turtle.write(":",font=("Arial",20,"normal"))
                  turtle.pencolor("blue")
                  turtle.fd(20)
            elif i=="1":
                  turtle.bk(30)
                  drawdigit(eval(i))
            else:
                  drawdigit(eval(i))
                  
def main():
      turtle.setup(900,350,200,200)
      turtle.penup()
      turtle.fd(-420)
      turtle.pensize(5)
      turtle.speed(10)
      drawdate(time.strftime("%Y-%m+%d=",time.gmtime()))
      drawtime(time.strftime("%H-%M+%S",time.gmtime()))
      
      turtle.hideturtle()
      turtle.done()
main()

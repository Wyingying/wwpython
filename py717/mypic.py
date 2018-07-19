'''
将现在时间用画布实时的画出来:
'''
import datetime
import turtle
#strftime
now_time = datetime.datetime.now().strftime("%Y年%m月%d日")
turtle.pensize(8)
turtle.pencolor("green")
#turtle.penup()
#turtle.left(90)
#turtle.pendown()
#turtle.forward(50)
#
#turtle.left(90)
#turtle.forward(50)

#turtle.left()
#turtle.penup()
#turtle.begin_fill()
#turtle.end_fill()
turtle.hideturtle()
#turtle.done()
def pic(i):
	if  i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 8 or i ==9:
		turtle.pendown()
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.forward(40)
	if i == 0 or i==1 or i == 2 or i==3 or i==4 or i==7 or i==8 or i== 9:
		turtle.pendown()
		turtle.left(90)
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.left(90)
		turtle.forward(40)
	if i == 0 or i==2 or i == 3 or i == 5 or i == 6 or i== 7 or i == 8 or i== 9:
		turtle.pendown()
		turtle.left(90)
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.left(90)
		turtle.forward(40)
	if i == 0 or i == 4 or i ==5 or i ==6 or i == 8 or i == 9:
		turtle.pendown()
		turtle.left(90)
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.left(90)
		turtle.forward(40)
	if i == 0 or i == 2 or i == 6 or i == 8:
		turtle.pendown()
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.forward(40)	
	if i == 0 or i == 2 or i == 3 or i == 5 or i == 6 or i == 8 or i == 9:
		turtle.pendown()
		turtle.left(90)
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.left(90)
		turtle.forward(40)
	if i == 0 or i ==1 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
		turtle.pendown()
		turtle.left(90)
		turtle.forward(40)
	else:
		turtle.penup()
		turtle.left(90)
		turtle.forward(40)
	turtle.right(90)
	turtle.penup()
	turtle.fd(20)	
def main():
	
	turtle.setup(800,200,20,20)
	turtle.penup()
	turtle.bk(300)
	#turtle.done()
	for s in now_time:
		if s in ("年","月","日"):
			turtle.forward(20)
			turtle.write(s,font=("Arial",20,"normal"))
			turtle.forward(30)
		else:
			
			pic(int(s))
	turtle.done()

main()

# 统计用户输入变量的前n项和

n = int(input("请输入你要计算的值："))
s=0
i=0
while i<= n:
	s=s+i
	i+=1
	
print("前{0}项的和为{1}：".format(n,s))



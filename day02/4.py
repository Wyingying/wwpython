#读入一列整型数，判断是否是回文整形

num = int(input("请输入一个整型数："))
new_num=0
sava=num
while num:
	new_num=new_num*10+num%10
	num=num//10
if new_num==sava:
	print("{}是一个回文整型".format(sava))
else:
	print("{}不是一个回文整型".format(sava))

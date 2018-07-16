
#1.读入用户输入的两个整型数，判断其大小关系

num1,num2=eval(input("请输入个数字："))

if num1 > num2:
	print("第一个数字大于第二个数")
elif num1 < num2:
	print("第二个数字大于第一个数字")
else:
	print ("两个数字相等")

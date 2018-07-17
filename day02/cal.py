'''
能被4整除，不能被100整除，或能被400整除的是闰年
已知1990一月1日是星期一，求你输入的年份的月是星期几
'''

da = input("请输入你要想要查询的日期：")
#1996.5
y = int(da.split(".")[0])
m = int(da.split(".")[1])
sum1=0
for i in range(1990,y):
	if (i%4 == 0 and i%100 != 0) or (i%400 == 0):
		sum1+=366
	else:
	
		sum1+=365

#1.3.5.7.8.10.12 31
for i in range(1,m):
	if i==1 or i==3 or i==5 or i==7 or i == 8 or i==10 or i==12:
		sum1+=31
	elif i==4 or i==6 or i==9 or i==11:
		sum1+=30
	else:
		sum1+=(28+(y%4==0 and y%100!=0) or( y%400==0))
sum2 = sum1+1
#print(sum1,sum2)
#print(sum3)
#1990.1.1日星期一 除以7后的余数是3
week = sum2%7
if m==1 or m==3 or m==5 or m==7 or m == 8 or m==10 or m==12:
	days=31
elif m==4 or m==6 or m==9 or m==11:
	days=30
else:
	days=(28+(y%4==0and y%100!=0 or y%400==0))
titlestr = "{}月 {}".format(m,y)
print(titlestr.center(20))
print("日 一 二 三 四 五 六")
for i in range(week):
	print("   ",end='')
for d in range(1,days+1):
	print("{:>2}".format(d),end="\n" if (week+d)%7==0 else " ")
print()

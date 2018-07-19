'''
能被4整除，不能被100整除，或能被400整除的是闰年
已知1990一月1日是星期一，求你输入的年份的月是星期几
'''
'''
定义一个判断闰年的函数

'''
def isleap(year):
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

'''
定义计算每月多少天的函数
'''
def monthday(month,year):
	if month==1 or month==3 or month==5 or month==7 or month == 8 or month==10 or month==12:
		day=31
	elif month==4 or month==6 or month==9 or month==11:
		day=30
	else:
		day=(28+ isleap(year))
	return day
da = input("请输入你要想要查询的日期：")
#1996.5
y = int(da.split(".")[0])
m = int(da.split(".")[1])
sum1=0
for i in range(1990,y):
	if isleap(i):
		sum1+=366
	else:
	
		sum1+=365

#1.3.5.7.8.10.12 31
for i in range(1,m):
	sum2+=monthday(i,y)
sum2 = sum1+1
#print(sum1,sum2)
#print(sum3)
#1990.1.1日星期一 除以7后的余数是3
week = sum2%7
days = monthday(m,y)
titlestr = "{}月 {}".format(m,y)
print(titlestr.center(20))
print("日 一 二 三 四 五 六")
for i in range(week):
	print("   ",end='')
for d in range(1,days+1):
	print("{:>2}".format(d),end="\n" if (week+d)%7==0 else " ")
print()

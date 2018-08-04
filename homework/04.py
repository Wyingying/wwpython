'''
1.读入10个学生的成绩，要求在0~100之间，定义一个函数,
统计10个学生成绩的平均分，最高分，和最低分

2.随机产生10个10以内的整型数，存放到列表中，将列表中的最大值放在列表的最后。

3.随机产生密码：
	在26个大小写字母和10个数字组成的列表中，随机生成10个8位密码

4.定义一个列表，列表中有20个随机产生的100以内的整型数,
定义一个函数，统计20个整型数的分布情况。
每有一个数值在其所属区域打印一个*
例如5个100， 3个85,88,89
100:*****
90~99:
80~89:***
...
0~9:
'''
'''
s = eval(input("请输入10个学生的成绩(0-100)用逗号隔开："))
s = list(s)

def average(s):
	sn = 0
	for i in s:
		sn += i
	n = len(s)
	return sn/n

ave = average(s)

print("这10个学生的平均分为：",ave)

import random

l1 = []
for i in range(0,10):
	l1.append(random.randint(0,9))
print(l1)
l = len(l1)
for i in range(0,l-1):
	flag= False
	for j in range(1,l-i):
		if l1[i] > l1[j]:
			t = l1[i]
			l1[i]= l1[j]
			l1[j]= t
			flag = True
	if not flag:
		break
print(l1)


import random
def bubble_sort(data):
	for i in range(len(data) - 1):
		indicator = False 
		for j in range(len(data) - 1 - i):
			if data[j] > data[j + 1]:
				data[j], data[j+1] = data[j+1], data[j]
				indicator = True
		if not indicator:
			break
	

data = list(range(10))
random.shuffle(data)
print(data)
bubble_sort(datai)
print(data)

#3.
import random

l =list(range(0,10))

for i in range(ord('a'),ord('z')):
	l.append(chr(i))
for i in range(ord('A'),ord('Z')):
	l.append(chr(i))
def rad():
	for i in range(0,10):	
		s=random.sample(l,8)
		print(s)
		
rad()

'''
import random

l = []
for i in range(0,21):
	l.append(random.randint(0,99))

def dieve(l):
	length = len(l)
	a,b,c,d,e,f,g,h,k,s,m=0,0,0,0,0,0,0,0,0,0,0
	for i in range(0,length):
		
		if l[i]==100:
			a +=1
		if 90<=i and i<=99:
			b +=1
		if 80 <=l[i] and l[i] <=89:
			c +=1
		if 70 <=l[i] and l[i]<= 79:
			d +=1
		if 60 <= l[i] and l[i] <=69:
			e +=1
		if 50 <= l[i] and l[i] <= 59:
			f +=1
		if 40 <= l[i] and l[i]<=49:
			g +=1
		if 30 <=l[i] and l[i]<=39:
			h +=1
		if 20 <= l[i] and l[i] <=29:
			k +=1
		if 10 <= l[i] and l[i]<=19:
			s +=1
		if 0 <= l[i] and l[i] <=9:
			m +=1
	s=[]
	s.apeend(a)
	s.append(b)
	s.append(c)
	s.append(d)
	s.append(e)
	s.append(f)
	s.append(g)
	s.append(h)
	s.append(k)
	s.append(s)
	s.append(m)
	return s

			 

			
print(dieve(l))


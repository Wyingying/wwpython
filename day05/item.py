'''
如何在一个for语句中迭代多个可迭代对象
并行--使用内置函数zip，它能将多个可迭代对象合并，每次返回一个元祖
串行--使用标准库中的itertools.chain，它能将多个可迭代对象连接
'''
import random
from itertools import chain
math = [random.randint(60,100) for i in range(40)]
english = [random.randint(60,100) for i in range(40)]
chinese= [random.randint(60,100) for i in range(40)]
for a,b,c in zip(math,english,chinese):
	print("每个学生的总分为:{}".format(a+b+c))

e1 = [random.randint(60,100) for i in range(40)]
e2 = [random.randint(60,100) for i in range(40)]
e3 = [random.randint(60,100) for i in range(40)]
e4 = [random.randint(60,100) for i in range(40)]
count = 0
for i in chain(e1,e2,e3,e4):
	if i>90:
		count+=1
print("这四个班级成绩大于90分的人数为:{}".format(count))
